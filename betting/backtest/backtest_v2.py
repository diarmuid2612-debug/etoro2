# v2: time-weighted attack/defence ratings (Maher/Dixon-Coles style), walk-forward by matchday
import csv, glob, math, os, sys, datetime as dt
from collections import defaultdict
D=sys.argv[1]; XI=float(sys.argv[2]) if len(sys.argv)>2 else 0.004
def num(x):
    try: return float(x)
    except: return None
def pdate(s):
    for f in ("%d/%m/%Y","%d/%m/%y"):
        try: return dt.datetime.strptime(s,f)
        except: pass
by_lg=defaultdict(list)
for path in sorted(glob.glob(os.path.join(D,"*.csv"))):
    lg,season=os.path.basename(path)[:-4].split("_")
    with open(path,encoding="latin-1") as f:
        for r in csv.DictReader(f):
            if not r.get("HomeTeam") or r.get("FTHG") in (None,""): continue
            d=pdate(r["Date"])
            if not d: continue
            by_lg[lg].append(dict(season=season,date=d,h=r["HomeTeam"],a=r["AwayTeam"],hg=int(r["FTHG"]),ag=int(r["FTAG"]),
              bfo=num(r.get("BFE>2.5")),bfu=num(r.get("BFE<2.5")),po=num(r.get("P>2.5")),pu=num(r.get("P<2.5")),
              pco=num(r.get("PC>2.5")),pcu=num(r.get("PC<2.5"))))
P=lambda l,k:1-sum(math.exp(-l)*l**i/math.factorial(i) for i in range(k))
def fit(hist,today):
    att=defaultdict(lambda:1.0); de=defaultdict(lambda:1.0); home=1.25
    w=[math.exp(-XI*(today-m["date"]).days) for m in hist]
    for _ in range(15):
        num_a=defaultdict(float); den_a=defaultdict(float); num_d=defaultdict(float); den_d=defaultdict(float)
        hn=hd=0
        for m,wt in zip(hist,w):
            h,a=m["h"],m["a"]
            num_a[h]+=wt*m["hg"]; den_a[h]+=wt*de[a]*home; num_a[a]+=wt*m["ag"]; den_a[a]+=wt*de[h]
            num_d[a]+=wt*m["hg"]; den_d[a]+=wt*att[h]*home; num_d[h]+=wt*m["ag"]; den_d[h]+=wt*att[a]
            hn+=wt*m["hg"]; hd+=wt*att[h]*de[a]
        for t in num_a: att[t]=(num_a[t]+1.3)/(den_a[t]+1.0)   # light prior toward average
        for t in num_d: de[t]=(num_d[t]+1.3)/(den_d[t]+1.0)
        home=hn/hd if hd else home
        s=sum(att.values())/len(att); att={k:v/s for k,v in att.items()}; att=defaultdict(lambda:1.0,att)
    return att,de,home
preds=[]
for lg,ms in by_lg.items():
    ms.sort(key=lambda m:m["date"])
    dates=sorted({m["date"] for m in ms})
    i=0
    for d in dates:
        hist=[m for m in ms if (d-m["date"]).days>0 and (d-m["date"]).days<=500]
        today=[m for m in ms if m["date"]==d]
        cnt=defaultdict(int)
        for m in hist:
            if (d-m["date"]).days<=250: cnt[m["h"]]+=1; cnt[m["a"]]+=1
        if len(hist)<150: continue
        att,de,home=fit(hist,d)
        for m in today:
            if cnt[m["h"]]<8 or cnt[m["a"]]<8: continue
            lh=att[m["h"]]*de[m["a"]]*home; la=att[m["a"]]*de[m["h"]]
            preds.append((m,lh+la))
def mkt(m,c=False):
    o,u=(m["pco"],m["pcu"]) if c else (m["po"],m["pu"])
    if not o or not u: return None
    a,b=1/o,1/u; return a/(a+b)
def lam_from(p):
    lo,hi=0.2,8
    for _ in range(50):
        mid=(lo+hi)/2
        if P(mid,3)<p: lo=mid
        else: hi=mid
    return mid
print(f"v2 (xi={XI}) predictions: {len(preds)}")
print("TEST A - O/U 2.5 at Betfair, 5% commission")
for w in (0.0,0.5,0.7):
  for thr in (1.05,1.10,1.15):
    n=pl=wins=0;exp=0
    for m,lam in preds:
        pm=mkt(m)
        if pm is None: continue
        for side,price in (("O",m["bfo"]),("U",m["bfu"])):
            if not price or price<1.65 or price>10: continue
            pmod=P(lam,3) if side=="O" else 1-P(lam,3); pmk=pm if side=="O" else 1-pm
            ch=(1-w)*pmod+w*pmk
            if ch*(1+(price-1)*0.95)<thr: continue
            won=(m["hg"]+m["ag"]>=3)==(side=="O"); n+=1;wins+=won;exp+=ch
            pl+=(price-1)*0.95 if won else -1
    if n: print(f"  w={w} value>={thr}: bets {n:5d} win {wins/n:4.0%} expected {exp/n:4.0%} ROI {pl/n:+6.1%}")
print("TEST B - log-loss (lower=better)")
for k in (3,4,5):
    lm=lk=lb=0;n=0
    for m,lam in preds:
        pc=mkt(m,True)
        if pc is None: continue
        y=(m["hg"]+m["ag"])>=k; pmod=P(lam,k); pmk=P(lam_from(pc),k); pb=0.5*pmod+0.5*pmk
        for p,acc in ((pmod,"m"),(pmk,"k"),(pb,"b")):
            p=min(max(p,1e-6),1-1e-6); v=-(y*math.log(p)+(1-y)*math.log(1-p))
            if acc=="m": lm+=v
            elif acc=="k": lk+=v
            else: lb+=v
        n+=1
    print(f"  {k}+ goals: model {lm/n:.4f}  market {lk/n:.4f}  50/50 blend {lb/n:.4f}  (n={n})")
