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
