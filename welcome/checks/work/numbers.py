"""Numbers lens, launch setup pieces (checked 2026-11-06). Standard library only.

Dates and weekdays, holiday arithmetic, the AMT phase-out arithmetic implied by Rev. Proc. 2025-32 sec. 4.10,
and the characters' pay totals against how the welcome pieces describe them.
"""
import datetime as dt
import json
import pathlib

ROOT = pathlib.Path("/Users/vu/Workspace/paid-in-equity")


def wd(y, m, d):
    return dt.date(y, m, d).strftime("%A")


def nth_weekday(y, m, weekday, n):
    """n-th given weekday (Mon=0) of a month."""
    d = dt.date(y, m, 1)
    d += dt.timedelta(days=(weekday - d.weekday()) % 7)
    return d + dt.timedelta(weeks=n - 1)


print("== Cheat sheet dates for 2026 returns ==")
for label, (y, m, d) in {
    "Q4 estimated payment (1040-ES): Jan 15 2027": (2027, 1, 15),
    "Jan 31 2027 (statutory date for W-2, 3921, 3922)": (2027, 1, 31),
    "Feb 1 2027 (sheet: W-2, 3921, 3922)": (2027, 2, 1),
    "Feb 15 2027 (statutory 1099-B date)": (2027, 2, 15),
    "Feb 16 2027 (sheet: 1099-B)": (2027, 2, 16),
    "Apr 15 2027 (sheet: return due)": (2027, 4, 15),
}.items():
    print(f"{label}: {wd(y, m, d)}")

wash = nth_weekday(2027, 2, 0, 3)
print("Washington's Birthday 2027 (third Monday of February):", wash, wd(wash.year, wash.month, wash.day))
assert wash == dt.date(2027, 2, 15), "Feb 15 2027 should be the holiday"
# Jan 31 2027 is Sunday -> next business day Monday Feb 1 (not a holiday)
assert dt.date(2027, 1, 31).weekday() == 6
assert dt.date(2027, 2, 1).weekday() == 0
# Feb 15 holiday -> Tuesday Feb 16
assert dt.date(2027, 2, 16).weekday() == 1
# April 15 2027 is a Thursday, not a federal holiday
assert dt.date(2027, 4, 15).weekday() == 3
# Jan 15 2027 Friday, not a holiday (MLK day is third Monday = Jan 18)
print("MLK day 2027:", nth_weekday(2027, 1, 0, 3))
assert dt.date(2027, 1, 15).weekday() == 4

print()
print("== AMT (Rev. Proc. 2025-32 sec. 4.10) ==")
amt = {
    "joint": dict(exempt=140200, threshold=1_000_000, complete=1_280_400),
    "single/HoH": dict(exempt=90100, threshold=500_000, complete=680_200),
    "MFS": dict(exempt=70100, threshold=500_000, complete=640_200),
}
for k, v in amt.items():
    rate = v["exempt"] / (v["complete"] - v["threshold"])
    print(f"{k}: exemption {v['exempt']:,}; threshold {v['threshold']:,}; complete phase-out {v['complete']:,}; implied rate {rate:.4f}")
    assert abs(rate - 0.5) < 1e-9, "implied phase-out rate should be 50 cents per dollar"

print()
print("== Payroll tax figures (Pub 15 (2026); SSA notice 90 FR 49047) ==")
print("Social Security max employee tax at 6.2% x 184,500 =", round(0.062 * 184_500, 2))
print("Additional Medicare thresholds per IRC 3101(b)(2): joint 250,000; MFS = half = ", 250_000 / 2, "; other 200,000")

print()
print("== Schedule dates (schedule.json) ==")
sched = json.load(open(ROOT / "schedule.json"))["issues"]
byid = {i["id"]: i for i in sched}
non_tue = [i["id"] for i in sched if dt.date.fromisoformat(i["date"]).weekday() != 1]
print("issues not on a Tuesday:", non_tue)
for i in ("L1", "13", "14", "15", "1"):
    d = dt.date.fromisoformat(byid[i]["date"])
    print(i, byid[i]["date"], d.strftime("%A"), "|", byid[i]["title"], "|", byid[i]["tool"], "|", byid[i]["tier"])
print("Jan 5 2027:", wd(2027, 1, 5), "| Mar 30 2027:", wd(2027, 3, 30), "| Nov 17 2026:", wd(2026, 11, 17), "| Nov 6 2026:", wd(2026, 11, 6))

# first paid issue and free/paid pairing
paid = [i for i in sched if i["tier"] == "paid"]
print("first paid issue:", paid[0]["id"], paid[0]["date"])
print("paid issues:", len(paid))
# each paid issue should follow a free issue by exactly 7 days
bad = []
for i in sched:
    if i["tier"] == "paid":
        prev = sched[sched.index(i) - 1]
        gap = (dt.date.fromisoformat(i["date"]) - dt.date.fromisoformat(prev["date"])).days
        if prev["tier"] != "free" or gap != 7:
            bad.append(i["id"])
print("paid issues not a week after a free one:", bad)
# topics in Q2-Q4 with free+paid pairs vs. free only
free_after_april = [i["id"] for i in sched if i["date"] >= "2027-04-01" and i["tier"] == "free"]
print("free issues from April:", len(free_after_april))
no_pair = []
for i in sched:
    if i["date"] >= "2027-04-01" and i["tier"] == "free":
        idx = sched.index(i)
        nxt = sched[idx + 1] if idx + 1 < len(sched) else None
        if not nxt or nxt["tier"] != "paid":
            no_pair.append((i["id"], i["date"]))
print("free issues from April with no paid issue the next week ('most topics' check):", no_pair)

print()
print("== Characters vs. welcome pieces ==")
ch = {c["id"]: c for c in json.load(open(ROOT / "characters.json"))["characters"]}
for cid, c in ch.items():
    print(cid, c["age"], c["state"], c["filing_status"], c["total_comp_usd"], "|", c["headline"])
assert ch["priya"]["salary_usd"] + ch["priya"]["rsu_annual_usd"] == 180000
assert ch["marcus"]["salary_usd"] + ch["marcus"]["rsu_annual_usd"] == 350000
assert ch["dana"]["salary_usd"] + ch["dana"]["paper_equity_annual_usd"] == 600000
assert ch["leo"]["salary_usd"] + ch["leo"]["commission_target_usd"] + ch["leo"]["rsu_annual_usd"] == 280000
assert sum(ch["leo"]["commission_by_quarter_usd"]) == 100000 == ch["leo"]["commission_target_usd"]
print("totals match: Priya 180,000; Marcus 350,000; Dana 600,000; Leo 280,000 (140k + 100k + 40k)")
