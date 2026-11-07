# Numbers check: launch setup pieces (2026-11-06)

**Verdict: fail.** 1 blocking, 5 minor. The cheat sheet's figures, rules and dates are all correct for tax year 2026; the blocking item is in the privacy page. Script: `welcome/checks/work/numbers.py`.

## Blocking

1. **site/privacy.md, "The newsletter", sentence 2.** "Substack shows us how many readers opened it and clicked its links" reads as aggregate counts only. Substack's own help pages say the publisher sees each subscriber's own email-open counts and, per subscriber, "emails received, emails opened, link clicks". A reader would think individual opens and clicks are invisible to the publisher. Fix: "Substack shows us, for each subscriber, how many of our emails they opened and which links they clicked, and gives each an activity rating based on email opens and web views." (Sources: support.substack.com 360058529871; on.substack.com/p/subscriber-dashboard-guide.)

## Minor

- **privacy.md, "This site" and Do Not Track bullet.** "lets no other party collect information about what you do here" and "tracks no one" follow a sentence saying GitHub logs every visitor's IP. The host sees page requests. Say the site itself sets no cookies and runs no tracking of its own.
- **privacy.md, payments and "Who gets your information."** Says Stripe processes the payment. paid.md says some readers subscribe in the iPhone app, where Apple takes the payment. Add Apple (or "the payment processor you choose"). Substack's policy also lists card details among data Substack collects, so "Stripe holds your card details" is more specific than its source.
- **paid.md, top comment.** Substack sends founding members a separate "Welcome email to founding subscribers". Founding memberships go on sale January 5, so the first buyers would not get this text unless it is pasted there too.
- **paid.md, "renews automatically each year."** True only for annual plans; Substack also has monthly. Keep it if only annual plans are sold.
- **free.md, start-here.md, about.md, "each comes with a free calculator."** schedule.json issue 13 (March 30, 2027) says "There's no new calculator"; issues 26, 35, 46, 51 and 52 list a survey page, reader questions, an interactive report and a preview. Say "most issues".

## Confirmed (full list in numbers.json)

- **Cheat sheet figures.**
  - Supplemental withholding 22%, and 37% over $1 million (Pub 15 (2026)).
  - Social Security wage base $184,500 (Pub 15 (2026); 90 FR 49047).
  - Medicare 1.45%; Additional Medicare 0.9% over $250,000 joint, $125,000 MFS, $200,000 otherwise (IRC 3101(b)(2)); employers start at $200,000.
  - AMT exemption $90,100 / $140,200 / $70,100, phase-out starting at $500,000 (single, head of household, MFS) and $1,000,000 (joint) at 50 cents per dollar (Rev. Proc. 2025-32 sec. 4.10; complete phase-out amounts equal threshold plus twice the exemption).
- **Cheat sheet rules.** ESPP and ISO holding periods, the ESPP qualifying-wage "lesser of" rule, disqualifying-sale wages, no withholding on these wages, the basis rule for stock granted or acquired after 2013 with Form 8949 code B, and the 83(b) 30-day, Form 15620 and no-revocation rules all match Pub 525, Pub 15-B, 26 CFR 1.6045-1 and the Form 15620 instructions.
- **Cheat sheet dates (Python weekdays).**
  - January 15, 2027 is a Friday (Form 1040-ES).
  - February 1, 2027 is a Monday: January 31 is a Sunday for W-2, 3921 and 3922.
  - February 16, 2027 is a Tuesday: February 15 is Washington's Birthday, so the 1099-B date moves.
  - April 15, 2027 is a Thursday.
  - There is no consolidated-statement extension in the IRS instructions.
- **Welcome pieces.**
  - November 17, 2026, March 30, 2027 and January 5, 2027 are all Tuesdays.
  - The first paid issue is April 13, 2027, always a week after a free one, so "most topics get two Tuesdays" holds.
  - The four characters' ages, states, filing statuses and pay match characters.json, and the pay components add up to $180,000, $350,000, $600,000 and $280,000.
  - The founding-sale date of January 5 is not in schedule.json, so I could only check that nothing contradicts it.
- **Platform claims.**
  - GitHub's IP logging matches its docs.
  - Substack's cookies, Do Not Track and activity-rating statements match its privacy policy and help center.
  - Substack allows XLSX attachments, cancelling goes through Settings or the App Store, and the default welcome email carries the survey link.
- **Links.** All 29 links in the pieces resolve.
