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

Data note: on 26 Oct 2026 FRED and federalreserve.gov were blocked by this environment's
network policy; until they are allowed, readings come from news/web search and are marked
as estimates.

## Log

| Week of | Excess liq. (ours) | GMI reading | DXY | 2s10s | HY spread | BTC ETF flows | Oil | Verdict |
|---|---|---|---|---|---|---|---|---|
| 19 Oct 2026 (baseline, Raoul) | – | broad −2.0 / narrow −4.5 | 101.8 | 35bp | 3.23% | −$230m | ~$97 | Scarce; hold, don't add |
