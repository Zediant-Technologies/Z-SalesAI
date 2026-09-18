---
name: seo-seo-audit
description: "Zediant SEO skill for audit."
---

# Skill Contract

## Authority

Read:
1. Claude.md
2. applicable policies/
3. relevant root context/
4. relevant context/seo/ files

Do not override policy or source-of-truth hierarchy.

## Evidence

Use CONFIRMED / LIKELY / UNKNOWN.
Never invent facts, metrics, customers or capabilities.

## Scope

This skill does not independently write business-process fields to Zoho CRM.

## Approval

High-impact website changes require HUMAN APPROVAL before implementation/publication.

## Failure behavior

Use DATA GAP, DATA CONFLICT, POLICY BLOCK or HUMAN APPROVAL REQUIRED where appropriate.

# SEO Audit Skill

## Purpose

Perform a read-only SEO audit of the Zediant website.

## Responsibilities

Evaluate:
- crawlability
- indexability
- robots.txt
- XML sitemap
- canonical URLs
- redirects
- broken links
- 404s
- duplicate URLs/content
- title tags
- meta descriptions
- heading hierarchy
- structured data
- image alt text
- internal links
- page speed / Core Web Vitals where measurable
- mobile usability
- HTTPS
- URL structure
- content quality
- conversion relevance

## Procedure

1. Discover the website and page inventory.
2. Collect observable evidence.
3. Separate technical, on-page, content and conversion findings.
4. Identify severity.
5. Identify implementation effort.
6. Recommend next action.

## Output

Finding
URL
Evidence
SEO Impact
Business Impact
Recommendation
Priority
Effort
Approval Required

## Critical rule

This is a read-only audit unless a separate approved implementation task is explicitly provided.
