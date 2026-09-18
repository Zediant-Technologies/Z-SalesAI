# Standardizing CTA Phrasing — Enterprise Custom Development Page
**Fix for:** "CTA phrasing — still not standardized" (P1, from the re-audit)
**Goal:** Replace four different button phrasings with one consistent phrase, sitewide button-style pattern.

---

## Step 1: Confirm the target phrase

**Recommended:** "Talk to Our Enterprise Engineering Team"

Why this one specifically, not just any of the four already in use:
- It matches the "Talk to Our Engineering Team" pattern already standardized on the other service pages (AI-Enabled Product Engineering, Dedicated Engineering Pods), so it's consistent sitewide, not just on this page.
- "Enterprise" keeps this page's specific positioning (vs. a generic "Talk to our team") — it doesn't just copy the other pages' button verbatim, it signals this page's audience.
- "Talk to" reads as lower-friction and more conversational than "Consult with" or "Discuss," which sound more formal/higher-commitment — better fit for a first click.

If you'd rather keep the more formal "Consult with" register (some enterprise buyers respond better to it), the same fix works with **"Consult With Our Enterprise Engineering Team"** instead — the important part is picking one and using it everywhere, not which exact verb you land on.

---

## Step 2: Locate every CTA instance on the page

Four buttons currently carry different text for the same action (get in touch / start a conversation). In your CMS/page builder, find and open each of these:

| # | Location | Current text |
|---|---|---|
| 1 | Hero section | "Consult with our Enterprise Team" |
| 2 | "Discuss Your Enterprise Engineering Needs" CTA block (after the Challenges/Build-or-Modernize sections) | "Discuss Your Enterprise Project" |
| 3 | Same CTA block, second button | "Consult with Our Engineering Experts" |
| 4 | Contact form submit button | "Talk to our engineering team" |

Note: the hero's second button, "View Case Studies & Success Stories," is a *different action* (browsing proof, not contacting sales) — leave that one as-is. Same for "Read Wholesale Parts CRM Case Study" / "Read Lubricant Recommendation Case Study" / "View all case studies" links in the case-studies section — those aren't contact CTAs either.

---

## Step 3: Edit each button's label field

For buttons #1, #2, and #3 above: this is a plain text/label edit — find the button element in your page builder and change only its visible label text, not its link/destination. After editing, confirm each button still points to the same place it did before (usually the contact form anchor or a booking link) — you're changing what the button says, not where it goes.

- Button #1 (hero) → change to: **"Talk to Our Enterprise Engineering Team"**
- Button #2 (CTA block) → change to: **"Talk to Our Enterprise Engineering Team"**
- Button #3 (CTA block, second button) → this one's worth a decision rather than a straight rename, since having two buttons side-by-side with identical text reads oddly. Two options:
  - Remove it entirely, since it duplicates button #2's action with no real difference between "Discuss Your Enterprise Project" and "Consult with Our Engineering Experts" — one clear CTA per block is usually stronger than two competing ones.
  - Or, if you want to keep two buttons in that block on purpose (e.g., one for "talk to sales," one for "book a technical consult"), keep the text different but make each one specific about what it actually leads to, rather than two generic variations on the same phrase.

---

## Step 4: Handle the contact form button separately

Button #4 ("Talk to our engineering team," capitalization aside) is very close to the target phrase already — it's missing "Enterprise." If this button is a shared/reused component across other service pages (worth checking, since the "Candidate Selection" form label turned out to be exactly this kind of shared component elsewhere on the site), don't rename it here in isolation — check whether the same submit button appears on the other three service pages first.

- If it's page-specific: change it to match — **"Talk to Our Enterprise Engineering Team"**.
- If it's a shared component used on all four service pages: renaming it here would change it everywhere, which may not be what you want (the other pages may want their own contextual version, e.g. "Talk to Our Platform Engineering Team" on the Platform Engineering page, which — worth noting — is already exactly what that page's hero button says). In that case, this becomes a slightly bigger decision: either make the submit button page-aware (different label per page, if your form tool supports that), or accept one neutral phrase across all forms sitewide (e.g., just "Talk to Our Engineering Team," dropping "Enterprise" everywhere so it works as a shared default).

---

## Step 5: Preview and verify

After the edits:
1. Reload the live page and visually confirm all three (or two, if you removed the duplicate) contact-intent buttons read identically.
2. Click through each one and confirm it still lands on the correct destination (contact form / anchor link).
3. Check mobile view — button text length differences can affect wrapping on smaller screens; "Talk to Our Enterprise Engineering Team" is a few characters longer than the current shortest option ("Discuss Your Enterprise Project"), so it's worth a quick mobile check after the change.

---

## Suggested order

1. Step 1 — pick the final phrase (two minutes, your call).
2. Step 3, buttons #1 and #2 — quick, low-risk text edits.
3. Step 3, button #3 — the one judgment call (remove vs. differentiate); decide once you can see the page with #1 and #2 already updated.
4. Step 4 — check whether the form button is shared before touching it.
5. Step 5 — verify everything, including mobile.
