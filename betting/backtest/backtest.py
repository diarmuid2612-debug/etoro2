import csv, glob, math, os, sys, datetime as dt
from collections import defaultdict
D=sys.argv[1]
def num(x):
    try: return float(x)
    except: return None
def pdate(s):
    for f in ("%d/%m/%Y","%d/%m/%y"):
        try: return dt.datetime.strptime(s,f)
        except: pass
matches=[]
for path in sorted(glob.glob(os.path.join(D,"*.csv"))):
    lg,season=os.path.basename(path)[:-4].split("_")
    with open(path,encoding="latin-1") as f:
        for r in csv.DictReader(f):
            if not r.get("HomeTeam") or r.get("FTHG") in (None,""): continue
            matches.append(dict(lg=lg,season=season,date=pdate(r["Date"]),h=r["HomeTeam"],a=r["AwayTeam"],
                hg=int(r["FTHG"]),ag=int(r["FTAG"]),
                bfo=num(r.get("BFE>2.5")),bfu=num(r.get("BFE<2.5")),bfco=num(r.get("BFEC>2.5")),bfcu=num(r.get("BFEC<2.5")),
                po=num(r.get("P>2.5")),pu=num(r.get("P<2.5")),pco=num(r.get("PC>2.5")),pcu=num(r.get("PC<2.5"))))
matches.sort(key=lambda m:(m["lg"],m["season"],m["date"] or dt.datetime(1900,1,1)))
P=lambda l,k:1-sum(math.exp(-l)*l**i/math.factorial(i) for i in range(k))
def implied_lam(p_over25):
    lo,hi=0.2,8
    for _ in range(50):
        mid=(lo+hi)/2
        if P(mid,3)<p_over25: lo=mid
        else: hi=mid
    return mid
def run(shrink,ha=1.1,minp=6):
    out=[]
    st=defaultdict(lambda:[0,0,0]); key=None; tot=[0,0]
    for m in matches:
        k=(m["lg"],m["season"])
        if k!=key: st=defaultdict(lambda:[0,0,0]); key=k; tot=[0,0]
        H=st[m["h"]];A=st[m["a"]]
        if H[0]>=minp and A[0]>=minp and tot[1]>0:
            avg=tot[0]/tot[1]  # goals per team per game
            r=lambda x:shrink*x+(1-shrink)*avg
            lh=r(H[1]/H[0])*r(A[2]/A[0])/avg*ha; la=r(A[1]/A[0])*r(H[2]/H[0])/avg/ha
            out.append((m,lh+la))
        H[0]+=1;H[1]+=m["hg"];H[2]+=m["ag"];A[0]+=1;A[1]+=m["ag"];A[2]+=m["hg"]
        tot[0]+=m["hg"]+m["ag"];tot[1]+=2
    return out
def market_p(m,closing=False):
    o,u=(m["pco"],m["pcu"]) if closing else (m["po"],m["pu"])
    if not o or not u: return None
    a,b=1/o,1/u; return a/(a+b)
COMM=0.05
print(f"matches loaded: {len(matches)}")
# ---- Test A: betting O/U 2.5 at Betfair exchange (pre-match) ----
print("\nTEST A - betting Over/Under 2.5 at Betfair exchange prices (5% commission)")
print("shrink  w    bets  win%  exp%   ROI    CLV(vs Pinnacle close)")
for shrink in (0.5,0.75,0.9):
    preds=run(shrink)
    for w in (0.0,0.5,0.7):
        n=pl=stake=wins=0; exp=0; clv=0; nclv=0
        for m,lam in preds:
            pm=market_p(m)
            if pm is None: continue
            for side,price,close in (("O",m["bfo"],m["pco"]),("U",m["bfu"],m["pcu"])):
                if not price or price<1.65 or price>10: continue
                pmod=P(lam,3) if side=="O" else 1-P(lam,3)
                pmk=pm if side=="O" else 1-pm
                ch=(1-w)*pmod+w*pmk
                payout=1+(price-1)*(1-COMM)
                if ch*payout<1.15: continue
                won=(m["hg"]+m["ag"]>=3)==(side=="O")
                n+=1;stake+=1;wins+=won;exp+=ch
                pl+=(price-1)*(1-COMM) if won else -1
                if close: clv+=price/close-1; nclv+=1
        if n: print(f"{shrink:<7}{w:<5}{n:<6}{wins/n:5.0%} {exp/n:5.0%} {pl/stake:+6.1%}  {clv/max(nclv,1):+6.1%}")
# ---- Test B: calibration of P(4+), P(5+) model vs market-derived ----
print("\nTEST B - accuracy for 4+ and 5+ goals (lower log-loss = better)")
preds=run(0.75)
for k,label in ((4,"4+ goals (over 3.5)"),(5,"5+ goals (over 4.5)")):
    ll={"model":0,"market (close)":0,"blend 30/70":0}; n=0
    bins=defaultdict(lambda:[0,0,0])
    for m,lam in preds:
        pc=market_p(m,closing=True)
        if pc is None: continue
        y=(m["hg"]+m["ag"])>=k
        pmod=P(lam,k); pmk=P(implied_lam(pc),k); pbl=0.3*pmod+0.7*pmk
        for name,p in (("model",pmod),("market (close)",pmk),("blend 30/70",pbl)):
            p=min(max(p,1e-6),1-1e-6); ll[name]+=-(y*math.log(p)+(1-y)*math.log(1-p))
        n+=1
        b=min(int(pmod*10),9); bins[b][0]+=1; bins[b][1]+=y; bins[b][2]+=pmk
    print(f"\n{label}: {n} matches, actual rate {sum(v[1] for v in bins.values())/n:.0%}")
    for name,v in ll.items(): print(f"   log-loss {name:15s} {v/n:.4f}")
    print("   model says -> actually happened (market said)")
    for b in sorted(bins):
        c,y,mk=bins[b]
        if c>=50: print(f"   {b*10:>2}-{b*10+10}%: {y/c:4.0%} of {c:5d} games   (market {mk/c:4.0%})")
