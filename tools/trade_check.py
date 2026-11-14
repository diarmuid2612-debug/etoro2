#!/usr/bin/env python3
"""Mechanical pre-trade check for the eToro pot (CLAUDE.md "Pre-trade checklist").

Usage:
  python3 -I tools/trade_check.py --dir buy --entry 401 --stop 396.5 --target 412 \
      --min-rr 3 --risk 30 [--units 6.6] [--leverage 5] [--cash 1038] \
      [--levels 406.93,412.39] [--quote 401.2] [--spread 0.1]

--levels: every chart level between here and beyond the target (highs/lows, ceilings).
--units: the units from the prepare-trade preview, to confirm the real risk.
Prints each check as PASS/FAIL; exit code 1 if anything fails.
"""
import argparse
import sys


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dir", choices=["buy", "sell"], required=True)
    p.add_argument("--entry", type=float, required=True)
    p.add_argument("--stop", type=float, required=True)
    p.add_argument("--target", type=float, required=True)
    p.add_argument("--min-rr", type=float, required=True)
    p.add_argument("--risk", type=float, default=30.0)
    p.add_argument("--units", type=float)
    p.add_argument("--leverage", type=float, default=1.0)
    p.add_argument("--cash", type=float)
    p.add_argument("--levels", default="")
    p.add_argument("--quote", type=float, help="live price from the preview")
    p.add_argument("--spread", type=float, default=0.0)
    a = p.parse_args()

    fails = 0

    def check(ok, msg):
        nonlocal fails
        print(("PASS  " if ok else "FAIL  ") + msg)
        if not ok:
            fails += 1

    buy = a.dir == "buy"
    sign = 1 if buy else -1

    check((a.stop < a.entry) if buy else (a.stop > a.entry),
          f"stop {a.stop} is on the losing side of entry {a.entry}")
    check((a.target > a.entry) if buy else (a.target < a.entry),
          f"target {a.target} is on the winning side of entry {a.entry}")

    stop_dist = abs(a.entry - a.stop) + a.spread
    reward = abs(a.target - a.entry) - a.spread
    rr = reward / stop_dist if stop_dist > 0 else 0
    check(rr >= a.min_rr, f"reward to risk {rr:.2f} (incl. spread {a.spread}) >= {a.min_rr}")

    levels = [float(x) for x in a.levels.split(",") if x.strip()]
    blocking = [lv for lv in levels if 0 < (lv - a.entry) * sign < abs(a.target - a.entry)]
    check(not blocking,
          "no marked level between entry and target" if not blocking
          else f"levels in the way of the target: {blocking} (target must sit before the first one)")

    units_plan = a.risk / stop_dist if stop_dist > 0 else 0
    exposure = units_plan * a.entry
    print(f"INFO  plan: {units_plan:.4f} units, exposure ${exposure:,.2f}, "
          f"margin at {a.leverage:g}x ${exposure / a.leverage:,.2f}, "
          f"loss at stop ${a.risk:.2f}, gain at target ${units_plan * reward:,.2f}")

    if a.units is not None:
        real_risk = a.units * stop_dist
        check(real_risk <= a.risk * 1.05,
              f"preview units {a.units} risk ${real_risk:.2f} at the stop (limit ${a.risk:.2f} +5%)")
    if a.cash is not None:
        units = a.units if a.units is not None else units_plan
        margin = units * a.entry / a.leverage
        check(margin <= a.cash, f"margin ${margin:,.2f} fits cash ${a.cash:,.2f}")
    if a.quote is not None:
        drift = (a.quote - a.entry) * sign
        check(drift <= 0.25 * abs(a.entry - a.stop),
              f"live quote {a.quote} within a quarter of the stop distance of the planned entry")
        check((a.quote > a.stop) if buy else (a.quote < a.stop),
              f"live quote {a.quote} has not already passed the stop {a.stop}")

    print("ALL CHECKS PASS" if not fails else f"{fails} CHECK(S) FAILED: do not place")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
