"""Numbers-lens recomputation for the launch setup pieces (plain standard library).

Run: python3 welcome/checks/work/numbers.py   (from the project folder)
"""
import datetime as dt
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
ok = True


def check(label, mine, theirs):
    global ok
    good = mine == theirs
    ok &= good
    print(f"{'OK  ' if good else 'DIFF'} {label}: mine={mine!r} piece={theirs!r}")


def wd(y, m, d):
    return dt.date(y, m, d).strftime("%A")


print("== Weekdays of every date the pieces state ==")
dates = {
    "about.md first issue 'Tuesday, November 17, 2026'": ((2026, 11, 17), "Tuesday"),
    "start-here.md first issue 'November 17'": ((2026, 11, 17), "Tuesday"),
    "paid.md/start-here.md founding memberships January 5, 2027": ((2027, 1, 5), "Tuesday"),
    "paid.md/start-here.md paid edition opens March 30, 2027": ((2027, 3, 30), "Tuesday"),
    "privacy.md effective November 6, 2026 (today)": ((2026, 11, 6), "Friday"),
}
for label, (ymd, stated) in dates.items():
    check(label, wd(*ymd), stated)

print("\n== Cheat sheet 'Dates for 2026 returns' ==")
# 4th estimated payment: 1040-ES (2026) says Jan. 15, 2027.
print("Jan 15, 2027 is a", wd(2027, 1, 15), "(not a holiday; MLK Day is the 3rd Monday = Jan 18)")
# W-2 / 3921 / 3922: statutory Jan 31 (IRC 6039(b); W-2 instructions say Feb 1, 2027)
jan31 = dt.date(2027, 1, 31)
print("Jan 31, 2027 is a", jan31.strftime("%A"), "-> next business day", (jan31 + dt.timedelta(days=1)).strftime("%A %B %d, %Y"))
check("Feb 1, 2027 weekday (W-2, 3921, 3922 date)", wd(2027, 2, 1), "Monday")
# 1099-B: Feb 15 (Reg. 1.6045-1(k)(2)); Feb 15, 2027 = third Monday of February?
mondays = [dt.date(2027, 2, d) for d in range(1, 29) if dt.date(2027, 2, d).weekday() == 0]
third_monday = mondays[2]
check("third Monday of February 2027 (Washington's Birthday, 5 U.S.C. 6103)", third_monday.isoformat(), "2027-02-15")
feb16 = third_monday + dt.timedelta(days=1)
check("1099-B date after holiday roll", (feb16.isoformat(), feb16.strftime("%A")), ("2027-02-16", "Tuesday"))
# April 15
check("April 15, 2027 weekday", wd(2027, 4, 15), "Thursday")
print("April 16, 2027 (DC Emancipation Day) is a", wd(2027, 4, 16), "-> does not move April 15")
# Pub 525 / 2026 pattern: Jan 31, 2026 Saturday -> Feb 2; Feb 15, 2026 Sunday, Feb 16 holiday -> Feb 17
print("2026 pattern check: Jan 31, 2026 =", wd(2026, 1, 31), "; Feb 15, 2026 =", wd(2026, 2, 15), "; Feb 16, 2026 =", wd(2026, 2, 16))

print("\n== Schedule: every issue date is a Tuesday; welcome-piece dates match the schedule ==")
sched = json.loads((ROOT / "schedule.json").read_text())["issues"]
bad = [i["id"] for i in sched if dt.date.fromisoformat(i["date"]).strftime("%A") != "Tuesday"]
check("non-Tuesday schedule dates", bad, [])
by_id = {i["id"]: i for i in sched}
check("L1 date (first issue)", by_id["L1"]["date"], "2026-11-17")
check("L1 tool", by_id["L1"]["tool"], "Withholding gap calculator")
check("issue 1 date (tax season starts in January)", by_id["1"]["date"], "2027-01-05")
check("issue 13 date (paid edition opens)", by_id["13"]["date"], "2027-03-30")
check("issue 13 sketch says paid edition opens", "paid edition opens" in by_id["13"]["title"], True)
first_paid = min((i for i in sched if i["tier"] == "paid"), key=lambda i: i["date"])
print("first paid-tier issue:", first_paid["id"], first_paid["date"], "- pair_of", first_paid.get("pair_of"),
      "(free partner", by_id[first_paid["pair_of"]]["date"] + ")")
gaps = {(dt.date.fromisoformat(i["date"]) - dt.date.fromisoformat(by_id[i["pair_of"]]["date"])).days
        for i in sched if i["tier"] == "paid"}
check("paid issue follows its free issue by days", gaps, {7})
print("L-series (2026) dates:", [i["date"] for i in sched if i["id"].startswith("L")])

