# Betfair goals scanner (read-only)

Pulls Betfair Exchange Over/Under 2.5 / 3.5 / 4.5 prices for the next 24 hours,
rates every line with our goals model, and prints the bets that pass the rules
(price ≥ 1.65, model chance × price ≥ 1.15 after commission). **It never places bets.**

## One-time setup on Windows (ThinkPad)

1. **Install Python**: download it from python.org (Windows installer). On the first
   installer screen, tick **"Add python.exe to PATH"**, then click Install.
2. **Get this folder onto the laptop**: download the repository from GitHub
   (Code → Download ZIP) and unzip it, then open the `betting\scanner` folder.
3. **Open PowerShell in that folder**: in File Explorer, click the address bar,
   type `powershell` and press Enter.
4. **Install the Betfair library**:
   ```
   pip install -r requirements.txt
   ```
5. **Create your settings file**: copy `config.example.ini` to `config.ini` and fill in
   your Betfair username and your **delayed** app key. Your password is not stored;
   the scanner asks for it each run. `config.ini` is never uploaded to GitHub.
   If you don't have the key (or the Betfair Demo Tool won't work), run
   `python scan.py --setup-key`: it logs in, fetches your delayed key and saves it for you.
6. **Check the model works** (no login needed):
   ```
   python scan.py --selftest
   ```

## Every day

```
python scan.py              # next 24 hours
python scan.py --hours 48   # next 48 hours
```

The output lists, best first:
- **Bets that pass the rules**, with price, money available, model chance vs market chance,
  and a **GAP warning** (use half stake) when the model and market disagree by more than 15 points.
- **Near-misses**, with the price to request.
- **Games not rated**, because a team is missing from `teams.csv` or the teams are in
  different leagues (e.g. Champions League). Rate those manually.

A full CSV of every line is saved in the `output` folder.

## Keeping the model's data current

`teams.csv` holds each team's games played, goals for and goals against. The model is only
as good as this file, so update it weekly (or ask Claude to). Team names must match
Betfair's spelling (e.g. `Man City`, `Paris St-G`, `Dundee Utd`); close spellings are matched
automatically. Mark a row `estimated = yes` when a number is a guess.

## Settings (`config.ini`, `[rules]`)

| Setting | Default | Meaning |
|---|---|---|
| min_price | 1.65 | Never bet below this price |
| value_threshold | 1.15 | Model chance × price (after commission) must reach this |
| commission | 0.05 | Betfair commission on winnings |
| gap_warning_points | 15 | Flag half stake when model and market differ by more than this |
| shrink | 0.75 | How much to trust each team's own numbers vs the league average (lower = more cautious) |
| home_advantage | 1.10 | Home team boost |

## Troubleshooting

- **Login fails with "CERT_AUTH_REQUIRED" or similar**: Betfair wants certificate login.
  Follow Betfair's "Non-Interactive (bot) login" guide, put the two certificate files in a
  folder, and set `certs_folder` in `config.ini`.
- **Prices look a few seconds old**: normal with the free delayed key.
