# Site pages review (rules lens, facts included)

Pages: `site/disclaimer.md` and `site/privacy.md`, live at https://chauduyphanvu.github.io/paid-in-equity/disclaimer/ and /privacy/. Checked 2026-11-06. No lawyer reviewed either page, and I am not one.

**Verdict: fail. 1 blocking, 11 minor.** The disclaimer covers its four required things and crosses no house rule. The privacy page covers California's six items. It fails on one sentence: its summary says the newsletter keeps only what it needs to email you, and the page itself says otherwise.

## Blocking

**1. `privacy.md`, opening paragraph, second sentence.** "The newsletter keeps only what it needs to email you" is wrong by the page's own account. It also keeps opens, clicks and an activity rating, survey answers, billing details for paying members, and every message a reader sends (some processed by an AI service). A reader who stops at the summary would think only an email address is held. A posted policy that understates collection is what Bus. & Prof. Code §22576 and the FTC's deception rules target.
*Fix:* "In short: the calculators collect nothing. The newsletter collects what Substack and Stripe collect when you subscribe or pay, plus any message you send us; the sections below list it." Better: three lines of who holds what.

## Minor (one line each; full text and evidence in the JSON)

2. `privacy.md`, "Who gets your information": "income, holdings and tax details never reach us" is absolute; a reader can email figures. Say "the calculators never send us ...".
3. `privacy.md`, "The newsletter": the Stripe field list (name, billing address, country, card brand, last four) is not confirmed by any Substack or Stripe page I could open. Substack's FAQ says only that publishers "retain full billing info". Check one real Stripe customer after the first sale and correct the list.
4. `privacy.md`, "The newsletter": "in Substack's iPhone app, Apple does" is incomplete. Apple is always offered there, but U.S. readers can be offered web checkout (Stripe) inside the app. For Apple payments we get the email, not payment details.
5. `privacy.md`, Substack cookies paragraph and Do Not Track bullet (§22575(b)(5), (6)): answered in substance, not plainly. Add one sentence saying other companies may collect on Substack's pages, that Substack does not honor Do Not Track, and what Do Not Track is. Confirm no tracking pixel is on in Substack's settings, then say none was added.
6. `privacy.md`, "Email you send us": "Anthropic's terms" has no link. Anthropic's consumer policy lets it train on inputs unless the account opts out. Link it, check the publisher's account setting, and say what is true.
7. Both pages: nobody is named as "we" or "the publisher", and the disclaimer's only contact route is "reply to any issue" (no issue to reply to for a site-only visitor). Add the contact address to the disclaimer and a line on who runs the newsletter. Confirm `andzrev@pm.me` is where Substack replies go; it appears nowhere else in the project.
8. `disclaimer.md`, "How it's made": "Every figure comes from a primary source" contradicts "made-up pay, grants and tax returns". Say "every tax rule and limit".
9. `disclaimer.md`, "How it's made" and "The calculators" (and `privacy.md` "The calculators"): present tense about calculators that don't exist yet (live index: "The first one arrives with the first issue"; `engine/` is empty). Re-verify with `pie privacy` and the IRS-example tests before November 17.
10. `disclaimer.md`, "No professional relationship": "doesn't predict" is right, but "likely" and the December "look ahead" can read as predictions. Add a sentence that bad, likely and great are what-if scenarios.
11. Both pages, plain English: grade 7.6 and 7.9, so the level is fine. Undefined terms: withholding, alternative minimum tax, IP address, cookies, browser storage, analytics, Do Not Track. Five sentences run past 30 words.
12. `privacy.md`: no stated purpose for survey answers, no retention statement, and nothing yet about the anonymous 2027 reader survey, which needs its own paragraph before June 29, 2027.

## What I confirmed

- **Live matches source.** Both live pages are byte-identical to `docs/*/index.html` and say the same, line for line, as the `.md` sources. The publisher-note comments do not render. HEAD equals origin/main.
- **Links.** All 12 distinct links return 200: corrections log, footer links, Substack subscribe, the public GitHub repo, two GitHub docs pages, Substack and Stripe privacy pages. The mailto is well-formed; I could not test the mailbox.
- **The site's own behavior.** No script, iframe, image, form, import or external font in any of the five built pages. No `Set-Cookie` on any live response. So "no cookies, no tracking, no request after load" holds for the site as built.
- **GitHub:** its Pages docs say the visitor's IP address "is logged and stored for security purposes, regardless of whether the visitor has signed into GitHub or not". Matches.
- **Substack's privacy policy (updated May 14, 2026):** name, email and payment details including billing address; Creators get name and email; Stripe processes card payments; cookies include third-party ones; it may track activity after you leave; it does not support Do Not Track; accounts are deleted from the account page. All match. Its dashboard guide confirms emails received, opened and link clicks.
- **Apple:** Substack's in-app purchase FAQ confirms Apple handles billing for in-app purchases, iOS only.
- **The statute.** §22575(b)(1) to (6) read from the enrolled AB 370 and california.public.law. Each item is covered (see JSON). The footer "Privacy" link on every page, home included, meets "conspicuously post" (§22577(b)(3)(A)).
- **House rules.** The disclaimer has all four required parts. No advice, pick, forecast, provider recommendation, credential or invented person on either page. The five companies are named only as the publisher's own service providers.
- **Reader mail.** `mail/` is gitignored and untracked, so "a private folder" is not in the public repo.

## Not verified

- Substack's help center (`support.substack.com`) returned 403 to my fetches. The activity-rating wording and the billing-country article rest on search excerpts of those pages, and "survey answers are linked to your email" rests on a third-party guide. The statement errs toward over-disclosure.
- That every Substack email carries an unsubscribe link: known Substack behavior, not read from a page.
- CCPA, GDPR and COPPA. The house rules do not require them and I did not assess them.
- The CAN-SPAM mailing address in Substack settings (not on these pages).

## Noticed, outside the two pages

- `pie.json` has `site_url` empty and `launch_setup_done` false. Welcome texts and issue footers that use `{{site_url}}` will have no working disclaimer or privacy link until it is set to https://chauduyphanvu.github.io/paid-in-equity.
- I saw filenames under `welcome/checks/` in a directory listing and `git ls-files`; I opened none of them.

## The one change that would most improve these pages

Rewrite the privacy page's summary as a short "who holds what" list (calculators: nothing; Substack: name, email, opens and clicks, optional survey answers; Stripe or Apple: payment; messages you send). It fixes the blocking finding and is what a non-technical reader would actually read.
