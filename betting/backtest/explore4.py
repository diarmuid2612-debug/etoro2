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
    for _ in range(40):
        mid=(lo+hi)/2
        if P(mid,3)<p: lo=mid
        else: hi=mid
    return mid
G=[]
for path in sorted(glob.glob(os.path.join(D,"*.csv"))):
    lg,season=os.path.basename(path)[:-4].split("_")
    ms=[r for r in csv.DictReader(open(path,encoding="latin-1")) if r.get("FTHG") not in (None,"") and pdate(r["Date"])]
    ms.sort(key=lambda r:pdate(r["Date"]))
    st=defaultdict(lambda:dict(p=0,gf=0,ga=0,pts=0,gd=0,last=None,lastdate=None))
    for r in ms:
        h,a=r["HomeTeam"],r["AwayTeam"];hg,ag=int(r["FTHG"]),int(r["FTAG"]);d=pdate(r["Date"])
        H,A=st[h],st[a]
        pco,pcu=num(r.get("PC>2.5")),num(r.get("PC<2.5"))
        if H["p"]>=6 and A["p"]>=6 and pco and pcu:
            order=sorted(st,key=lambda t:(-st[t]["pts"],-st[t]["gd"])); pos={t:i+1 for i,t in enumerate(order)}; n=len(order)
            p=(1/pco)/((1/pco)+(1/pcu)); lam=lam_from(p)
            ah,aa=num(r.get("AvgH")),num(r.get("AvgA"))
            t=r.get("Time") or ""
            G.append(dict(lg=lg,tg=hg+ag,mk4=P(lam,4),mkt_o25=p,
                fav=min(ah,aa) if ah and aa else None, awayfav=(aa<ah) if ah and aa else None,
                month=d.month,wd=d.weekday(),hour=int(t[:2]) if t[:2].isdigit() else None,
                h_conc=H["ga"]/H["p"],a_conc=A["ga"]/A["p"],h_sc=H["gf"]/H["p"],a_sc=A["gf"]/A["p"],
                hpos=pos.get(h),apos=pos.get(a),n=n,
                h_last=H["last"],a_last=A["last"],
                h_rest=(d-H["lastdate"]).days if H["lastdate"] else None,a_rest=(d-A["lastdate"]).days if A["lastdate"] else None,
                red=(num(r.get("HR")) or 0)+(num(r.get("AR")) or 0),ref=r.get("Referee"),
                hst=num(r.get("HST")),ast=num(r.get("AST"))))
        for T,gf,ga in ((H,hg,ag),(A,ag,hg)):
            T["p"]+=1;T["gf"]+=gf;T["ga"]+=ga;T["gd"]+=gf-ga;T["pts"]+=3 if gf>ga else 1 if gf==ga else 0
            T["last"]=hg+ag;T["lastdate"]=d
N=len(G); base=sum(g["tg"]>=4 for g in G)/N
print(f"{N} games (matchday 7+, with closing prices); 4+ goals in {base:.1%}\n")
def show(title,groups):
    print(title)
    print(f"   {'group':34s} {'games':>6s} {'4+ actual':>9s} {'market':>7s} {'diff':>6s}")
    for name,sel in groups:
        g=[x for x in G if sel(x)]
        if len(g)<150: continue
        act=sum(x["tg"]>=4 for x in g)/len(g); mk=sum(x["mk4"] for x in g)/len(g)
        se=math.sqrt(act*(1-act)/len(g)); flag=" <--" if abs(act-mk)>2.5*se else ""
        print(f"   {name:34s} {len(g):6d} {act:9.1%} {mk:7.1%} {act-mk:+6.1%}{flag}")
    print()
show("1. What the MARKET expected (closing over 2.5 chance)",[(f"market over2.5 {lo}-{lo+10}%",lambda x,lo=lo:lo/100<=x["mkt_o25"]<(lo+10)/100) for lo in range(30,80,10)])
show("2. Defences: goals conceded per game before the match",[("both concede 1.5+ per game",lambda x:x["h_conc"]>=1.5 and x["a_conc"]>=1.5),
  ("both concede under 1.0",lambda x:x["h_conc"]<1.0 and x["a_conc"]<1.0),("home concedes 1.8+",lambda x:x["h_conc"]>=1.8),("away concedes 1.8+",lambda x:x["a_conc"]>=1.8)])
show("3. Attacks: goals scored per game",[("both score 1.6+",lambda x:x["h_sc"]>=1.6 and x["a_sc"]>=1.6),("both score under 1.1",lambda x:x["h_sc"]<1.1 and x["a_sc"]<1.1)])
show("4. Strength of the favourite (match odds)",[("big favourite (<1.40)",lambda x:x["fav"] and x["fav"]<1.4),("clear fav 1.40-1.80",lambda x:x["fav"] and 1.4<=x["fav"]<1.8),("close game (fav 2.00+)",lambda x:x["fav"] and x["fav"]>=2.0),("away team favourite",lambda x:x["awayfav"])])
show("5. Table position",[("both top 4",lambda x:x["hpos"]<=4 and x["apos"]<=4),("both bottom 4",lambda x:x["hpos"]>x["n"]-4 and x["apos"]>x["n"]-4),("top 4 v bottom 4",lambda x:min(x["hpos"],x["apos"])<=4 and max(x["hpos"],x["apos"])>x["n"]-4)])
show("6. Previous game of each team",[("both teams' last game had 4+",lambda x:(x["h_last"] or 0)>=4 and (x["a_last"] or 0)>=4),("either team's last game had 4+",lambda x:(x["h_last"] or 0)>=4 or (x["a_last"] or 0)>=4),("both last games 0-1 goals",lambda x:(x["h_last"] if x["h_last"] is not None else 9)<=1 and (x["a_last"] if x["a_last"] is not None else 9)<=1)])
show("7. Rest days",[("either team 3 days or less rest",lambda x:(x["h_rest"] or 99)<=3 or (x["a_rest"] or 99)<=3),("both 6+ days rest",lambda x:(x["h_rest"] or 0)>=6 and (x["a_rest"] or 0)>=6)])
show("8. When",[(m,lambda x,i=i:x["month"]==i) for i,m in ((8,"August"),(9,"September"),(10,"October"),(11,"November"),(12,"December"),(1,"January"),(2,"February"),(3,"March"),(4,"April"),(5,"May"))]+
  [("midweek (Tue-Thu)",lambda x:x["wd"] in (1,2,3)),("evening kick-off 19:00+",lambda x:x["hour"] is not None and x["hour"]>=19),("lunchtime before 14:00",lambda x:x["hour"] is not None and x["hour"]<14)])
show("9. League",[(lg,lambda x,lg=lg:x["lg"]==lg) for lg in sorted({x["lg"] for x in G})])
show("10. IN-GAME (only known after kick-off - not usable before)",[("a red card shown",lambda x:x["red"]>=1),("10+ shots on target combined",lambda x:x["hst"] is not None and x["hst"]+x["ast"]>=10)])
