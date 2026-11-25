import csv, glob, math, os, sys
from collections import defaultdict
D=sys.argv[1]
def num(x):
    try: return float(x)
    except: return None
P=lambda l,k:1-sum(math.exp(-l)*l**i/math.factorial(i) for i in range(k))
def lam_from(p):
    lo,hi=0.2,8
    for _ in range(50):
        mid=(lo+hi)/2
        if P(mid,3)<p: lo=mid
        else: hi=mid
    return mid
rows=[]
for path in glob.glob(os.path.join(D,"*.csv")):
    lg=os.path.basename(path).split("_")[0]
    with open(path,encoding="latin-1") as f:
        for r in csv.DictReader(f):
            if r.get("FTHG") in (None,""): continue
            h,a=num(r.get("AvgH") or r.get("BbAvH")),num(r.get("AvgA") or r.get("BbAvA"))
            o,u=num(r.get("BFE>2.5")),num(r.get("BFE<2.5"))
            pco,pcu=num(r.get("PC>2.5")),num(r.get("PC<2.5"))
            if not (h and a and o and u and pco and pcu): continue
            rows.append(dict(lg=lg,h=h,a=a,o=o,u=u,pco=pco,pcu=pcu,tg=int(r["FTHG"])+int(r["FTAG"])))
def grp(name,sel):
    g=[r for r in rows if sel(r)]
    n=len(g)
    if n<100: return
    res={}
    for side in ("O","U"):
        pl=0;w=0
        for r in g:
            won=(r["tg"]>=3)==(side=="O"); price=r["o"] if side=="O" else r["u"]
            pl+=(price-1)*0.95 if won else -1; w+=won
        res[side]=(w/n,pl/n)
    act4=sum(r["tg"]>=4 for r in g)/n; act5=sum(r["tg"]>=5 for r in g)/n
    imp4=imp5=0
    for r in g:
        a,b=1/r["pco"],1/r["pcu"]; lam=lam_from(a/(a+b)); imp4+=P(lam,4); imp5+=P(lam,5)
    print(f"{name:34s} {n:6d} | O2.5 won {res['O'][0]:4.0%} ROI {res['O'][1]:+6.1%} | U2.5 ROI {res['U'][1]:+6.1%} | "
          f"4+: {act4:4.0%} vs mkt {imp4/n:4.0%} | 5+: {act5:4.0%} vs mkt {imp5/n:4.0%}")
print(f"{len(rows)} matches with prices\n")
print("Group                              games  | backing every Over 2.5 / Under 2.5 at Betfair (5% comm) | goals vs market-implied")
grp("ALL GAMES",lambda r:True)
grp("Home team favourite",lambda r:r["h"]<r["a"])
grp("AWAY team favourite",lambda r:r["a"]<r["h"])
grp("  away fav, away odds < 1.50",lambda r:r["a"]<1.5)
grp("  away fav, away odds 1.50-2.00",lambda r:1.5<=r["a"]<2.0 and r["a"]<r["h"])
grp("  away fav, away odds 2.00+",lambda r:r["a"]>=2.0 and r["a"]<r["h"])
print("\nAway favourite, by league:")
for lg in sorted({r["lg"] for r in rows}):
    grp(f"  {lg}",lambda r,lg=lg:r["lg"]==lg and r["a"]<r["h"])
