import json,glob,sys
D=sys.argv[1]
m=json.load(open(f"{D}/markets.json"))
cb=set()
for f in glob.glob(f"{D}/cb*.json"):
    try: cb.update(t["coin_id"] for t in json.load(open(f)).get("tickers",[]))
    except Exception: pass
skip={"usdt","usdc","dai","fdusd","usde","pyusd","tusd","usds","rlusd","usd1","eurc","usdg","susde","paxg","xaut","wbtc","weth","steth","wsteth","cbbtc","weeth","reth","lbtc","cbeth","jitosol","msol","tbtc"}
print(" ".join(c["id"] for c in m if c["id"] in cb and c["symbol"].lower() not in skip))
