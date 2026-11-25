# Goals model backtest

Tests the scanner's goals model on past seasons from football-data.co.uk
(results plus Betfair exchange and Pinnacle over/under 2.5 prices).

```
# download (8 leagues x 5 seasons) into a data folder, then:
python backtest.py <data_folder>
```

Data URL pattern: `https://football-data.co.uk/mmz4281/<season>/<league>.csv`
(seasons 2122..2526; leagues E0 E1 D1 I1 SP1 F1 N1 SC0).

## Result (run 25 Nov 2026, 14,338 matches)

- **Test A (betting O/U 2.5 at Betfair prices, 5% commission):** every setting lost money
  (-6% to -28% ROI). The model's bets were expected to win 53-62% of the time but won 38-43%.
- **Test B (accuracy for 4+ / 5+ goals):** the closing market is better calibrated than the model
  (log-loss 0.587 vs 0.607 for 4+, 0.399 vs 0.414 for 5+). The model overshoots at the top end:
  when it says 60-70% for 4+ goals, it happens 48%; when it says 40-50% for 5+ goals, it happens 25%.
  Blending with the market does not beat the market alone.

## v2 model (backtest_v2.py, run 25 Nov 2026)

Time-weighted attack/defence ratings fitted to the last ~500 days of results per league
(last season carried over, home advantage per league), refitted before every matchday.

- **Test A:** still loses in every setting; best was -2.1% ROI over 697 bets (model only,
  value >= 1.15). Expected win rate 60%, actual 48%.
- **Test B:** still less accurate than the closing market for 3+, 4+ and 5+ goals
  (log-loss 0.691 vs 0.671, 0.608 vs 0.589, 0.414 vs 0.400); blending does not beat the market.

Conclusion: results-based goals models do not beat Betfair/Pinnacle over/under prices in these leagues.
