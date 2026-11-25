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
P=lambda l,k:1-sum(math.exp(-l)*l**i/math.factorial(i) for i in range(k))
def lam_from(p):
    lo,hi=0.2,8
    for _ in range(50):
        mid=(lo+hi)/2
        if P(mid,3)<p: lo=mid
        else: hi=mid
    return mid
games=[]
for path in sorted(glob.glob(os.path.join(D,"*.csv"))):
    lg,season=os.path.basename(path)[:-4].split("_")
    ms=[]
    for r in csv.DictReader(open(path,encoding="latin-1")):
        if r.get("FTHG") in (None,"") or not pdate(r["Date"]): continue
        ms.append(r)
    ms.sort(key=lambda r:pdate(r["Date"]))
    tab=defaultdict(lambda:[0,0,0])  # played, points, goal diff
    for r in ms:
        h,a,hg,ag=r["HomeTeam"],r["AwayTeam"],int(r["FTHG"]),int(r["FTAG"])
        order=sorted(tab,key=lambda t:(-tab[t][1],-tab[t][2]))
        pos={t:i+1 for i,t in enumerate(order)}
        if tab[h][0]>=6 and tab[a][0]>=6 and h in pos and a in pos:
            games.append(dict(lg=lg,season=season,gap=pos[h]-pos[a],tg=hg+ag,
                bo=num(r.get("BFE>2.5")),bu=num(r.get("BFE<2.5")),po=num(r.get("P>2.5")),pu=num(r.get("P<2.5")),
                pco=num(r.get("PC>2.5")),pcu=num(r.get("PC<2.5"))))
        tab[h][0]+=1;tab[a][0]+=1;tab[h][2]+=hg-ag;tab[a][2]+=ag-hg
        if hg>ag: tab[h][1]+=3
        elif hg<ag: tab[a][1]+=3
        else: tab[h][1]+=1;tab[a][1]+=1
def report(name,g):
    if len(g)<80: return
    def roi(side,col_o,col_u,comm):
        n=pl=w=0
        for x in g:
            price=x[col_o] if side=="O" else x[col_u]
            if not price: continue
            won=(x["tg"]>=3)==(side=="O"); n+=1; w+=won; pl+=(price-1)*(1-comm) if won else -1
        return (pl/n, w/n, n) if n else (None,None,0)
    po=roi("O","po","pu",0); pu=roi("U","po","pu",0); bo=roi("O","bo","bu",0.05); bu=roi("U","bo","bu",0.05)
    gm=[x for x in g if x["pco"] and x["pcu"]]
    a4=sum(x["tg"]>=4 for x in gm)/len(gm); a5=sum(x["tg"]>=5 for x in gm)/len(gm)
    i4=i5=0
    for x in gm:
        p=(1/x["pco"])/((1/x["pco"])+(1/x["pcu"])); l=lam_from(p); i4+=P(l,4); i5+=P(l,5)
    f=lambda v:"   n/a" if v is None else f"{v:+6.1%}"
    print(f"{name:38s} {len(g):5d} | O2.5 won {po[1]:4.0%}  Pinnacle {f(po[0])}  Betfair {f(bo[0])} ({bo[2]:4d}) | U2.5 Pinnacle {f(pu[0])} | "
          f"4+ {a4:4.0%} v {i4/len(gm):4.0%} | 5+ {a5:4.0%} v {i5/len(gm):4.0%}")
old=("2122","2223","2324"); new=("2425","2526")
print("Group (away team N+ places higher)        games | over 2.5 ROI (Pinnacle, Betfair after 5%) | under 2.5 | goals actual v market\n")
report("All games (from matchday 7)",games)
for gap in (5,8,10):
    sel=[x for x in games if x["gap"]>=gap]
    report(f"Away {gap}+ places higher",sel)
    report(f"   older 3 seasons",[x for x in sel if x["season"] in old])
    report(f"   latest 2 seasons",[x for x in sel if x["season"] in new])
print("\nAway 5+ places higher, by league:")
for lg in sorted({x["lg"] for x in games}):
    sel=[x for x in games if x["gap"]>=5 and x["lg"]==lg]
    report(f"  {lg}",sel)
    report(f"     older",[x for x in sel if x["season"] in old]); report(f"     latest",[x for x in sel if x["season"] in new])
