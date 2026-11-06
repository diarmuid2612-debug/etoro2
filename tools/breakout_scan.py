"""Breakout -> retest -> confirmation scan on daily closes (00:00 UTC).
A qualifying coin: first close >2% above the prior 60-day ceiling (max close 60..3 days
before) within the last 25 days; after that, closes came back to the ceiling (-3%..+5%)
without closing below -3%; the latest close is back above +2% of the ceiling, higher
than the previous close, and less than 25% above the ceiling (not extended)."""
import json,glob,os,sys,datetime as dt
D=sys.argv[1]; rows=[]
for f in glob.glob(f"{D}/*.json"):
    try: P=json.load(open(f))["prices"]
    except Exception: continue
    pts=[(dt.datetime.utcfromtimestamp(t/1000),v) for t,v in P]
    if pts and (pts[-1][0].hour or pts[-1][0].minute): pts=pts[:-1]
    c=[v for _,v in pts]
    if len(c)<80: continue
    n=len(c); last=c[-1]; id=os.path.basename(f)[:-5]
    for b in range(n-25,n):
        R=max(c[max(0,b-60):b-3])
        if not (c[b]>R*1.02 and c[b-1]<=R*1.02): continue
        after=c[b+1:]; low=min(after) if after else None
        if not after: st="BREAKOUT (no retest yet)"
        elif low<R*0.97: st="FAILED (closed back below)"
        elif low>R*1.05: st="BREAKOUT (no retest yet)"
        elif last>R*1.02 and last>c[-2] and last<R*1.25: st="CONFIRMED"
        else: st="RETESTING (no confirming close)"
        rows.append((st,id,str(pts[b][0].date()),round(R,6),round(low,6) if low else None,round(last,6),round(last/R-1,3),round(max(c[b:])/R-1,3)))
        break
order={"CONFIRMED":0,"RETESTING (no confirming close)":1,"BREAKOUT (no retest yet)":2,"FAILED (closed back below)":3}
print("status | coin | breakout day | ceiling | retest low | last close | last vs ceiling | peak vs ceiling")
for r in sorted(rows,key=lambda r:(order[r[0]],r[1])): print(" | ".join(map(str,r)))
