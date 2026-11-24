"""Read-only Betfair Exchange goals scanner.

Pulls Over/Under 2.5 / 3.5 / 4.5 prices for upcoming football matches,
rates each line with the goals model, and lists bets that pass the rules.
It never places a bet.

Usage (Windows PowerShell, inside this folder):
    python scan.py                 # next 24 hours
    python scan.py --hours 48      # next 48 hours
    python scan.py --selftest      # check the model maths, no Betfair login
"""
import argparse
import configparser
import csv
import datetime as dt
import difflib
import getpass
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MARKETS = {"OVER_UNDER_25": 2.5, "OVER_UNDER_35": 3.5, "OVER_UNDER_45": 4.5}
BOOK_CHUNK = 40  # keeps each listMarketBook request under Betfair's data-weight limit


# ---------------- model ----------------
def poisson_at_least(lam, k):
    return 1 - sum(math.exp(-lam) * lam ** i / math.factorial(i) for i in range(k))


def expected_goals(home, away, league_avg, shrink, home_adv):
    """home/away = (played, goals_for, goals_against). Returns (home_xg, away_xg)."""
    r = lambda x: shrink * x + (1 - shrink) * league_avg
    hp, hf, ha = home
    ap, af, aa = away
    home_xg = r(hf / hp) * r(aa / ap) / league_avg * home_adv
    away_xg = r(af / ap) * r(ha / hp) / league_avg / home_adv
    return home_xg, away_xg


def line_chance(total_xg, line, side):
    over = poisson_at_least(total_xg, int(line + 0.5))
    return over if side == "Over" else 1 - over


# ---------------- data ----------------
def load_teams(path):
    teams = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if not row.get("team"):
                continue
            teams[row["team"].strip().lower()] = {
                "league": row["league"].strip(),
                "played": int(row["played"]),
                "gf": int(row["goals_for"]),
                "ga": int(row["goals_against"]),
                "league_avg": float(row["league_avg_goals_per_team"]),
                "estimated": row.get("estimated", "").strip().lower() in ("yes", "y", "1", "true"),
            }
    return teams


def find_team(name, teams):
    key = name.strip().lower()
    if key in teams:
        return key
    words = set(key.replace("-", " ").split())
    # Never map youth, reserve or women's sides onto a senior team's data.
    if words & {"u18", "u19", "u20", "u21", "u23", "ii", "b", "w", "women", "reserves", "res", "jong"}:
        return None
    match = difflib.get_close_matches(key, teams.keys(), n=1, cutoff=0.8)
    if match:
        return match[0]
    # Betfair often adds a prefix or suffix ("AC Monza", "FC Utrecht", "Celtic FC"):
    # accept a team name that appears as whole words inside the Betfair name, or vice versa.
    for team in teams:
        team_words = set(team.replace("-", " ").split())
        shorter, longer = sorted((team_words, words), key=len)
        if shorter and shorter <= longer and len(" ".join(shorter)) >= 4:
            return team
    return None


def load_config():
    cfg = configparser.ConfigParser()
    path = os.path.join(HERE, "config.ini")
    if not os.path.exists(path):
        sys.exit("config.ini not found. Copy config.example.ini to config.ini and fill it in.")
    cfg.read(path)
    return cfg


# ---------------- betfair ----------------
def betfair_client(cfg):
    import betfairlightweight  # imported here so --selftest works without it

    bf = cfg["betfair"]
    password = getpass.getpass("Betfair password (not stored): ")
    certs = bf.get("certs_folder", "").strip()
    client = betfairlightweight.APIClient(bf["username"], password, app_key=bf["app_key"], certs=certs or None)
    if certs:
        client.login()  # certificate login
    else:
        client.login_interactive()  # username/password login
    return client


def setup_app_key(cfg):
    """Fetch (or create) the account's delayed app key and write it into config.ini."""
    import re
    import requests

    client = betfair_client(cfg)  # login does not need a valid app key

    def account_call(method, params):
        # The app-key operations only need the session token (no X-Application header).
        resp = requests.post(
            "https://api.betfair.com/exchange/account/json-rpc/v1",
            json={"jsonrpc": "2.0", "method": "AccountAPING/v1.0/" + method, "params": params, "id": 1},
            headers={"X-Authentication": client.session_token, "Content-Type": "application/json"},
            timeout=30,
        )
        data = resp.json()
        if "error" in data:
            sys.exit(f"Betfair refused {method}: {data['error']}")
        return data["result"]

    apps = account_call("getDeveloperAppKeys", {}) or []
    if not apps:
        print("No app keys yet - creating them...")
        apps = [account_call("createDeveloperAppKeys", {"appName": "goals-scanner"})]
    delayed = [v for app in apps for v in app.get("appVersions", []) if v.get("delayData")]
    if not delayed:
        sys.exit("Could not find a delayed app key on this account. Check developer.betfair.com.")
    key = delayed[0]["applicationKey"]
    if not delayed[0].get("active", True):
        print("Note: Betfair shows this delayed key as inactive.")
    path = os.path.join(HERE, "config.ini")
    with open(path, encoding="utf-8") as f:
        text = f.read()
    text = re.sub(r"(?m)^app_key\s*=.*$", "app_key = " + key, text)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Delayed app key saved to config.ini. Now run: python scan.py")


