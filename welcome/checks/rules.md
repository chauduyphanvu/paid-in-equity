# Rules check: launch setup pieces (2026-11-06)

**Verdict: fail.** 3 blocking, 12 minor. Pieces read: welcome/free.md, paid.md, start-here.md, about.md; site/cheat-sheet.md, disclaimer.md, privacy.md. Details and evidence are in rules.json.

None of the six legal lines is crossed in any piece. The blockers are all about honesty of claims, in the privacy page and the paid edition's date.

## Blocking

1. **site/privacy.md, The newsletter.** "Substack shows us how many readers opened it and clicked its links" understates what Substack gives the publisher. Substack's own guide: per-subscriber "emails received, emails opened, link clicks". The page must list the categories of personal information collected (22575(b)(1)). Say it is per subscriber.
2. **site/privacy.md, This site, last sentence.** "Lets no other party collect information about what you do here" contradicts the sentence before it: GitHub logs every visitor's IP address (GitHub docs). Name the exception. This is the (b)(6) disclosure.
3. **welcome/paid.md (What you get) and welcome/start-here.md (The paid edition).** "The paid edition opens on March 30, 2027" is stated as fact, but the plan says that if fewer than 30 founding memberships sell by March 23, the publisher rethinks the paid edition. Buyers aren't told, or what happens to their money. Use "planned to open" and add the condition and the founding-member outcome (publisher's decision).

## Minor

- privacy.md: "Only Substack, Stripe and the AI service" omits GitHub and the mailbox provider; "Stripe processes the payment" is wrong for iPhone-app buyers (Apple does; paid.md already says so).
- paid.md: "plans across several years" conflicts with rule 2 ("illustrations, not plans"). Use "what-if scenarios".
- paid.md: "code on GitHub" listed as a paid addition while the code is public everywhere else.
- paid.md: renewal paragraph is helpful but gives no price or cancel effects; the pre-January-5 test purchase in house rules is still open.
- free.md: "two quick questions" holds only if the default Substack survey (age, gender, where you hang out) is replaced; use pick-lists, not free text.
- free.md, start-here.md, about.md: "every calculator is tested against the IRS's own worked examples" is wider than the house wording (checklist and calendar tools have none; engine/test/irs is empty today).
- start-here.md: "withholding gap" undefined.
- cheat-sheet.md: AMT, restricted stock, Section 423 and the long-term bullet need glosses; the 83(b) sentence should say IRS consent is only for a mistake of fact (26 CFR 1.83-2(f)); no line saying AI made it and no accountant or lawyer reviewed it.
- privacy.md and about.md: "we" and "the publisher" are never identified.
- Length: cheat sheet about 720 words, privacy about 520, start-here about 414; required content outranks the target.

## The one change that would most improve the set

After the blockers: say who is behind it. Seven pieces say AI agents do the work and a "publisher" directs it, but never that a named person reads the replies and signs off on every issue.

## Notes, not findings

- `{{contact_email}}` is already in the built docs/privacy/index.html; `pie site` doesn't fill it or stop on it, so editing site/privacy.md before the next push is the publisher's job.
- Substack's help center returned 403 to my fetches; the cancellation path comes from search excerpts of its pages. The survey-export detail (responses carry email and name) is from a search summary, not an opened page.
- Numbers and dates in the cheat sheet were left to the other checker.
