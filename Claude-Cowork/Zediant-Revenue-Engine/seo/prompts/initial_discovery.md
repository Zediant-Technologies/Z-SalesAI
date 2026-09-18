# Initial SEO Discovery — READ ONLY

## Objective

Establish a factual baseline for Zediant SEO before any website changes or content creation.

## Hard constraint

READ-ONLY.

Do not:
- publish
- edit website pages
- delete pages
- create redirects
- change canonicals
- change index/noindex
- alter robots.txt
- alter sitemap
- create content for publication

## Step 1 — Read Zediant context

Read Claude.md, policies/, and all relevant root context files.

Pay particular attention to:
- services.md
- icp.md
- company.md
- campaigns.md
- case_studies.md
- competitors.md

## Step 2 — Discover website

Crawl/discover the public Zediant website and build a page inventory.

Record:
URL
Page Type
Title
Meta Description
H1
Indexability
Canonical
Status Code
Primary Topic
Observed Search Intent
CTA
Internal Links
Content Quality Notes

## Step 3 — Technical baseline

Check:
- robots.txt
- sitemap
- indexability
- canonicals
- redirects
- broken links
- 404s
- duplicate URLs
- duplicate/thin content
- structured data
- mobile issues
- page speed/Core Web Vitals where measurable
- HTTPS

## Step 4 — Existing content baseline

Classify existing pages:
- homepage
- service
- solution
- industry
- location
- case study
- blog/resource
- other

Identify:
- strong pages
- weak pages
- missing commercial pages
- thin pages
- overlapping pages
- orphan pages

## Step 5 — Search visibility baseline

Use available search/ranking sources.

Do not fabricate:
- search volume
- rankings
- traffic
- CTR
- impressions

Mark unavailable metrics UNKNOWN.

## Step 6 — Competitor discovery

Identify relevant search competitors based on actual SERPs and Zediant's target services.

Do not assume that every business competitor is an SEO competitor.

Record:
Competitor
Relevant SERP/topic
Observed strength
Content gap
Service gap
Potential opportunity

## Step 7 — Initial keyword universe

Create a preliminary keyword set around validated Zediant services and buyer problems.

Classify:
- intent
- buyer stage
- ICP relevance
- commercial intent
- service relevance
- geography

Do not create articles yet.

## Step 8 — Prioritized backlog

Create P0/P1/P2/P3 recommendations.

P0 = critical technical/indexation or high-value commercial issue.
P1 = high-value service/search opportunity.
P2 = meaningful optimization/content opportunity.
P3 = lower-impact enhancement.

## Final deliverables

Create/update:
- seo/data/seo_baseline.csv
- seo/data/content_inventory.csv
- seo/audits/technical/initial_technical_audit.md
- seo/audits/onpage/initial_onpage_audit.md
- seo/audits/content/initial_content_audit.md
- seo/audits/competitor/initial_competitor_audit.md
- seo/strategy/seo_priorities.md

At the end, provide a concise executive summary and explicitly list all DATA GAPs and HUMAN APPROVAL REQUIRED items.
