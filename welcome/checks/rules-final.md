# Rules check (final): site/privacy.md and welcome/paid.md

Checked 2026-11-06. Verdict: **fail** (1 blocking, 8 minor). Machine-readable version: `rules-final.json`.

No line in house rules 1 to 6 is crossed in either piece. The one blocking finding is on the privacy page's accuracy under Bus. & Prof. Code §22575(b)(1).

## Blocking

**1. privacy.md, "The newsletter", paragraph 2: payers' billing details.** The page says Substack "also collects billing details" and "We never see your card number", which reads as if the publisher sees no billing data. Stripe's policy says it shares end customers' name, email and billing address with the business using it, and Substack says billing address and country sit in the publisher's own Stripe account (looked up by subscriber email), with card brand and last four digits visible there. A payer would not learn that the publisher can see their billing address.
Fix: "If you pay on the web, Stripe processes the payment and passes us your name, email address, billing country or address, the card's brand and last four digits, and your payment history. We never see the full card number. If you pay in Substack's iPhone app, Apple processes the payment and we get your email address and payment history, but not your payment method." Confirm each item on a test purchase in the publisher's Stripe dashboard, and add the items to "Who gets your information".

## Minor

2. **privacy.md, "Email you send us": Anthropic.** "Under Anthropic's terms" is true but vague. Consumer plans: training if the setting is on, 5-year retention if allowed, 30 days if not. Commercial plans: no training, 30 days. Name the plan's actual position in one sentence, link Anthropic's and Apple's policies (only Substack's and Stripe's are linked), and give the mail folder a retention period. If the agents run on a consumer plan with training on, this becomes blocking.
3. **privacy.md, "Who gets your information": "we never ask for your income, holdings or tax details".** Literally false, since the calculators ask for exactly that. Say "never receive", and that what you type stays on your device.
4. **privacy.md, Do Not Track bullet and Substack paragraph: §22575(b)(5) and (b)(6) are met only by implication.** Say how the site responds to the signal (the same either way, because it doesn't track), define the term, and say whether the publisher has turned on any of Substack's analytics or ad tracking (Substack's third-party cookies are ones publishers choose to set).
5. **privacy.md, "This site": "GitHub's privacy statement covers that".** GitHub's Pages page says the IP is logged for security and points to the statement; the statement never mentions Pages. Reword to "GitHub's documentation says…".
6. **paid.md, "renews automatically until you cancel".** No term, no price. California's auto-renewal law expects the retained acknowledgment to carry them. Also wrong for comp and gift recipients, and it is unknown whether Substack sends them this email. Use `{{renewal_price}}` and "every year"; check comps and gifts on the test purchase.
7. **paid.md, subject and opening.** Founding buyers from January 5 are welcomed to an edition that opens March 30, and the email doesn't say what happens if it doesn't (the publisher's note leaves that open). Use a founding-member version and add the decision once made.
8. **paid.md, "attached... in the part for paid members".** Substack supports XLSX embeds, but nothing I could reach says a file below the paywall is gated at its own link. Test signed out before January 5.
9. **paid.md, links.** The free welcome, Start here and About all link the privacy page; this email links only the disclaimer. Add it.

## What I confirmed (details in the JSON)

- Rules 1 to 6 hold for both pieces; reader mail is handled per rule 6 (no figures requested, permission before use, no name without written OK).
- Substack: name and email collected and passed to the publisher; billing address and card details collected; Stripe processes cards; third-party cookies; "does not support Do Not Track"; account deletion; activity rating from opens and web views; per-subscriber opens and link clicks; survey answers tied to email in the export.
- Apple: in-app purchase in the iPhone app only, Android cannot buy in-app, publisher gets the email address but not the payment method; cancel through the App Store.
- GitHub: visitor IP logged for security whether or not signed in. Three live github.io sites set no cookies. The built `docs/` has no scripts, forms, embeds or external requests.
- §22575 elements: (b)(2) to (b)(4) present; (b)(1), (b)(5), (b)(6) per findings 1 and 4.
- paid.md against the plan and schedule: March 30, 2027 is a Tuesday (issue 13); first paid issue is April 13 (issue 15); the rest of the offer matches the plan. About 346 words.

## Limits

support.substack.com, leginfo and Justia returned 403 and I did not work around that. The statute came from FindLaw and California Public Law copies; Substack's support articles came through search excerpts. Stripe's and Substack's privacy policies, Substack's in-app-payments FAQ, GitHub's docs and Anthropic's pages were read directly.

Later, not a finding: the plan's anonymous State of Equity Comp survey (June 29, 2027) needs its own line on the privacy page when it opens.

## The one change that helps most

On the privacy page, list exactly what the publisher can see about a payer. In the welcome email, put the renewal term and price in the renewal sentence.
