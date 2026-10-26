#!/usr/bin/env bash
# Morning breakout-retest scan for coins on Coinbase (data: CoinGecko free API).
# Usage: tools/coinbase_scan.sh <data_dir>   (data_dir outside the repo, e.g. the scratchpad)
set -u
D="${1:?data dir}"; mkdir -p "$D/mc"; cd "$D"
CG=https://api.coingecko.com/api/v3
curl -sS -m 30 -o markets.json "$CG/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1"
rm -f cb*.json
for p in 1 2 3 4 5 6; do curl -sS -m 30 -o cb$p.json "$CG/exchanges/gdax/tickers?page=$p"; sleep 4; done
python3 -I "$(dirname "$0")/coinbase_universe.py" "$D" > ids.txt
rm -f mc/*.json
end=$((SECONDS+900))
for id in $(cat ids.txt); do
  [ $SECONDS -gt $end ] && break
  for t in 1 2 3; do
    c=$(curl -sS -m 30 -o mc/$id.json -w "%{http_code}" "$CG/coins/$id/market_chart?vs_currency=usd&days=120&interval=daily")
    [ "$c" = 200 ] && break; rm -f mc/$id.json; sleep 20
  done
  sleep 4
done
echo "fetched $(ls mc | wc -l) of $(wc -w < ids.txt)"
python3 -I "$(dirname "$0")/breakout_scan.py" "$D/mc"
