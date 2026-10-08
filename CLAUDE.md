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
- Current long-term holdings: SUI, HYPE, PUMP, AR, HNT and ELIZAOS.
- AR and HNT were bought with structural stops (AR $3.85, HNT $0.435). Keep them as
  set unless the account holder asks to change them.
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

## Intraday model (demo phase)

Short-term trading on the Nasdaq 100 (eToro NSDQ100), held for hours and closed the same
day. It follows the rules above (structural stop, retest entry, size from the stop, full
proposal and an explicit yes) with these additions. **Demo account only** until the
proving rules at the end are met and the account holder agrees to go live.

**Market:** Nasdaq 100 only.

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

**When:** London (08:00–11:00) or New York (14:30–17:00), Irish time. No new trades from
30 minutes before to 30 minutes after high-impact US news (CPI, jobs report, Fed
decisions, weekly jobless claims). Close every intraday position by 21:00 Irish time; never
hold overnight.

**Risk limits:**
- Maximum $20 risk per trade.
- Maximum 2 trades a day. Stop for the day after 2 losses or −$40.
- Stop for the week at −$100.
- At least 2:1 reward to risk, from the structural stop.
- Size = $20 ÷ stop distance. eToro's minimum position is $1,000, so at about 31,000 the
  stop can be up to about 600 points away. Leverage up to 20x.

**Managing the trade:** move the stop to entry only after a new structural swing forms
beyond it, never at a fixed profit. Optionally take half at 1.5R and leave the rest to
the target. (R = the amount risked.)

**Proving it:** log every demo trade in `TRADE_LOG.md` (date, session, setup, bias,
entry, stop, target, result in R, notes). After at least 20 trades or 4 weeks, review.
Go live only if the average result is positive (at 2:1, a win rate of about 40% or more)
and the account holder says yes. Real trades then follow the same limits.

**After the demo phase:** run the proven model in an eToro Agent Portfolio (its own
portfolio and access key, copied by the real account). Set it up from a laptop so the
key and connector settings can be handled safely. Never store the key in this repo.
