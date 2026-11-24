"""Global liquidity morning chart (same proxy as liquidity_proxy.py).

proxy  = Fed assets (WALCL) - TGA (WTREGEN) - reverse repo (RRPONTSYD) + bank credit (TOTBKCR), $bn
excess = 6-month annualised growth of the proxy - nominal GDP YoY (pp)
Usage: python3 liquidity_chart.py <data dir with FRED csvs> <out.png>
"""
import bisect, csv, datetime as dt, sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

D, OUT = sys.argv[1], sys.argv[2]


def load(s):
    out = []
    try:
        rows = list(csv.reader(open(f"{D}/{s}.csv")))[1:]
    except FileNotFoundError:
        return out
    for r in rows:
        try:
            out.append((dt.date.fromisoformat(r[0]), float(r[1])))
        except (ValueError, IndexError):
            pass
    return out


def asof(series, d):
    ds = [x[0] for x in series]
    i = bisect.bisect_right(ds, d) - 1
    return series[i][1] if i >= 0 else None


W, T, R, B, G = (load(s) for s in ("WALCL", "WTREGEN", "RRPONTSYD", "TOTBKCR", "GDP"))
CURVE, HY, USD, BTC = (load(s) for s in ("T10Y2Y", "BAMLH0A0HYM2", "DTWEXBGS", "CBBTCUSD"))


def proxy(d):
    v = [asof(W, d), asof(T, d), asof(R, d), asof(B, d)]
    if None in v:
        return None
    return v[0] / 1000 - v[1] / 1000 - v[2] + v[3]


def gdp_yoy(d):
    # latest nominal GDP YoY for every point, as in liquidity_proxy.py (keeps the log comparable)
    return (G[-1][1] / G[-5][1] - 1) * 100


start = dt.date.today() - dt.timedelta(days=730)
pd_, pv, ed, ev = [], [], [], []
for d, _ in W:
    if d < start:
        continue
    p, p6, p12 = proxy(d), proxy(d - dt.timedelta(days=182)), proxy(d - dt.timedelta(days=364))
    if None in (p, p6):
        continue
    pd_.append(d); pv.append(p)
    ann6 = ((p / p6) ** 2 - 1) * 100
    ed.append(d); ev.append(ann6 - gdp_yoy(d))


def since(s):
    return [x for x in s if x[0] >= start]


fig, ax = plt.subplots(4, 1, figsize=(10, 12), sharex=True)
fig.suptitle(f"Global liquidity check — {dt.date.today():%a %d %b %Y}", fontsize=14, weight="bold")

# 1 proxy + BTC
a = ax[0]
a.plot(pd_, pv, color="#1f6feb", lw=2, label="US liquidity proxy ($bn)")
a.set_ylabel("$bn")
b = a.twinx()
bt = since(BTC)
if bt:
    b.plot([x[0] for x in bt], [x[1] for x in bt], color="#f7931a", lw=1, alpha=0.8, label="BTC (Coinbase)")
    b.set_ylabel("BTC $")
a.set_title(f"Fed assets − TGA − RRP + bank credit: {pv[-1]:,.0f}bn ({pd_[-1]:%d %b})  |  BTC {bt[-1][1]:,.0f}" if bt else "Liquidity proxy")
h1, l1 = a.get_legend_handles_labels(); h2, l2 = b.get_legend_handles_labels()
a.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=8)

# 2 excess liquidity
a = ax[1]
a.plot(ed, ev, color="#8250df", lw=2)
a.axhline(0, color="k", lw=1)
a.fill_between(ed, ev, 0, where=[v >= 0 for v in ev], color="#2da44e", alpha=0.25)
a.fill_between(ed, ev, 0, where=[v < 0 for v in ev], color="#cf222e", alpha=0.25)
state = "ABUNDANT" if ev[-1] > 0 else "SCARCE"
a.set_title(f"Excess liquidity (6m ann. growth − nominal GDP): {ev[-1]:+.2f}pp → {state}  (turn = above 0)")
a.set_ylabel("pp")

# 3 curve + HY
a = ax[2]
c = since(CURVE)
if c:
    a.plot([x[0] for x in c], [x[1] * 100 for x in c], color="#0969da", lw=1.5, label="2s10s (bp)")
    a.axhline(45, color="#0969da", ls="--", lw=0.8)
a.set_ylabel("2s10s bp")
b = a.twinx()
h = since(HY)
if h:
    b.plot([x[0] for x in h], [x[1] for x in h], color="#cf222e", lw=1.5, label="HY spread (%)")
    b.axhline(4, color="#cf222e", ls=":", lw=0.8)
    b.axhline(3, color="#2da44e", ls=":", lw=0.8)
b.set_ylabel("HY %")
a.set_title(f"2s10s {c[-1][1]*100:.0f}bp (good > 45, steepening)  |  HY spread {h[-1][1]:.2f}% (good < 3, bad → 4)" if c and h else "Curve / credit")
h1, l1 = a.get_legend_handles_labels(); h2, l2 = b.get_legend_handles_labels()
a.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=8)

# 4 dollar
a = ax[3]
u = since(USD)
if u:
    a.plot([x[0] for x in u], [x[1] for x in u], color="#57606a", lw=1.5)
    a.set_title(f"Broad trade-weighted dollar (FRED DTWEXBGS, not DXY): {u[-1][1]:.2f} ({u[-1][0]:%d %b}) — falling = good")
a.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))

for x in ax:
    x.grid(alpha=0.3)
fig.text(0.01, 0.005, "Data: FRED (WALCL, WTREGEN, RRPONTSYD, TOTBKCR, GDP, T10Y2Y, BAMLH0A0HYM2, DTWEXBGS, CBBTCUSD). "
         "Proxy of GMI's measure, not the same series.", fontsize=7, color="#57606a")
fig.tight_layout(rect=(0, 0.01, 1, 0.97))
fig.savefig(OUT, dpi=110)
print(OUT)
print(f"proxy {pv[-1]:,.0f}bn ({pd_[-1]}) | excess {ev[-1]:+.2f}pp (prev week {ev[-2]:+.2f}) | "
      f"2s10s {c[-1][1]*100:.0f}bp | HY {h[-1][1]:.2f}% | USD broad {u[-1][1]:.2f} | BTC {bt[-1][1]:,.0f}")
