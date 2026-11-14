#!/usr/bin/env bash
# Morning breakout-retest scan of every Coinbase USD pair, using Coinbase's public candles.
# Usage: tools/coinbase_scan.sh <data_dir>   (outside the repo, e.g. the scratchpad)
set -u
D="${1:?data dir}"; mkdir -p "$D/cbc"; rm -f "$D"/cbc/*.json
curl -sS -m 30 -o "$D/products.json" https://api.exchange.coinbase.com/products
python3 -I -c "
import json,sys
p=json.load(open(sys.argv[1]))
print('\n'.join(x['id'] for x in p if x['quote_currency']=='USD' and x['status']=='online' and not x.get('trading_disabled')))" "$D/products.json" > "$D/ids.txt"
xargs -P 4 -I{} sh -c 'curl -sS -m 20 -o "$0/cbc/{}.json" "https://api.exchange.coinbase.com/products/{}/candles?granularity=86400"; sleep 0.5' "$D" < "$D/ids.txt"
python3 -I "$(dirname "$0")/cb_breakout_scan.py" "$D/cbc"
