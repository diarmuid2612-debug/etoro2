# Excess liquidity tracker

Weekly check (Fridays ~09:00 Irish) asked for on 26 Oct 2026, following Raoul Pal's
Macro Investing Tool (19 Oct 2026): "until the excess liquidity measure gets back above
zero, the curve steepens from the front end and the dollar heads back under 100, I don't
have the signal I want. So I hold what I have; I don't add."

## Method (an approximation of GMI's measure, not the same series)

- **Broad US liquidity proxy** = Fed total assets (FRED WALCL) − Treasury General Account
  (WTREGEN) − overnight reverse repo (RRPONTSYD) + commercial bank credit (TOTBKCR).
  GMI's narrow measure also adds bank-held securities.
- **Flow** = 6-month annualised % change of the proxy.
- **Excess liquidity** = flow − nominal GDP growth (latest year-on-year, FRED GDP).
  Above zero = "abundant" (money left over for risk assets); below zero = "scarce".
- GMI's published readings on 17–19 Oct 2026: broad −2.0, narrow −4.5 ("scarce" since
  August; nowcast staying there into October). Our proxy will not match exactly; watch its
  direction and the zero crossing, and record any newer GMI reading when shared.

## Confirming signals (Raoul's list)

| Signal | Bad | Good |
|---|---|---|
| Excess liquidity | below zero, falling | crosses above zero |
| Dollar (DXY, eToro USDOLLAR id 25) | above 102 | below 100 (200-day, channel break) |
| 2s10s yield curve | flattening, below 35bp | back above 45bp, steepening from the front end |
| High-yield spread | rising towards 4% | falling back below ~3% |
| Global liquidity YoY | heading to 0% | holding above 5% |
| BTC spot ETF flows | weekly outflows | sustained inflows |
| Oil (WTI) | above $100 | falling back (Iran deal) |

Data: FRED, federalreserve.gov and api.coingecko.com were allowed in the environment on
26 Oct 2026 (coinmarketcap.com and farside.co.uk still fail). Script: `tools/liquidity_proxy.py`
(download the FRED CSVs for WALCL, WTREGEN, RRPONTSYD, TOTBKCR, GDP into a folder, then run
`python3 -I tools/liquidity_proxy.py <folder>`). Units: WALCL/WTREGEN $m, RRP and bank
credit $bn. Bank credit lags the Fed data by about a week. Nominal GDP YoY is quarterly
(latest Q2 2026: 6.31%).

