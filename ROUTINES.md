# Fresh-session routines (demo trial)

Create these in the Claude app under **Routines** (claude.ai), so each run starts its own
session. For each routine:

- **Repository:** `diarmuid2612-debug/etoro2`, branch `ccr-d905f096-58iyk5`
- **Environment:** Doc22
- **Connector:** eToro (must be ticked, or the run cannot trade)
- **Notifications:** push on

Times are Irish (Europe/Dublin), weekdays only.

---

## 1. Demo scan — 07:10, 13:50 and 16:05

Prompt:

```
Demo trial scan. Follow CLAUDE.md section "Demo trial" (incl. "Waiting MIT orders at levels" and
"Close-out safeguards"). DEMO ACCOUNT ONLY: pass account "demo" to every eToro call; never touch the
real account.
1) git pull. Read TRADE_LOG.md "Demo trial" to see today's demo trades and waiting orders.
2) get-my-positions-and-orders (demo). Report any open demo trade vs its stop/target. Re-check every
   waiting demo MIT: cancel it if its setup is gone (DELETE /api/v3/trading/execution/demo/orders/{id}).
3) Read eToro candles (daily, 4H, 1H, 15m) for NSDQ100 28, SPX500 27, DJ30 29, GER40 32, GOLD 18,
   OIL 17. Check the US/EU data calendar: no entry from 30 min before to 30 min after high-impact data.
4) If no demo trade is open and none has filled today:
   - a setup meeting the full bar (3:1, or 2.5:1 A-grade) -> place it ("meets bar");
   - otherwise a setup with a structural stop and at least 2:1 after the spread -> place it as an MIT
     at the level, or market if price is there ("below bar"); max 2 waiting MITs, not two on
     Nasdaq/S&P/Dow; when one fills cancel the others.
   - At the 16:05 run, if nothing has filled today, you MUST place one (market, or an MIT likely to
     fill before 19:30). No entry after 19:30.
   Size: $30 risk, size = $30 / (stop distance + spread), margin within a $1,000 pot
   (python3 -I tools/trade_check.py ... --cash 1000), up to 20x indices/gold.
5) BEFORE placing: the prepare-trade quote's asOf must be within 2 minutes of now and match the latest
   candle; if stale, do NOT place (say so). Call place-trade immediately after prepare-trade.
6) Confirm via get-my-positions-and-orders (exact SL/TP), log every action in TRADE_LOG.md
   "Demo trial", commit and push to ccr-d905f096-58iyk5. Finish with a 3-line summary.
```

## 2. Demo close-out — 20:25 and 20:50

Prompt:

```
Demo trial close-out. DEMO ACCOUNT ONLY (account "demo"); never touch the real account.
CLOSE FIRST, before anything else:
1) get-my-positions-and-orders (demo). For every open demo day trade (anything not marked as a
   morning swing trade in TRADE_LOG.md "Demo trial"): prepare-close and IMMEDIATELY place-close with
   no call in between; if the token expired, prepare a fresh one and place at once; repeat until
   confirmed closed.
2) Cancel every unfilled demo MIT (DELETE /api/v3/trading/execution/demo/orders/{id}).
3) git pull; for each demo trade closed today, read get-my-trading-history (demo) and fill in
   Result (R) and Result ($) in TRADE_LOG.md "Demo trial". Count closed demo trades; at 10, write the
   review (win rate, average R, total $, meets bar vs below bar, what stopped out and why; note trade
   #1 lost through a missed close-out) and put it at the top of the summary.
4) Commit, push. At the 20:50 run, if nothing was open and nothing changed, end with "nothing to do".
```

---

Once these exist, the 07:15 / 13:45 / 16:00 scans in the main conversation keep only the
real-account proposals, and the old in-conversation demo close-outs (20:25, 20:50) are switched off.