def fetch_markets(client, hours):
    from betfairlightweight import filters

    now = dt.datetime.now(dt.timezone.utc)
    mfilter = filters.market_filter(
        event_type_ids=["1"],  # football
        market_type_codes=list(MARKETS),
        market_start_time={
            "from": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "to": (now + dt.timedelta(hours=hours)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        },
    )
    catalogue = client.betting.list_market_catalogue(
        filter=mfilter,
        # Zero-weight projections only, so 1000 markets stay inside Betfair's data limit.
        market_projection=["EVENT", "COMPETITION", "RUNNER_DESCRIPTION", "MARKET_START_TIME"],
        max_results=1000,
        sort="FIRST_TO_START",
    )
    books = {}
    ids = [m.market_id for m in catalogue]
    for i in range(0, len(ids), BOOK_CHUNK):
        chunk = client.betting.list_market_book(
            market_ids=ids[i : i + BOOK_CHUNK],
            price_projection=filters.price_projection(price_data=["EX_BEST_OFFERS"]),
        )
        for b in chunk:
            books[b.market_id] = b
    return catalogue, books


def market_line(market_name):
    """'Over/Under 2.5 Goals' -> 2.5 (None if not one of our lines)."""
    import re

    found = re.search(r"(\d)\.5", market_name or "")
    line = float(found.group(0)) if found else None
    return line if line in MARKETS.values() else None


def best_back(runner_book):
    offers = runner_book.ex.available_to_back
    return (offers[0].price, offers[0].size) if offers else (None, None)


# ---------------- main scan ----------------
def scan(cfg, hours):
    rules = cfg["rules"]
    shrink = float(rules.get("shrink", 0.75))
    home_adv = float(rules.get("home_advantage", 1.10))
    min_price = float(rules.get("min_price", 1.65))
    value_line = float(rules.get("value_threshold", 1.15))
    gap_warning = float(rules.get("gap_warning_points", 15))
    # How much to trust the market's price vs our model when judging value. Our simple model
    # overshoots on extreme matchups (Monza v Fiorentina: model 68%, market 39%, actual xG ~44%),
    # so value is judged on a blend that leans toward the market.
    market_weight = float(rules.get("market_weight", 0.7))
    commission = float(rules.get("commission", 0.05))
    teams = load_teams(os.path.join(HERE, cfg["files"].get("teams_csv", "teams.csv")))
    # Champions League games use each team's Champions League record (small samples,
    # so they are pulled harder toward the competition average).
    cl_path = os.path.join(HERE, cfg["files"].get("cl_teams_csv", "teams_cl.csv"))
    cl_teams = load_teams(cl_path) if os.path.exists(cl_path) else {}
    cl_shrink = float(rules.get("cl_shrink", 0.5))

    client = betfair_client(cfg)
    try:
        catalogue, books = fetch_markets(client, hours)
    except Exception as e:  # turn Betfair's long error dump into a clear message
        if "INVALID_APP_KEY" in str(e):
            sys.exit("Betfair says the app_key in config.ini is not valid.\n"
                     "Run:  python scan.py --setup-key   to fetch your delayed key automatically.")
        raise
    print(f"Fetched {len(catalogue)} over/under markets.\n")

    rows, skipped = [], set()
    for m in catalogue:
        event = m.event.name
        if " v " not in event:
            continue
        home_name, away_name = [s.strip() for s in event.split(" v ", 1)]
        competition = m.competition.name if m.competition else ""
        is_cl = "champions league" in competition.lower() and "women" not in competition.lower()
        table, game_shrink = (cl_teams, cl_shrink) if is_cl else (teams, shrink)
        hk, ak = find_team(home_name, table), find_team(away_name, table)
        if not hk or not ak:
            skipped.add(f"{event} (no data for {home_name if not hk else away_name})")
            continue
        h, a = table[hk], table[ak]
        if h["league"] != a["league"]:
            skipped.add(f"{event} (different leagues - rate manually)")
            continue
        hxg, axg = expected_goals((h["played"], h["gf"], h["ga"]), (a["played"], a["gf"], a["ga"]),
                                  h["league_avg"], game_shrink, home_adv)
        line = market_line(m.market_name)
        book = books.get(m.market_id)
        if line is None or book is None:
            continue
        names = {r.selection_id: r.runner_name for r in m.runners}
        for rb in book.runners:
            label = names.get(rb.selection_id, "")
            side = "Over" if label.startswith("Over") else "Under" if label.startswith("Under") else None
            if not side:
                continue
            price, size = best_back(rb)
            if not price:
                continue
            chance = line_chance(hxg + axg, line, side)
            market_chance = 1 / price
            payout = lambda p: 1 + (p - 1) * (1 - commission)  # after commission
            blended = lambda p: (1 - market_weight) * chance + market_weight / p
            value = blended(price) * payout(price)
            # lowest price at which the blended value reaches the value line
            needed = next((p / 100 for p in range(101, 5001) if blended(p / 100) * payout(p / 100) >= value_line), 50.0)
            needed = max(min_price, needed)
            gap = (chance - market_chance) * 100
            rows.append({
                "kickoff": m.market_start_time.strftime("%a %H:%M"),
                "match": event,
                "competition": m.competition.name if m.competition else "",
                "bet": f"{side} {line}",
                "price": price,
                "available": round(size or 0),
                "model_chance": chance,
                "market_chance": market_chance,
                "value": value,
                "back_at": needed,
                "pass": price >= min_price and value >= value_line,
                "warning": ("GAP " + f"{gap:+.0f}pts - half stake") if abs(gap) > gap_warning else "",
                "estimated": "yes" if (h["estimated"] or a["estimated"]) else "",
                "xg": f"{hxg:.2f}-{axg:.2f}",
            })
    report(rows, skipped, cfg)


def report(rows, skipped, cfg):
    rows.sort(key=lambda r: r["value"], reverse=True)
    passing = [r for r in rows if r["pass"]]
    print("=== BETS THAT PASS THE RULES (best first) ===")
    if not passing:
        print("None. No bet is the right bet today.")
    for r in passing:
        print(f"{r['kickoff']}  {r['match']:<34} {r['bet']:<10} @ {r['price']:<5} "
              f"(EUR {r['available']} avail)  model {r['model_chance']:.0%} vs market {r['market_chance']:.0%}  "
              f"value {r['value']:.2f}  {r['warning']} {'[estimated data]' if r['estimated'] else ''}")
    print("\nTop 10 near-misses (back at these prices or better):")
    for r in [r for r in rows if not r["pass"]][:10]:
        print(f"{r['kickoff']}  {r['match']:<34} {r['bet']:<10} now {r['price']:<5} -> back at {r['back_at']:.2f}")
    if skipped:
        print(f"\nNot rated ({len(skipped)}): " + "; ".join(sorted(skipped)[:15]) + (" ..." if len(skipped) > 15 else ""))
    out_dir = os.path.join(HERE, "output")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, f"scan_{dt.datetime.now():%Y%m%d_%H%M}.csv")
    if rows:
        with open(out, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        print(f"\nFull results saved to {out}")


def selftest():
    # Feyenoord v Excelsior, 21 Nov: the model gave about 4.8 expected goals and 70% for Over 3.5.
    hxg, axg = expected_goals((12, 36, 17), (12, 16, 29), 1.85, 0.75, 1.10)
    o35 = line_chance(hxg + axg, 3.5, "Over")
    assert 4.7 < hxg + axg < 4.85, hxg + axg
    assert 0.69 < o35 < 0.71, o35
    assert abs(line_chance(2.0, 2.5, "Over") + line_chance(2.0, 2.5, "Under") - 1) < 1e-9
    teams = load_teams(os.path.join(HERE, "teams.csv"))
    assert find_team("Feyenoord", teams) and find_team("feyenord", teams)
    print(f"Self-test passed: Feyenoord v Excelsior xG {hxg:.2f}-{axg:.2f}, Over 3.5 {o35:.0%}. "
          f"{len(teams)} teams loaded.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Read-only Betfair goals value scanner")
    ap.add_argument("--hours", type=int, default=24, help="look this many hours ahead (default 24)")
    ap.add_argument("--selftest", action="store_true", help="check the model maths without logging in")
    ap.add_argument("--setup-key", action="store_true", help="fetch your delayed app key and save it to config.ini")
    args = ap.parse_args()
    if args.selftest:
        selftest()
    elif args.setup_key:
        setup_app_key(load_config())
    else:
        scan(load_config(), args.hours)
