# Trading rules

These rules apply to every trade proposed or placed from this repo, on real or demo
accounts. Read them before suggesting any trade or changing any stop-loss.

Longer-term ideas to watch are in `FUTURE_SETUPS.md`. Check their triggers during scans.

## 1. The chart sets the stop

- Before any trade, read the daily chart and find the relevant structure:
  support (for buys) or resistance (for shorts), plus the most recent swing low
  (buys) or swing high (shorts).
- Place the stop-loss **beyond both**: below support and the last swing low for a
  buy; above resistance and the last swing high for a short.
- Never place a stop inside a support/resistance zone, at the edge of one, or at a
  flat percentage from the entry price.
- After a breakout, the old ceiling becomes support (and after a breakdown the old
  floor becomes resistance). Price often retests it, so the stop must sit beyond the
  retest zone, not in it.
- State the level and the chart reason for it before the trade is placed.

## 2. Risk is decided per trade

- Agree how much each trade may lose, judged on the quality of the setup.
- A clean breakout confirmed by a daily close, with volume behind it and a nearby
  structural stop, can justify more risk. A weaker setup or a distant stop gets less.

## 3. Size comes last

- Position size = risk amount ÷ distance from entry to the structural stop.
- If the stop is far away, the position gets smaller. The stop is never moved closer
  to make the numbers work.

## 4. Every proposal shows the full picture

Before any trade, show: entry price, stop-loss and its chart reason, target
(take-profit), loss if stopped, gain if the target is hit, leverage, and position
size. Nothing is placed or changed without the account holder's explicit yes.

## Long-term holdings are exempt

- These rules apply to trades. Positions the account holder has designated as
  long-term holdings are exempt from the stop-loss rules above.
- Current long-term holdings: SUI, HYPE, NEAR and BTC. (PUMP was sold in full on 20 Oct 2026 at
  about 0.004546, 73,851.55 units, about −$11.40, to fund an IO breakout buy; the IO MIT order
  at 0.172 was rejected by eToro (error 814, "Instrument internal only"; IO is not tradable
  for the account holder on eToro). The proceeds went into SUI the same day: position
  3610510605, 326.77 units at 1.015 ($332, market, no stop). The account holder plans to
  deposit and buy more SUI if it drops to 0.90. On 24 Oct 2026 the SUI 0.90 MIT (order
  1615827191) was cancelled at the account holder's request and the cash went into BTC:
  position 3614117322, 0.001788 BTC at 80,527 ($144, market, no stop), inside the
  80,300–81,000 weekly buy zone. Reason: SUI was ~55% of crypto holdings and BTC was
  missing (Coutts-style anchor). Plan for new deposits: more BTC (zone 2 74,900–76,500),
  keep a cash buffer, optional AAVE (see FUTURE_SETUPS.md). HNT no longer shows in the open
  positions as of 17 Oct 2026, most likely closed by its $0.435 stop. AR was stopped out at
  its $3.85 stop on 8 Oct 2026 for about −$17.60. ELIZAOS no longer shows in the open
  positions as of 11 Oct 2026; its price, about 0.00036, is below its 0.00049 stop, so
  the stop most likely closed it.)
