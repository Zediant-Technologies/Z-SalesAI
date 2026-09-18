# Zediant Revenue Engine — SEO Module

## Purpose

This module adds Organic Search / SEO capability to the existing Zediant Revenue Engine without creating a separate Cowork project.

SEO is an acquisition channel within the Revenue Engine. It shares the existing Zediant business context but keeps SEO strategy, data, audits, content and recommendations isolated from outbound sales execution.

## Ownership

SEO owns:
- website/search discovery
- technical SEO analysis
- keyword research and clustering
- page-to-keyword mapping
- content strategy and briefs
- SEO content drafts
- internal-link recommendations
- SEO performance analysis

SEO does NOT own:
- Zoho CRM business-process writes
- lead approval
- outbound campaign approval
- pricing
- commercial commitments
- customer claims
- final publication of high-impact website changes

## Source of truth

Read the existing root context first:
- context/company.md
- context/services.md
- context/icp.md
- context/campaigns.md
- context/case_studies.md
- context/competitors.md
- context/pricing-public.md

Then read the SEO-specific context under context/seo/.

Do not duplicate or contradict the root business context.

## First run

Run:
seo/prompts/initial_discovery.md

The first run is READ-ONLY. It must not publish, delete, redirect, canonicalize, de-index, or modify the website.

## Approval model

RESEARCH → ANALYSIS → RECOMMENDATION → HUMAN APPROVAL → IMPLEMENTATION → QA → PUBLISH → MEASURE

## Important

Do not assume that a high-volume keyword is valuable.
Prioritize ICP relevance, commercial intent, service relevance, evidence, search opportunity and ranking feasibility.
