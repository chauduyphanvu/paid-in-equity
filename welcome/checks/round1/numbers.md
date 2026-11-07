# Numbers check: launch setup pieces

Checked 2026-11-06. Lens: numbers. Verdict: **pass** (0 blocking, 8 minor).

Scope: site/cheat-sheet.md (every figure, rule, form and date, tax year 2026), welcome/free.md, paid.md, start-here.md, about.md, site/disclaimer.md, site/privacy.md. Script: welcome/checks/work/numbers.py (all comparisons match).

## What I confirmed
- Every number in the cheat sheet matches its primary source for tax year 2026: 22 and 37 percent supplemental withholding (Pub 15 section 7), 37 percent top rate (Rev. Proc. 2025-32 4.01), $184,500 Social Security base (Pub 15; SSA notice, 90 FR 49047), Medicare and Additional Medicare thresholds (IRC 3101(b)(2); Pub 15), AMT exemptions $90,100 / $140,200 and the 50-cent phase-out from $500,000 / $1,000,000 (Rev. Proc. 2025-32 4.10).
- Rules: ESPP and ISO formulas reproduce Pub 525 Examples 8, 10 and 11; holding periods, 83(b) 30 days and no revocation, code B on Form 8949, no withholding on ISO and ESPP wages (Pub 15-B).
- Dates and weekdays (Python): January 15, 2027 (Friday, 1040-ES); February 1, 2027 (Monday; W-2 instructions; January 31 is a Sunday); February 16, 2027 (Tuesday; February 15 is Washington's Birthday); April 15, 2027 (Thursday). Nov 17, 2026, Jan 5 and Mar 30, 2027 are Tuesdays and match schedule.json and the plan; every schedule date is a Tuesday.
- Character facts in the welcome pages match characters.json (ages, states, filing statuses, $180,000 / $350,000 / $280,000 sums).

## Findings (all minor)
1. **cheat-sheet, 83(b):** "on Form 15620" implies the form is required; a written statement is equally valid (Pub 525; Form 15620 says its use is voluntary). Say "Form 15620 or a signed written statement".
2. **cheat-sheet, AMT bullet:** only single and joint are given. Leo files as head of household and uses the $90,100 unmarried amount; married filing separately ($70,100) is missing. Add both.
3. **cheat-sheet, Cost basis:** "granted after 2013" is narrower than the 1099-B instructions ("granted or acquired after 2013"). Widen it.
4. **cheat-sheet, ESPP/ISO bullets:** "lesser of the actual gain and the grant-date discount" goes negative on a loss; Pub 525 says no ordinary income on a loss. Add "or zero".
5. **cheat-sheet, Feb 1 and Feb 16 rows:** derived from statute and holiday rules, since the 2026 General Instructions for Certain Information Returns are not out yet. Sound, but re-check at the January rollover.
6. **privacy, activity rating:** Substack says "email opens and web views", not "reads". Match its wording.
7. **privacy, GitHub link:** redirects to a renamed page; the claim is correct there. Update the URL.
8. **free, about, start-here, disclaimer:** "every calculator is tested against the IRS's own worked examples". engine/years and engine/test/irs are empty and no calculator exists yet. Make sure it is true when L1 ships.

Nothing blocking: no wrong figure, rule, tax year, filing status or date.
