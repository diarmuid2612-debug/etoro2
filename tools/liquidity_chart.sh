#!/usr/bin/env bash
# Morning global-liquidity chart. Usage: tools/liquidity_chart.sh <out dir>
# Downloads FRED series into <out dir>/data and writes <out dir>/liquidity_<date>.png
set -euo pipefail
OUT=${1:?out dir}
DATA="$OUT/data"; mkdir -p "$DATA"
START=$(date -u -d '3 years ago' +%Y-%m-%d)
for s in WALCL WTREGEN RRPONTSYD TOTBKCR GDP T10Y2Y BAMLH0A0HYM2 DTWEXBGS CBBTCUSD; do
  for i in 1 2 3; do
    if curl -sf --max-time 60 "https://fred.stlouisfed.org/graph/fredgraph.csv?id=$s&cosd=$START" -o "$DATA/$s.csv"; then break; fi
    sleep 5
  done
done
if [ ! -d /root/pylib/matplotlib ]; then
  python3 -m pip install -q --target /root/pylib matplotlib >/dev/null 2>&1
fi
HERE=$(cd "$(dirname "$0")" && pwd)
PYTHONPATH=/root/pylib python3 "$HERE/liquidity_chart.py" "$DATA" "$OUT/liquidity_$(date -u +%Y-%m-%d).png"
