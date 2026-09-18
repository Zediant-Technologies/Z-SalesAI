# Batch 1 — Homepage Title & Meta Description Proposal

Status: PREPARED ONLY — NOT DEPLOYED. The live homepage has not been modified.
Date: 2026-08-20
URL: `https://www.zediant.com/`

---

## Live re-check performed today

- **CURRENT TITLE:** "Innovative Digital Solutions for Business Growth - Zediant Technologies" (71 characters)
- **CURRENT META DESCRIPTION:** "Zediant offers cutting-edge digital solutions to drive your business forward. Explore our services in SaaS development, e-commerce, cloud solutions, and more to transform your business." (185 characters)
- **CURRENT H1:** "Your Global AI-Enabled Product Engineering Partner."
- **CURRENT PRIMARY VISIBLE POSITIONING:** The H1 already reflects current positioning (AI-Enabled Product Engineering), but the title and meta description do not — they describe a generic "digital solutions" agency and reference SaaS development, e-commerce, and cloud solutions, none of which are among the four services currently in the top navigation.
- **CURRENT PRIMARY SERVICES (per live top-navigation "Services" dropdown, re-checked today):** AI-enabled Product Engineering; Dedicated Engineering (the confirmed canonical Dedicated Engineering Pods page, `/services/dedicated-engineering/`); Platform Engineering; Enterprise Custom Development. This matches `context/services.md`'s documented four current services and `context/company.md`'s statement that Dedicated Engineering Pods is the primary/preferred delivery model (~90% of billing).

This confirms the same title/meta mismatch already logged in `seo/audits/onpage/initial_onpage_audit.md` §1 and `seo/strategy/p0-implementation-plan.md` §3 is still present and unchanged today.

---

## Proposed replacement

### PROPOSED TITLE

`Dedicated Engineering Pods | AI-Enabled Engineering | Zediant`

**CHARACTER COUNT:** 61 characters (current: 71 characters).

### PROPOSED META DESCRIPTION

`Zediant offers Dedicated Engineering Pods and AI-enabled product engineering. Explore Platform Engineering and Enterprise Custom Development services.`

**CHARACTER COUNT:** 150 characters (current: 185 characters).

---

## SEO RATIONALE

The proposed title leads with Dedicated Engineering Pods — Zediant's primary, revenue-dominant service per `context/company.md` — followed by AI-Enabled Engineering, matching the existing, unflagged H1's positioning ("Your Global AI-Enabled Product Engineering Partner"). Both are now the actual top-of-navigation services rather than the generic "digital solutions" framing the current title uses. The proposed meta description names all four current services in the same priority order as the live navigation (Dedicated Engineering Pods and AI-enabled product engineering first, Platform Engineering and Enterprise Custom Development second), replacing references to SaaS development, e-commerce, and cloud solutions — service names that do not correspond to any current top-navigation item and that this SEO program's own discovery already flagged as stale.

## SEARCH INTENT

The current title/meta target a generic "digital solutions agency" intent, which is broad, high-competition, and does not match what a prospect searching for the company's actual, current, dominant offer (dedicated/pod-based engineering teams, AI-enabled product engineering) would be looking for. The proposed copy targets prospects searching for dedicated engineering teams, staff-augmentation-style pods, or AI-enabled product engineering partners — intent categories that align with `context/icp.md` and the actual revenue mix documented in `context/company.md`.

## CLAIMS CHECK

Per `policies/claims-and-compliance.md`:

- No performance claim (e.g., "30-40% faster") is introduced — the proposed copy names services only, not outcomes.
- No certification/compliance claim (e.g., "SOC 2 Certified") is introduced. SOC 2 wording is out of scope for this document — see `batch-1-soc2-verification.md`, which handles that topic separately and confirms it is a read-only verification, not a rewrite.
- No customer count, headcount, or satisfaction-rate figure is introduced.
- No geography claim (e.g., naming specific countries/offices) is introduced — none appeared in the original title/meta either.
- No new service name is introduced beyond the four already documented in `context/services.md` and currently live in the top navigation. "AI-Enabled Engineering" is a shortened form of the existing, live, unflagged H1 wording ("AI-Enabled Product Engineering"), not a new claim.
- No keyword stuffing — each service name appears exactly once across the title and meta combined; no repeated phrase-stacking.

## RISKS

- **Low technical risk:** a title/meta change is easily reverted and has no structural impact on the site.
- **Low compliance risk:** the proposed copy was checked against `policies/claims-and-compliance.md` and introduces no new claim category; it only reorders/renames already-approved service names.
- **Minor SEO risk:** any metadata change can cause a short-term fluctuation in how a page displays in search results while re-crawled/re-indexed; this is a normal, expected, low-severity effect and not a reason to avoid a demonstrably more accurate title/meta.
- **DATA GAP:** current search ranking/impression data for the existing title/meta is unavailable (no Search Console access), so the precise before/after CTR impact cannot be quantified in advance.

## ROLLBACK VALUE

If reverted, restore the exact current values captured above and already on record verbatim in `seo/data/seo_baseline.csv`:

- Title: `Innovative Digital Solutions for Business Growth - Zediant Technologies`
- Meta description: `Zediant offers cutting-edge digital solutions to drive your business forward. Explore our services in SaaS development, e-commerce, cloud solutions, and more to transform your business.`

---

**No changes have been made to the live homepage.** This is a proposal only, pending human approval.