- NEAR: bought 12 Oct 2026 by swapping the August HYPE position (closed at about 87.44,
  about +$14.69). Position 3602844662, 57.90 units at 5.872, $340, no leverage, no stop
  (account holder's choice). Bought after the first daily close above the 5.60 ceiling
  (5.639 on 11 Oct) and a 4H retest to 5.557 that held. The May HYPE position stays.
  Added 12 Oct 2026: position 3603032012, 24.27 units at 5.769, $140, no stop, funded by
  selling half of STRK (1,360 units at about 0.104, about +$60 profit). NEAR total about
  82.2 units, average about 5.84. This left free cash at about $2, below the $450 trading
  reserve; the account holder chose this knowingly.
- STRK and AKT were stopped out overnight 12–13 Oct 2026 in an altcoin correction: STRK
  rest at 0.086 (about +$35; with the half sold earlier, about +$95 in all) and AKT at
  0.685 (about −$25). The freed cash (about €563) sits in the eToro Cash account, not
  the Trading account, and must be moved over in the app before it can be used.
- 13 Oct 2026 long-term buys (account holder wants to concentrate on HYPE, SUI and NEAR,
  aiming for closer to equal weight; SUI is already the largest, so new money goes to
  HYPE and NEAR): NEAR position 3604439721, 47.88 units at 5.012 ($240, market). Pending
  MIT orders: NEAR $240 at 4.55 (order 1610742724) and HYPE $140 at 77.50 (order
  1609603578). No leverage, no stops.
- As of 17 Oct 2026 neither MIT order is pending. HYPE filled 15 Oct: position 3607164516,
  1.81 units at 77.48 ($140). A NEAR buy opened 14 Oct evening: position 3606333254,
  47.01 units at 4.799 ($225.62), not at the 4.55 order level (reason not confirmed).
  NEAR total about 177 units.
- 19 Oct 2026 SUI buys (account holder chose SUI; HYPE is also held elsewhere): position
  3609898382, 151.21 units at 0.991 ($150, market, at the 0.99–1.00 weekly support), plus
  pending MIT order 1616566534, $150 at 0.90 (top of the 0.85–0.90 weekly support). No
  leverage, no stops. Free cash about $152 until the MIT fills, then about $0.
- 20 Oct 2026: the SUI 0.90 MIT order was cancelled at the account holder's request to free
  margin for a small GER40 test trade (see TRADE_LOG.md). The GER40 order never filled and
  was cancelled; the SUI order was re-placed the same day: MIT order 1615827191, $145 at 0.90
  (slightly less than $150 to fit the free cash).
- 27 Oct 2026, to fund the $1,000 eToro trading pot (account holder: "half NEAR, half SUI";
  plus a €400 deposit that landed in the eToro Cash account and must be moved to Trading):
  closed SUI position 3610510605 in full (326.77 units bought at 1.015, sold ~0.926, ~−$29),
  NEAR position 3602844662 in full (57.90 units at 5.872, sold ~4.62, ~−$72) and 7.3 units of
  NEAR 3603032012 (bought 5.769, ~−$8.5). Freed ~$596; Trading cash $595.85 afterwards.
  Remaining NEAR ~111.9 units (5.012, 5.769 rest 16.97, 4.799 lots); SUI ~1,583 units.
- NEAR's breakout failed: the 12 Oct daily close was 5.363, back below the 5.60 ceiling,
  and it dipped to 4.886 overnight. It is back inside the 4.30–5.60 range.
- HNT was bought with a structural stop ($0.435). Keep it as set unless the account
  holder asks to change it.
- ELIZAOS: on 8 Oct 2026 the two positions added on 6 Oct were closed for about +$127
  profit (more than the full ~$300 put into ELIZAOS came back). One position remains:
  205,021 units, entry 0.000478, $98 invested, stop 0.00049 (set 7 Oct at the account
  holder's request; structural, below the 7 Oct retest low of 0.00051 and the
  0.00055–0.00057 breakout zone). It is now a free ride on profit. Raise the stop only
  under new higher lows, and only when the account holder asks. The founder
  declared the token "dead" in August 2026 (foundation wound down, treasury spent, no
  buybacks, no link to the Eliza software), so a strong chart alone is not a reason to
  add. Adding more needs news of a revival (official statement, relaunch, major
  listing) plus the chart signals: a higher base at 0.00030–0.00035, or a daily close
  above 0.00057 followed by a retest that holds.
- Do not add, move or remove stops on long-term holdings, and do not keep suggesting
  them. Leave any existing stops on them as they are unless asked.
- Later in the cycle, when asked, set wide stops below major support on the weekly
  chart to protect profits.

## Entry: wait for the retest

- Do not chase breakouts. After a confirmed breakout (or breakdown), wait for price to
  come back to the level it broke: the old ceiling for a buy, the old floor for a
  short.
- Enter only when that level holds: price touches the retest zone and is rejected
  from it (bounces off support for a buy, turns down from resistance for a short).
  Prefer a daily close that confirms the rejection.
- The stop then goes just beyond the retest zone and the latest swing point, which
  is much closer than a stop placed after a chased breakout.
- If a breakout never comes back to retest, skip it and move on. Missing a trade is
  acceptable; a poor entry is not.
- Use price alerts on retest zones so the moment is not missed.

## Breakout checklist

- Breakout confirmed by a **daily close** beyond the level, not just an intraday move.
- Prefer entries on the breakout day rather than days later.
- Check volume where data is available (a breakout on well above normal volume is
  stronger).
- Avoid setups that have already run far (e.g. +50% or more in a few days) and
  one-day spikes.
- Avoid entering just before scheduled events that cause gaps (earnings, central bank
  decisions, major data releases).
- Leveraged trades: aim for at least 2:1 reward to risk, using the structural stop.

## Checking the news behind a move

When a holding or a candidate moves sharply, find the reason before judging it:

- Search the founder and team names, partners and related projects for the last few
  days, not only the ticker or token name. Catalysts often never mention the ticker.
- Ask what changed this week, even after finding a big older story. An old story
  (e.g. a token declared dead) does not explain a new move.
- Check the "why is the price up/down" explanations on CoinMarketCap and CoinGecko.
- Say plainly when the search was limited (only snippets read, sites blocked, X not
  checked) instead of saying there is no news.

## Current focus (from 13 Oct 2026): long-term accumulation, trading paused

- On 13 Oct 2026 the account holder decided to leave trading alone for now (no new
  intraday or swing trades) and concentrate on buying good crypto at good levels for the
  next cycle. Do not propose trades or set up trade-monitoring checks unless asked.
- Long-term buys: buy at strong support (weekly/daily structure), not after big runs;
  staged entries are fine. Show price, level and chart reason, amount, and the effect on
  free cash before any buy; nothing is placed without an explicit yes.
- Existing trades with stops are left to run on their stops unless the account holder
  decides otherwise. By 17 Oct 2026 ORCA and the ZRO position from 2.109 no longer show
  (most likely stopped at 1.98 and 1.87). One ZRO position remains: 3592632251, 31.97
  units at 1.783, stop 1.40.
- The rules below for the intraday model stay on file for when trading resumes.

## Daily Coinbase crypto trade (from 26 Oct 2026; PAUSED from 27 Oct 2026)

- 27 Oct 2026: the account holder paused crypto trading (no new Coinbase picks, no crypto in the
  eToro pot). The open Coinbase TIA trade is still tracked in the morning report until it exits
  (stop 0.49, targets 0.69/0.79). The rules below stay on file for when it resumes.
- 27 Oct 2026 evening: the account holder converted all the TIA (3,082.49) to SUI on Coinbase,
  roughly break-even. That Coinbase SUI (~$1,600) is a mid to long-term holding, on top of
  the eToro SUI; together SUI is the largest crypto exposure by far.

- One "trade of the day": the account holder converts from one coin to another on
  Coinbase by hand. Claude has no Coinbase access; it scans, plans and reports only.
- Morning scan around 07:00 Irish (daily crypto candle closes at 00:00 UTC), run by
  `tools/coinbase_scan.sh <data dir in scratchpad>`: every online Coinbase USD pair
  (~400) from api.exchange.coinbase.com daily candles, `tools/cb_breakout_scan.py` for
  breakout -> retest -> confirmation, with stop, R:R and 30-day average USD volume.
  Favour coins with real volume (roughly $1m+/day); flag thin ones.
- Only a CONFIRMED setup qualifies: a daily close above a clear ceiling, a pullback that
  retested it and held, then a daily close bouncing back above it (not more than ~25%
  above the ceiling, not a coin that already ran 50%+). Otherwise report "no trade today";
  never lower the bar. Check the news behind the move (rules above) before proposing.
- Each pick shows: entry zone, structural stop (below the retest zone and the latest
  swing low) with its reason, target, reward to risk (at least 2:1), stop distance in %
  and loss per $100 converted. The account holder decides the size each morning and
  converts from a coin (not cash), so note how the source coin is doing too.
- **Risk per trade: $120** (set 27 Oct 2026 by the account holder; the TIA trade of 27 Oct,
  ~$1,500 position with a ~8% stop, is the reference). Size every trade from its stop:
  amount to convert = $120 ÷ stop distance (e.g. 8% stop → $1,500; 12% → $1,000; 6% → $2,000),
  including fees. Keep it fixed after wins and after losses; review after 20 trades and
  only raise it if the results are positive and the account holder says yes. Each morning
  report the exact amount to convert for $120 risk.
- A plain Coinbase Convert has no stop; use Coinbase Advanced for a stop order or sell
  by hand if the stop closes. Convert fees are higher than Advanced trading.
- Log every pick and result in TRADE_LOG.md (Coinbase section).

## Daily eToro trade (from 28 Oct 2026)

- Pot: **$1,000** freed in the eToro Trading account for trading (the account holder frees it;
  long-term holdings stay). Keep it fixed: withdraw profits above $1,000 monthly, never top
  up after losses; if the pot falls to **$750**, stop and review the method.
- **One trade idea every morning, ready by 07:15 Irish** (scan starts 07:02), aiming for
  **2–4 trades a week**. Markets (27 Oct 2026, account holder): NSDQ100 (28), SPX500 (27),
  GER40 (32), GOLD (18) and oil; **no crypto trading for now**. Setups on the 4H/daily charts,
  typically resolving in 1–4 days. While a trade is open, the report gives its status instead.
- Setups: breakout -> retest -> confirmation, or sweep and reversal, on the daily/4H charts.
  Structural stop (rules 1 and Entry above). **Minimum 4:1 reward to risk** (account
  holder's choice). No setup that meets the bar = "no trade today"; never lower the bar.
- **Risk per trade: $30** (3% of the pot; default proposed 27 Oct, change only on the
  account holder's say). Size = $30 ÷ stop distance; leverage only as needed for the
  margin to fit the pot (indices/gold up to 20x).
- The account holder is at work after 07:15 and cannot watch the trade, so every order goes
  in at once with **stop-loss and take-profit attached**: a market order if price is at the
  entry, or an MIT entry order at the retest level. Swing holds over days are fine (note
  overnight fees). Check the day's US/EU data calendar; skip or adjust if a high-impact
  release could trigger the entry in a spike.
- The 07:15 proposal shows the full picture (rule 4) and a ready eToro preview; it is placed
  only after the account holder's explicit yes. If the yes also approves it, an unfilled MIT
  entry is cancelled at 21:00 Irish the same day (Claude schedules that check).
- Only one open trade from this pot at a time unless the account holder agrees otherwise.
  Log every idea and result in TRADE_LOG.md (eToro daily section).

## Crypto switch rule for the pot: BTC 10x on half the pot (updated 31 Oct 2026, account holder's yes)

- Trigger (BOTH needed): excess liquidity crosses **above zero** in LIQUIDITY_LOG.md (weekly
  tracker, FRED proxy) **and** BTC closes a **week** (Sunday 00:00 UTC candle) above **80,300**.
  The account holder always meant to wait for liquidity; no entry on the BTC break alone.
- When both fire: **half the pot (~$519 margin) goes into BTC at 10x** = ~$5,190 exposure (same
  exposure as the earlier 5x/full-pot plan); the **other half (~$519) stays in cash** untouched
  as a reserve (worst case in a crash is capped at the $519 margin). eToro offers up to 20x on
  crypto in the app; never use 20x here (its forced close would sit above our stop). Entry on
  the **retest that holds, ~80,000–80,500**, via an MIT order with the stop attached, not on
  the breakout candle. Stop **75,800** (below the 76,141 weekly swing low), attached from the
  first second, never moved lower: ~−$285 + fees if stopped (more with slippage in a crash).
- Guardrails: **one attempt only**; if stopped out, no second 5x attempt: stop and review with
  what is left. Move the stop to break-even only after BTC reaches ~90,000 AND a new weekly
  higher low has formed. Take **one third off at ~100,000**; trail the rest under each new weekly
  higher low. Nightly CFD fees apply; report them monthly.
- Until the trigger fires the daily/day/position trades continue as below. When it fires, no new
  pot trades; any open pot trade runs to its stop/target first (or is closed on the account
  holder's yes) so the full pot is free.
- The weekly liquidity check (Fridays) and the Monday crypto weekly-close check report the
  status of both halves. Full eToro preview and the three-step checklist before placing;
  nothing is placed without the account holder's explicit yes.

## Position trades (from 30 Oct 2026, account holder's yes)

- Weekly-chart breakouts held for weeks to months (watchlist in FUTURE_SETUPS.md: MS, BX, GEV,
  ETSY, STAA, DFDV, plus others found later). **One position trade may run alongside** the
  swing/day trade from the same pot.
- Entry: a **weekly close** above the level (or a weekly reversal at support), then the retest
  that holds. Structural stop below the retest zone and the weekly swing low.
- Risk **$30** per position trade normally; **up to $75 for an A-grade setup** (weekly close
  confirms the breakout AND the retest holds, clear structural stop, no earnings within 2 weeks)
  — account holder's yes, 31 Oct 2026. Same pot. Size = risk ÷ stop distance; never leveraged
  for A-grade sizing. State the grade (normal / A) and why in the proposal. With 10–20% stops
  that is about $150–300 of stock, so **no leverage by default**: leverage does not raise the
  profit when size comes from the stop; it only adds overnight fees (charged daily on
  leveraged CFDs) and liquidation risk. Use leverage only if margin would not otherwise fit.
- Let it run: no fixed target by default; trail the stop under each new weekly higher low
  (only when a new weekly swing has formed). Take part profit at 3R if the account holder wants.
- Earnings gaps can jump a stop: note the next earnings date in the proposal; the account
  holder decides whether to hold through it.
- The three-step pre-trade checklist applies. Stocks carry a transaction fee on eToro; include it.

## Afternoon day trade (from 30 Oct 2026)

- The account holder finishes work at 16:00 Irish and can watch the US session after that. A scan
  runs every weekday at about 15:50 so an idea is ready by 16:00.
- Markets: Mag 7 stocks (AAPL 1001, MSFT 1004, NVDA 1137, GOOGL 6434, AMZN 1005, META 1003,
  TSLA 1111; stocks up to 5x) and NSDQ100 (28), SPX500 (27), DJ30 (29) (indices up to 20x).
  Nasdaq, S&P 500 and Dow move together: one of them at a time.
- Setups from the intraday model: A. sweep and reversal, B. breakout and retest, on 15-minute and
  1-hour charts, in the 4H trend direction. Levels: the US session high and low so far, the
  previous day's high and low, and the pre-market range. Structural stop beyond the retest zone
  and the latest swing.
- **Minimum 3:1 reward to risk** (4:1 stays for the morning swing trade). **Risk $30** per trade,
  from the same $1,000 pot. Size = $30 ÷ stop distance.
- Same-day only: close by 15 minutes before the US cash close (19:45 Irish until 1 Nov 2026,
  20:45 Irish from 2 Nov). Stop-loss and take-profit attached; no overnight holds.
- Skip a stock on its earnings day (and the day after if it gapped wildly), and avoid entries from
  30 minutes before to 30 minutes after high-impact US data.
- **One open pot trade at a time** (swing or day trade). If one is open, the 16:00 scan only
  reports its status.
- Stocks show "requires W-8BEN" on eToro: the form must be signed in the app before the first
  stock trade.
- Placed only after the account holder's explicit yes. Log in TRADE_LOG.md (eToro daily section,
  marked "PM").

## Pre-trade checklist (from 30 Oct 2026, account holder: "no mistakes")

Every pot trade (morning or afternoon) passes three checks before it is shown, and the
results are shown with the proposal. Any failure = no proposal (or fix the plan and re-check).

1. **Chart check (fresh data):** re-read the candles right before proposing, not from an
   earlier scan. Confirm: the instrument id and symbol; the trend direction; the level and the
   confirming candle has CLOSED (not still forming); the retest/reclaim actually happened. List
   every level between entry and target (session high/low, previous day high/low, swing
   points, ceilings) — the target must sit before the first one that blocks it. Check the
   earnings and data calendar again.
2. **Numbers check (`tools/trade_check.py`):** run
   `python3 -I tools/trade_check.py --dir buy|sell --entry E --stop S --target T --min-rr R
   --levels L1,L2 --leverage X --cash C --spread SP` and paste the output. It checks the stop
   and target sides, reward to risk including the spread, levels in the way, size for $30
   risk, margin against cash.
3. **Preview check:** after prepare-trade, compare the preview field by field with the plan
   (instrument, buy/sell, order type and trigger, units or amount, leverage, stop-loss,
   take-profit) and re-run trade_check.py with `--units` and `--quote` from the preview. If
   the live price has moved more than a quarter of the stop distance from the planned entry,
   re-plan instead of placing.
- **After placing:** read get-my-positions-and-orders and confirm the position or order exists
  with the exact stop-loss and take-profit; report the position or order id. If anything
  differs, fix it at once (or close) and tell the account holder.

## Intraday model (real-money learning phase, paused from 13 Oct 2026)

Short-term trading on major indices and gold (see Markets below), held for hours and closed the same
day. It follows the rules above (structural stop, retest entry, size from the stop, full
proposal and an explicit yes) with these additions. From 9 Oct 2026 the account holder
chose to run it on the **real account** with small stakes, funded by the ~$127 ELIZAOS
profit taken on 8 Oct plus about $123 of the account holder's own money. **Intraday
budget: if the net intraday result reaches −$250, stop and review before any further
intraday trade.** The weekly and daily limits below still apply.

**Trading reserve:** suspended on 13 Oct 2026 while trading is paused; the account holder
chose to use the free cash for long-term buys. Reinstate it if trading resumes. Original
rule: keep at least $450 of free cash in the main account reserved for
trading (set 8 Oct 2026). Long-term buys come only from new deposits or profits, never
from the reserve. Before any long-term buy, check that free cash stays at or above $450
afterwards; if not, say so before proposing it. Later (from a laptop) move this pot to a
separate eToro "Regular" sub-account; positions cannot be moved, only cash.

**Markets (from 9 Oct 2026):** Nasdaq 100 (NSDQ100, id 28), S&P 500 (SPX500, id 27),
DAX (GER40, id 32) and Gold (GOLD, id 18). Each gets its own bias and levels. Nasdaq and
S&P 500 move together, so treat them as one bet: never hold both at once. Only one
intraday trade open at a time; the daily, weekly and budget limits are shared across all
markets. DAX suits the London session (Frankfurt opens 08:00 Irish). Gold reacts sharply
to US data and Fed news, so respect the news blackout strictly. Pick the cleanest setup;
do not lower the bar to find a trade.

**Bias first:** before each session, read the daily and 4-hour charts. Trade only in the
4-hour trend direction (higher highs and lows: buys only; lower highs and lows: sells
only). No clear trend means no trade that day.

**Mark levels before the session:** previous day's high and low, Asian session high and
low (00:00–07:00 Irish time), previous week's high and low.

**Two setups only:**
- **A. Sweep and reversal:** price trades beyond a marked level, then a 15-minute candle
  closes back inside it, then price breaks the last 15-minute swing the other way. Enter
  on the retest of that broken swing. Stop beyond the tip of the sweep. Target the other
  side of the range or the next marked level.
- **B. Breakout and retest:** a 1-hour close beyond a marked level in the bias direction.
  Enter when the retest holds. Stop beyond the retest zone and the latest swing.

**When:** any time the market is open (from 9 Oct 2026 the account holder dropped the fixed
London/New York windows after the best moves came outside them; the London open 08:00 and
the US open 14:30 Irish are still the busiest times to watch). No new trades from
30 minutes before to 30 minutes after high-impact US news (CPI, jobs report, Fed
decisions, weekly jobless claims). Close every intraday position by 21:00 Irish time; never
hold overnight. Note the session time in the log so the review can compare times of day.

**Risk limits:**
- Maximum $40 risk per trade (raised from $20 on 8 Oct 2026 at the account holder's
  request; target win rate 40% or better at 2:1).
- Maximum 2 trades a day. Stop for the day after 2 losses or −$80.
- Stop for the week at −$200.
- At least 2:1 reward to risk, from the structural stop.
- Size = $40 ÷ stop distance. Margin (exposure ÷ leverage, up to 20x) must fit in
  available cash; if it does not, risk less rather than move the stop closer.

**Managing the trade:** move the stop to entry only after a new structural swing forms
beyond it, never at a fixed profit. Optionally take half at 1.5R and leave the rest to
the target. (R = the amount risked.)

**Proving it:** log every trade in `TRADE_LOG.md` (date, session, setup, bias,
entry, stop, target, result in R, notes). After at least 20 trades or 4 weeks, review.
Keep the $40 risk until the average result is positive (at 2:1, a win rate of about
40% or more). Raise risk per trade only after that review and with the account holder's yes.

**After the review:** run the proven model in an eToro Agent Portfolio (its own
portfolio and access key, copied by the real account). Set it up from a laptop so the
key and connector settings can be handled safely. Never store the key in this repo.