Proxy history (excess = 6m annualised flow − nominal GDP YoY): +0.43 (22 Jul), +0.20
(29 Jul), −0.15 (5 Aug, first below zero, matching GMI's "scarce since August"), −1.00
(12 Aug), −2.19 (2 Sep), −2.46 (23 Sep), −2.91 (30 Sep), −2.99 (7 Oct, low), −2.78 (14 Oct),
−1.19 (21 Oct). YoY growth of the proxy: 3.6% (Aug) → 5.2% (Oct), close to GMI's 4.9%.

## Log

| Week of | Excess liq. (ours) | GMI reading | DXY | 2s10s | HY spread | BTC ETF flows | Oil | Verdict |
|---|---|---|---|---|---|---|---|---|
| 19 Oct 2026 (baseline, Raoul) | – | broad −2.0 / narrow −4.5 | 101.8 | 35bp | 3.23% | −$230m | ~$97 | Scarce; hold, don't add |
| 21 Oct 2026 (FRED, first proxy) | −1.19pp (from −2.99 on 7 Oct) | – | 101.5 (26 Oct) | 31bp (23 Oct) | 3.40% (22 Oct) | not fetched | not fetched | Still scarce but improving; curve and HY spread worse; dollar just under 102 |
| 30 Oct 2026 (FRED, H.4.1 of 28 Oct) | −1.39pp (21 Oct revised to −0.75; low −2.55 on 7 Oct) | – | 101.4 | 37bp (29 Oct) | 3.14% (28 Oct) | not found this week | oil ~102 | Still below zero; credit healthy, curve slowly steepening, dollar soft. Binance $6.3bn hack 29–30 Oct hit crypto sentiment. Not the turn yet |
| 6 Nov 2026 (FRED, H.4.1 of 4 Nov) | **−2.11pp** (28 Oct −1.23, 21 Oct −0.59; low −2.63 on 7 Oct); bank credit only to 21 Oct | – | 101.6 (dipped to 100.86 on 4–5 Nov, closed back above the 101.10 floor) | 38bp (5 Nov) | 3.32% (4 Nov) | not fetched | ~95 | Worse again: the 6-month growth rate slowed. Post-election reversal 5 Nov (Nasdaq −4–5%, chips −11%, ~$560m crypto longs liquidated). BTC ~75,600. Not the turn |

### 29 Oct 2026 (post-Fed check)
- Fed 28 Oct: hold at 3.75–4.00%, 10–2 (Cook, Hammack for a hike); Warsh hinted at a December hike, no forward guidance.
- Q3 GDP advance 3.4% annualised (vs ~3.2% expected); September PCE 3.6% y/y, core 3.1% (in line). A December hike is still on the table.
- DXY 101.9 (between 100 and 102, no break). 2s10s 38bp (28 Oct, up from 29; still under 45). HY spread 3.18% (27 Oct, tighter than the 3.23% baseline). Oil 99.9, back under $100. BTC ETF flows for this week not found (latest seen: +$527m on 19 Oct; October roughly flat to negative).
- Verdict: no liquidity turn yet. Mixed: credit fine, curve steepening slowly, the dollar is flat and a hawkish Fed is a headwind.

### 3 Nov 2026 (interim check, account holder asked)
- No new Fed balance-sheet data since 28 Oct (next H.4.1 on Thu 5 Nov). Proxy for 28 Oct now
  **−1.23pp** (bank credit to 21 Oct revised in); 21 Oct −0.59, low −2.63 on 7 Oct. Still below zero.
- 2s10s 32bp (2 Nov, flatter than 37); HY spread **3.43%** (2 Nov, wider than 3.14 on 28 Oct:
  some risk-off after the chip sell-off and the Binance hack); DXY 101.35, testing the 101.10
  range floor. RRP ~0. Verdict: no turn; credit slightly worse, dollar softer.

## Raoul Pal "Macro Investing Tool" 2 Nov 2026: the turn checklist

Account holder shared the report on 9 Nov. Raoul: the weakness is liquidity, not AI (none of the
hyperscalers cut 2027 capex). "So I hold, and I don't add yet." Expected sequence: a base first,
then a rally as the ISM falls. Lead from financial conditions to liquidity is ~30 days now;
liquidity leads the Nasdaq/Bitcoin by ~a quarter.

His readings (2 Nov): real-time FCI (3m) low 53.4 on 14 Oct, 54.2 on 2 Nov (a higher low, just
turning; the 3-month change crosses zero ~January if conditions hold). Excess liquidity index
−0.5σ; October nowcast −2.4 broad, −5.5 narrow. US broad liquidity $25.76tn, +5.4% y/y but only
+0.6% over 3 months; narrow $11.53tn, −1.1% over 3 months. Global liquidity +6.6% y/y. S&P
speculators net short −6.9% of open interest (washed out). Since 2011, 7 conditions turns: Nasdaq
higher 6 months later in 5 (median ~+12%); the 2 failures (2011, 2018) re-tightened.

**Turn checklist (track weekly):**

| Signal | Needed | 2 Nov (Raoul) | 6–9 Nov (ours) |
|---|---|---|---|
| Dollar (DXY) | under 100 | 101.87 | 101.6 |
| 2-year minus fed funds | falling toward 0 (hikes priced out) | 4.59 − 3.88 = +71bp; Dec hike ~83% | 4.46 − 3.88 = **+58bp** (5 Nov) |
| 2s10s | steepening from the front end | 38bp | 38bp |
| Real-time FCI (3m) | keeps rising | 54.2, higher low | not available to us |
| Excess liquidity | turning up | −2.4 broad nowcast | −2.11 (our proxy, 4 Nov) |

**Where he is wrong (2018 path):** the Fed hikes in December (FOMC 9–10 Dec), the dollar breaks
back above 102, the 2-year pushes higher. Then conditions re-tighten and the base takes longer.

## Jamie Coutts "Alpha Crypto Pulse" 11 Nov 2026 (shared by the account holder)

- More cautious: margin-debt velocity confirmed a rollover in Sept (past confirmations: median
  S&P 500 fall 12% within a year, 21% within two). Took profit on a position +100%; holding more
  cash. Base case: the liquidity trough resolves late Q1 2027.
- BTC levels: market regime filter **72,049**, 10-month average 72,470, 300-day average 73,390
  (all within ~4% of price). Below **70,000** with a weekly Trend Chameleon reversal and the
  filter turning down = doubt the July low. Below **60,000** = likely capitulation low (liquidity
  response closer). Above **86,000** (Sept high) with the filter holding = bull cycle confirmed.
- Cost bases: short-term holders ~75,600, ETF buyers ~84,500, realized price ~54,000.
- Gauges: valuation fair and turning up, trend "uptrend, momentum lost" (one step from a
  downtrend), derivatives neutral; a derivatives washout would be the strongest buy signal.
- Warning light: USD stablecoin supply $293B, −6% in 30 days (fastest since Terra, May 2022).
- Liquidity-response checklist (his): MOVE, 10y yield, inflation expectations and stress index
  moving the right way; the dollar (101.7) and repo stress are the holdouts.
- Altcoins: only ~2.5% of the top 50 in a Trend Chameleon uptrend; he only holds alts when BTC is
  above the regime filter and the alt's own trend is up.

### 12 Nov 2026 (interim, account holder asked) — turn checklist 0–1 of 5
- Excess liquidity **−2.03pp** (4 Nov; next Fed H.4.1 tonight). DXY **102.84**, broke back above
  102 (Raoul's and Coutts' "where I'm wrong" signal). 2-year 4.56 vs fed funds 3.88 = **+68bp**
  (worse than +58). 2s10s **25bp** (flatter, worse). HY spread 3.30% (slightly better).
  BTC ~71,300, below Coutts' 72,049 regime filter. Verdict: re-tightening, the 2018-style risk.
