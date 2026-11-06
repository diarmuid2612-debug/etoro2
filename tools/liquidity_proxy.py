import csv, sys, datetime as dt, bisect
D=sys.argv[1]
def load(s):
    out=[]
    for r in list(csv.reader(open(f"{D}/{s}.csv")))[1:]:
        try: out.append((dt.date.fromisoformat(r[0]), float(r[1])))
        except: pass
    return out
def asof(series, d):
    ds=[x[0] for x in series]; i=bisect.bisect_right(ds,d)-1
    return series[i][1] if i>=0 else None
W=load("WALCL");T=load("WTREGEN");R=load("RRPONTSYD");B=load("TOTBKCR");G=load("GDP")
def proxy(d): return asof(W,d)/1000-asof(T,d)/1000-asof(R,d)+asof(B,d)
g=G[-1][1]/G[-5][1]-1
print(f"Nominal GDP YoY ({G[-1][0]} vs {G[-5][0]}): {g*100:.2f}%")
dates=[d for d,_ in W if d>=dt.date(2025,10,1)]
for d in dates[-14:]:
    p=proxy(d); p6=proxy(d-dt.timedelta(days=182)); p12=proxy(d-dt.timedelta(days=364))
    ann6=((p/p6)**2-1)*100
    print(f"{d} proxy {p:,.0f}bn  YoY {(p/p12-1)*100:5.2f}%  6m ann {ann6:5.2f}%  excess {ann6-g*100:+5.2f}pp")
