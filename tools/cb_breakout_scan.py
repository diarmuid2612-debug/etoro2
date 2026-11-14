"""Breakout -> retest -> confirmation scan on Coinbase daily candles (00:00 UTC).
Input: folder of <PRODUCT>.json files from
  https://api.exchange.coinbase.com/products/<PRODUCT>/candles?granularity=86400
(rows: [time, low, high, open, close, volume], newest first).
Ceiling R = highest close 60..3 days before the breakout day.
Breakout = first daily close >2% above R within the last 25 completed days.
Retest   = after the breakout, a daily LOW came back to R (-4%..+4%) and no close below -3%.
Confirmed = latest close >2% above R, higher than the previous close, <25% above R,
            and the post-breakout peak not more than +50% above R (not a run-away move).
Stop = below the lowest low since the breakout (retest swing low), minus 1%.
Target = post-breakout peak close (first resistance); R:R reported.
Liquidity = average daily USD volume over 30 days."""
import json,glob,os,sys,datetime as dt
D=sys.argv[1]; today=dt.datetime.utcnow().date(); rows=[]
for f in glob.glob(f"{D}/*.json"):
    try: K=json.load(open(f))
    except Exception: continue
    if not isinstance(K,list) or len(K)<90: continue
    K=sorted(K)                                   # oldest first
    if dt.datetime.utcfromtimestamp(K[-1][0]).date()>=today: K=K[:-1]   # drop today's partial candle
    lo=[k[1] for k in K]; hi=[k[2] for k in K]; c=[k[4] for k in K]; v=[k[5]*k[4] for k in K]
    n=len(c); last=c[-1]; pid=os.path.basename(f)[:-5]; liq=sum(v[-30:])/30
    for b in range(n-25,n):
        R=max(c[max(0,b-60):b-3])
        if not (c[b]>R*1.02 and c[b-1]<=R*1.02): continue
        after_c=c[b+1:]; after_l=lo[b+1:]
        peak=max(c[b:])
        if not after_c: st="BREAKOUT (no retest yet)"
        elif min(after_c)<R*0.97: st="FAILED (closed back below)"
        elif min(after_l)>R*1.04: st="BREAKOUT (no retest yet)"
        elif last>R*1.02 and last>c[-2] and last<R*1.25 and peak<R*1.5: st="CONFIRMED"
        elif peak>=R*1.5: st="EXTENDED (ran 50%+)"
        else: st="RETESTING (no confirming close)"
        swing=min(lo[b:]); stop=min(swing,R*0.96)*0.99
        rr=(peak-last)/(last-stop) if last>stop else None
        rows.append((st,pid,str(dt.datetime.utcfromtimestamp(K[b][0]).date()),R,last,last/R-1,peak/R-1,stop,(last-stop)/last,rr,liq))
        break
order={"CONFIRMED":0,"RETESTING (no confirming close)":1,"BREAKOUT (no retest yet)":2,"EXTENDED (ran 50%+)":3,"FAILED (closed back below)":4}
print(f"scanned {len(glob.glob(D+'/*.json'))} products")
print("status | product | breakout | ceiling | last | last/ceil | peak/ceil | stop | stop% | R:R to peak | $vol/day")
for r in sorted(rows,key=lambda r:(order[r[0]],-r[10])):
    st,p,bd,R,last,lr,pr,stop,sp,rr,liq=r
    print(f"{st} | {p} | {bd} | {R:.6g} | {last:.6g} | {lr:+.1%} | {pr:+.1%} | {stop:.6g} | {sp:.1%} | {rr if rr is None else round(rr,2)} | {liq:,.0f}")
