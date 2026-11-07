# Rules check: launch setup pieces (welcome/ and site/)

Checked 2026-11-06, rules lens. Verdict: **fail**. 3 blocking, 14 minor. All three blocking findings are on `site/privacy.md`. No legal line (house rules 1 to 6) is crossed in any of the seven pieces.

## Blocking

1. **site/privacy.md, "This site" and "Your choices": §22575(b)(6) missing.** The policy must say whether other parties may collect personal information about a visitor's activity across sites when they use the site or service. It only says "Substack's pages follow its own policy". Substack's policy says it uses third-party analytics cookies, may collect activity after you leave, and ignores Do Not Track. Fix: one plain sentence for the site (true only if no Substack form or other outside script is embedded) and one for Substack.
2. **site/privacy.md, "The newsletter": §22575(b)(1) missing.** No categories of third parties the publisher may share data with; the page says only who it does not share with (sponsors). Name Substack, Stripe and the AI tools. Add "name" to what Substack passes on (Substack's policy: name and email address).
3. **site/privacy.md, "Email you send us": untrue by omission.** "Stay in the publisher's email and a private folder" leaves out that AI agents read and draft replies to reader mail (house rule 6), via an AI provider's service. Say so. If the publisher really answers all mail alone, change rule 6 instead.

## Minor

- privacy.md: "used only to answer them and fix errors" is narrower than the plan (a question can become an issue with permission). Survey answers are linked to the subscriber's email or profile (Substack Help), and the activity rating is "email opens and web views". "The site sets no cookies" is false if the rules-change sign-up is a Substack embed. The only contact route is "reply to any issue", which an unsubscribed person lacks: give an address.
- disclaimer.md, free.md, start-here.md promise a dated correction "under the post's summary" and a mention in "the next email"; house rules require only a log line and an updated post. Confirm the correction steps do both.
- paid.md: "cancel in your Substack settings" misses subscribers who paid in the iPhone app (Apple). The membership sentence never says AI agents do the work. The XLSX-below-paywall claim isn't confirmed by any Substack page I could reach (Substack confirms XLSX attachments only): test with a free account. The two-Tuesdays pattern starts "from Q2" in the plan, not March 30.
- cheat-sheet.md: Form 15620 is optional (a Treas. Reg. 1.83-2 statement also works, per the form). Undefined terms: basis, supplemental pay, lookback, offering date, AMT income, capital gain, estimated payment; disclaimer uses RSUs before defining them. IRS says "granted or acquired after 2013" (passed to numbers checker).
- start-here.md and free.md: Priya's age and "withholding gap calculator" can't be confirmed from plan.md (check characters.json, schedule.json); "tax forms on their way" in December is February in the plan; free.md never states the first issue date (November 17).
- Length: start-here about 426 words and cheat-sheet about 570 (419 without Sources) are over 400; the others are under.
- start-here.md comment: pinning is the post's three-dot menu, "Pin to home page" (or the homepage editor), not Settings > Website.

## Verified

Provider names appear only as the publisher's own infrastructure. Disclaimer covers all four items in "Site and email"; privacy covers its list. §22575(b)(2) to (5) are met. GitHub Pages logs IP addresses regardless of sign-in (GitHub Docs, "Data collection"). Substack setup paths for welcome emails, About page, short description, publish-without-email, unsubscribe, account deletion. Form 15620 30-day rule and no revocation without consent. How-it's-made and not-advice lines present where the issue footer would have them.

Sources: statute text from AB 370 (Stats. 2013) copy at mintz.com, because leginfo.legislature.ca.gov returned 403; Substack help pages returned 403 to my fetch, so their wording comes from search summaries of those pages, and I did not work around the block.

## The one change that most improves the set

Rewrite privacy.md's "The newsletter" and "Email you send us" sections to say who receives readers' data, AI agents included. That fixes all three blockers at once and makes the page match the newsletter's promise of being honest about how it is made.
