# Claude.md — SEO Integration Addendum

Append this section to the active Claude.md after the existing Revenue Engine architecture/ownership sections. Do not replace the current Claude.md.

---

# SEO / ORGANIC SEARCH ENGINE

The Revenue Engine includes an SEO / Organic Search capability.

SEO is an acquisition channel within the Revenue Engine, not a separate autonomous business system.

## SEO ownership

SEO Skills own:
- website/search discovery
- technical SEO analysis
- keyword research
- keyword clustering
- page-to-keyword mapping
- content strategy
- content briefs
- SEO content drafts
- internal-link recommendations
- SEO performance analysis

SEO Skills do NOT own:
- Zoho CRM business-process writes
- lead approval
- outbound campaign approval
- pricing
- commercial commitments
- customer claims
- final publication of high-impact website changes

## SEO source of truth

Root context remains authoritative for:
- company
- services
- ICP
- campaigns
- case studies
- competitors
- pricing
- approved claims

SEO-specific interpretation lives under:
`context/seo/`

Do not create conflicting versions of the root business context.

## SEO workflow

RESEARCH
→ ANALYSIS
→ RECOMMENDATION
→ HUMAN APPROVAL
→ IMPLEMENTATION
→ QA
→ PUBLISH
→ MEASURE

## SEO approval

Human approval is required for:
- URL changes
- redirects
- canonical changes
- index/noindex changes
- deleting pages
- major service-page rewrites
- new commercial pages
- publishing new content

## SEO evidence

Never invent:
- search volume
- rankings
- traffic
- customer outcomes
- case studies
- metrics
- certifications
- capabilities

Use CONFIRMED / LIKELY / UNKNOWN.

## SEO CRM boundary

SEO may recommend a future organic-lead-to-CRM integration, but it must not independently write business-process fields to Zoho.

---

## SEO Skills

The SEO module is located at:

`skills/seo/`

Available Skills:
- seo_audit.skill
- keyword_research.skill
- keyword_clustering.skill
- page_optimizer.skill
- content_brief.skill
- seo_content_writer.skill
- internal_linking.skill
- seo_analyst.skill

The first SEO execution must use:

`seo/prompts/initial_discovery.md`

The first run is READ-ONLY and must not modify or publish website changes.