print("\n== Characters (characters.json) vs. the welcome pieces ==")
ch = {c["id"]: c for c in json.loads((ROOT / "characters.json").read_text())["characters"]}
check("Priya salary+RSU", ch["priya"]["salary_usd"] + ch["priya"]["rsu_annual_usd"], 180000)
check("Priya total_comp_usd", ch["priya"]["total_comp_usd"], 180000)
check("Priya age/state/status", (ch["priya"]["age"], ch["priya"]["state"], ch["priya"]["filing_status"]), (24, "WA", "single"))
check("Marcus salary+RSU", ch["marcus"]["salary_usd"] + ch["marcus"]["rsu_annual_usd"], 350000)
check("Marcus state/status", (ch["marcus"]["state"], ch["marcus"]["filing_status"]), ("CA", "married filing jointly"))
check("Dana state / ISO", (ch["dana"]["state"], "iso" in ch["dana"]), ("CA", True))
check("Dana salary+paper equity", ch["dana"]["salary_usd"] + ch["dana"]["paper_equity_annual_usd"], ch["dana"]["total_comp_usd"])
leo = ch["leo"]
check("Leo salary+commission+RSU", leo["salary_usd"] + leo["commission_target_usd"] + leo["rsu_annual_usd"], 280000)
check("Leo commissions by quarter sum", sum(leo["commission_by_quarter_usd"]), leo["commission_target_usd"])
check("Leo state/status", (leo["state"], leo["filing_status"]), ("TX", "head of household"))
check("Priya/Marcus have ESPP, Dana/Leo do not",
      ("espp" in ch["priya"], "espp" in ch["marcus"], "espp" in ch["dana"], "espp" in leo), (True, True, False, False))

print("\n== 2026 figures vs. sources (values read from the primary documents) ==")
# Rev. Proc. 2025-32 sec. 4.10: exemption / threshold / complete phaseout
rp = {"joint": (140200, 1_000_000, 1_280_400), "unmarried": (90100, 500_000, 680_200), "mfs": (70100, 500_000, 640_200)}
for k, (ex, thr, comp) in rp.items():
    check(f"AMT {k}: complete phase-out = threshold + exemption / 0.50", thr + ex / 0.50, comp)
print("  (the same arithmetic at 25 cents would give", {k: v[1] + v[0] / 0.25 for k, v in rp.items()}, "- so the 50-cent rate is confirmed)")
check("MFS Additional Medicare threshold = half of joint (IRC 3101(b)(2)(B))", 250000 / 2, 125000)
check("Social Security max employee tax at $184,500 x 6.2%", round(184500 * 0.062, 2), 11439.00)

print("\n== Pub 525 (2025) worked examples through the cheat sheet's ESPP rules ==")
# Example 10: qualifying ESPP. Option price 20, grant FMV 22, exercise FMV 23, sale 30.
price, grant_fmv, buy_fmv, sale = 20, 22, 23, 30
gain = sale - price
wages_q = max(0, min(gain, grant_fmv - price))
check("Example 10 wages per share (qualifying: lesser of gain and grant-date discount)", wages_q, 2)
check("Example 10 capital gain per share", gain - wages_q, 8)
wages_dq = buy_fmv - price
check("Example 11 wages per share (sold early: purchase-date value minus price)", wages_dq, 3)
check("Example 11 capital gain per share", sale - (price + wages_dq), 7)
# 15% discount plan with lookback: price = 85% of lower of grant and purchase value; grant-date discount = 15% of grant value
g, p = 100.0, 120.0
paid = 0.85 * min(g, p)
check("15% plan: discount at grant = 15% of grant value (per share)", round(g - 0.85 * g, 2), 15.0)
sale_px = 150.0
check("15% plan, qualifying sale at 150: wages", round(min(sale_px - paid, g - 0.85 * g), 2), 15.0)
check("15% plan, sold early (purchase value 120, paid 85): wages", round(p - paid, 2), 35.0)
# Pub 525 Example 8: ISO sold early. option 10, exercise FMV 12, sale 15 -> wages 2, capital gain 3
iso_wages = max(0, min(12 - 10, 15 - 10))
check("Example 8 ISO sold early wages per share (spread capped at gain)", iso_wages, 2)
check("Example 8 ISO sold at a loss (sale 9): wages", max(0, min(12 - 10, 9 - 10)), 0)

print("\n== 83(b) 30-day clock (illustration only) ==")
t = dt.date(2026, 12, 28)
d30 = t + dt.timedelta(days=30)
print("transfer", t, "-> day 30 is", d30, d30.strftime("%A"), "(Form 15620 instructions: roll to next business day under IRC 7503 if Sat/Sun/holiday)")

print("\nALL MATCH" if ok else "\nSOME DIFFERENCES - see DIFF lines")
