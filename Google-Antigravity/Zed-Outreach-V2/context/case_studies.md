# Zediant Case Studies

## Case Study Governance

This document is the current, authoritative case-study context for the Zediant Revenue Engine. It supersedes `migration/original-source/case_studies.md`, which is historical source material and must never be treated as current operating truth on its own. Current policy (`Claude.md`, `policies/*.md`) and the explicit human decisions recorded in this file's migration override any conflicting historical content.

Governing rules applied throughout this file:

- Case studies may only be used externally according to their documented **Customer Disclosure Status** and **External Use Approval** — a customer being nameable does not automatically mean the entire case study is approved for external use.
- Published metrics are used exactly as documented. No metric has been rounded, improved, extrapolated, reinterpreted, or combined.
- No case study, capability, or outcome has been invented, inferred, or strengthened beyond what the historical source documented.
- **CS-02 and CS-06 are the same customer/account.** They must never be presented as two separate customers and must never be used together as separate proof points in the same prospect conversation.
- **C1 — AI-Enabled Product Engineering currently has no approved case study.** This is an intentional, documented evidence gap, not an oversight.
- Campaign associations are evidence-based — grounded in each case study's documented business problem, technical need, and service delivered — never assigned by industry alone or by campaign portfolio weighting.
- The current outbound platform is Apollo. No historical outbound-platform configuration, sequence IDs, or campaign IDs appear anywhere in this file.

---

## Case Study Index

| ID | Case Study | Customer Disclosure | External Use Approval | Primary Campaign | Secondary Campaign | Status |
|---|---|---|---|---|---|---|
| CS-01 | Middleware Integration for Multiple Large DMS | ANONYMISED | HUMAN APPROVAL REQUIRED | C4 | — | HUMAN APPROVAL REQUIRED |
| CS-02 | Wholesale Parts CRM for Automotive Dealers and OEMs | ANONYMISED | HUMAN APPROVAL REQUIRED | C2 | C4 | HUMAN APPROVAL REQUIRED |
| CS-03 | Lubricant Recommendation & Equipment Maintenance Application | ANONYMISED | HUMAN APPROVAL REQUIRED | C2 | C4 | HUMAN APPROVAL REQUIRED |
| CS-04 | 11Wickets Scalability & Performance Optimisation | NAMED | HUMAN APPROVAL REQUIRED | C3 | — | HUMAN APPROVAL REQUIRED |
| CS-05 | Real-Time Executive Dashboards (Diamond Professional Consultants / Zakaa Innovation Hub) | NAMED | HUMAN APPROVAL REQUIRED | C4 | — | HUMAN APPROVAL REQUIRED |
| CS-06 | Team Augmentation for Automotive Software | ANONYMISED | HUMAN APPROVAL REQUIRED | C2 | C3 | HUMAN APPROVAL REQUIRED |
| CS-07 | Cryptocurrency Trading Application | ANONYMISED | HUMAN APPROVAL REQUIRED | C2 | — | HUMAN APPROVAL REQUIRED |
| CS-08 | Sitecore CMS Multisite Platform | ANONYMISED | HUMAN APPROVAL REQUIRED | C2 | C4 | HUMAN APPROVAL REQUIRED |
| CS-09 | BigCommerce Integration for Australia's Largest Office Supply Brand | ANONYMISED | HUMAN APPROVAL REQUIRED | C2 | — | HUMAN APPROVAL REQUIRED |
| CS-10 | WordPress Migration for an Online Poker Platform | ANONYMISED | HUMAN APPROVAL REQUIRED | C2 | — | HUMAN APPROVAL REQUIRED |

Every case study is marked `External Use Approval: HUMAN APPROVAL REQUIRED`. This is deliberate: the historical source documents naming/anonymity status but does not document a separate, explicit "approved for external use" determination for any entry — including the two named clients — as current policy (`policies/confidentiality.md` §4) requires. Naming permission is not full external-use approval.

**How this gate is satisfied (confirmed, September 2026).** A case study drafted into a lead's `Case_Study` field by `email-personalization` is not itself an external send — it sits in Zoho awaiting BDM review, same as every other personalization field. The existing BDM approval gate (moving `Lead_Status` to `Approved for Outreach`) is the human approval this section requires; a separate, standalone case-study sign-off step does not exist and is not needed. This does not relax anything about which facts may be used (still only what's documented above, never invented or strengthened) — it clarifies which human action satisfies `HUMAN APPROVAL REQUIRED` before a case study reaches a prospect.

---

## C1 Evidence Gap

**C1 — AI-Enabled Product Engineering currently has NO approved case study.**

This is confirmed, current, and intentional:

- No existing case study demonstrates AI-Enabled Product Engineering as its dominant, documented business problem or technical need.
- CS-04 (11Wickets) and CS-07 (Cryptocurrency Trading Application) are **not** assigned to C1. Their documented business problems are infrastructure scaling (CS-04 → C3) and secure mobile application delivery (CS-07 → C2), respectively. Neither demonstrates AI-Enabled Product Engineering.
- No case study is invented, reinterpreted, or manufactured to fill this gap.
- Previous campaign-mapping discrepancy resolved: `context/campaigns.md` has been corrected and no longer associates CS-04 or CS-07 with C1. C1 remains without an approved case study.
- A future, genuinely evidenced C1 case study can be added later. Until then, any prospect conversation requiring AI-Enabled Product Engineering proof should state plainly that no case study currently exists rather than substitute a different engagement.

---

## CS-02 / CS-06 Customer Identity Restriction

CS-02 and CS-06 are confirmed to represent the same customer/account (a global provider of SaaS and DaaS solutions for data-driven automobiles, operating in 186 countries with 50 OEM manufacturers and 250,000+ industry professionals).

Therefore:

- Never present CS-02 and CS-06 as two separate customers.
- Never use CS-02 and CS-06 together as separate proof points in the same prospect conversation, email, or proposal.
- The system may select **either** CS-02 **or** CS-06, based on which one's documented business problem best matches the prospect — CS-02 for CRM/dealer-facing mobile application evidence, CS-06 for staff augmentation/legacy-acquisition/test-coverage evidence.
- Do not claim customer diversity based on both studies appearing in Zediant's portfolio.

---

## CS-01 — Middleware Integration for Multiple Large DMS

### Customer
Anonymised — a leading automotive parts dealer's customised CRM product, serving dealers across APAC, UK, and USA.

### Customer Disclosure Status
ANONYMISED

### Confidentiality Classification
UNKNOWN — historical source classifies this as "Tier 3 — never name," which restricts naming but has not been mapped through the current PUBLIC/INTERNAL/CONFIDENTIAL/CUSTOMER-CONFIDENTIAL/RESTRICTED framework. Do not assume PUBLIC.

### External Use Approval
HUMAN APPROVAL REQUIRED

### Business Problem
The client's CRM product needed to serve dealers running different, incompatible dealer management systems (DMS). Customer and sales data sat siloed in each DMS with no path between them, so the CRM could not present a complete picture to sales representatives.

### Business Challenge
Data siloed across multiple heterogeneous DMS platforms (ERA, CDK, Pentana), no common data model across source systems, manual data entry consuming time and introducing errors, and no cross-network visibility into sales performance.

### Solution
Zediant Middleware — an integration layer between the DMS platforms and the CRM, standardising, enriching, and validating data in real time. An adapter pattern per source system was used so the solution could extend to additional dealers and DMS platforms without a bespoke rebuild each time.

### Services Delivered
Integration & Middleware Engineering; Enterprise Custom Development; Platform Architecture & System Design.

### Technology
Java, Spring, EJB, JMS, ActiveMQ, JAX-RS, REST, NoSQL, AngularJS, HTML5, CSS.

### Documented Outcomes
Qualitative only: improved data quality through standardisation/enrichment/validation; increased cross-network sales visibility; manual data entry eliminated between DMS and CRM; the solution became a repeatable, productised offering adopted across dealers in APAC, UK, and USA.

### Documented Metrics
No published metric. The historical source explicitly states no percentage figures are published for this engagement and instructs that none be invented.

### Evidence Status
DATA GAP — evidence provenance not explicitly documented (no metrics exist to trace, and no source is cited for the qualitative outcomes beyond the engagement narrative itself).

### Campaign Fit
The documented business problem — multiple systems that do not exchange data, requiring an integration/middleware layer — matches C4's defined business problem (systems not exchanging data; DMS/ERP/CRM/POS integration) directly, independent of the automotive industry context.

### Campaign Association
C4

### External Usage Restrictions
Never name the client. Describe only by category (e.g., "a leading automotive parts dealer's CRM product"). Do not attach any capability or metric not documented above.

### Internal Notes
*(Internal only — not for customer-facing use.)* Team composition and project timeline are not published. The historical source offers only an internal, non-published assumption (architect, 3–5 backend engineers, QA, PM; 6–12 months) based on comparable engagements — this must not be quoted externally as fact.

### Status
HUMAN APPROVAL REQUIRED

---

## CS-02 — Wholesale Parts CRM for Automotive Dealers and OEMs

### Customer
Anonymised — a global provider of SaaS and DaaS solutions for data-driven automobiles, with client software used in 186 countries by 50 OEM manufacturers and 250,000+ industry professionals. **This is the same customer/account as CS-06** — see the CS-02/CS-06 restriction above.

### Customer Disclosure Status
ANONYMISED

### Confidentiality Classification
UNKNOWN — historical "Tier 3 — never name," not yet mapped to the current classification framework.

### External Use Approval
HUMAN APPROVAL REQUIRED

### Business Problem
The client had a strong automotive SaaS/DaaS product suite but no CRM for dealers to manage sales and service representative activity, degrading the customer experience the platform was meant to deliver.

### Business Challenge
Repetitive manual rep tasks, poor inter-departmental collaboration, no real-time analytics on sales performance or customer behaviour, and sales/customer data locked inside heterogeneous dealer DMS platforms.

### Solution
An iPad-first CRM for field sales reps — lead and customer management, task and issue management, and analytics — supported by a middleware layer importing sales and customer data from dealer DMS platforms and generating statistics, reports, and projections. The engagement began with a transformational roadmap before development.

### Services Delivered
Design; Development; Quality Assurance; Project Management; Integration & Middleware Engineering; Advisory (transformational roadmap).

### Technology
Objective-C, Swift (iPad); .NET, C#; MS SQL Server; LINQ; jQuery, AngularJS, HTML5, CSS; middleware integration to dealer DMS platforms.

### Documented Outcomes
Qualitative: improved sales productivity, real-time analytics for dealers, centralised data for managers, improved customer experience.

### Documented Metrics
**50+ dealers** across APAC using the platform. **5,700 customers** served through it. Client scale context (not a Zediant-caused outcome metric, but a documented figure describing the client's own business): the client's software runs in **186 countries with 50 OEM manufacturers and 250,000+ industry professionals**. Team: 12 people. Duration: 18 months, Time & Material.

### Evidence Status
DATA GAP — evidence provenance not explicitly documented (no source is cited confirming how the dealer/customer counts were measured or verified).

### Campaign Fit
The dominant engagement shape is a 12-person, 18-month embedded team building and owning a CRM product — direct evidence for C2 (Engineering Pods & Staff Augmentation). The engagement also included a genuine middleware layer importing data from dealer DMS platforms, which is direct technical evidence for C4 (Middleware & API Integration).

### Campaign Association
C2 (primary), C4 (secondary)

### External Usage Restrictions
Never name the client. Never present CS-02 as a separate customer from CS-06, and never use both in the same conversation. Do not use the client-scale figures (186 countries / 50 OEMs / 250,000+ professionals) to imply anything about Zediant's own scale — they describe the client's business, not Zediant's.

### Internal Notes
*(Internal only.)* Exact per-role split of the 12-person team is not published.

### Status
HUMAN APPROVAL REQUIRED

---

## CS-03 — Lubricant Recommendation & Equipment Maintenance Application

### Customer
Anonymised — a leading automotive technology company in APAC, partnered with premium lubricant suppliers.

### Customer Disclosure Status
ANONYMISED

### Confidentiality Classification
UNKNOWN — historical "Tier 3 — never name," not yet mapped to the current classification framework.

### External Use Approval
HUMAN APPROVAL REQUIRED

### Business Problem
Determining the correct lubricant for a given piece of engine equipment depended on frequently changing specifications managed on paper — slow, error-prone, and not scalable across suppliers.

### Business Challenge
Manual, paper-based specification management; frequent specification changes with no reliable propagation; non-technical stakeholders unable to determine correct products; no scalable way to serve multiple lubricant suppliers from one platform.

### Solution
A web-based application automating lubricant recommendation, integrated with premium supplier databases and complex vehicle specifications, on a centralised database. The recommendation engine was exposed as an API consumed by both web and mobile clients across different suppliers.

### Services Delivered
Design; Development; Quality Assurance; Project Management.

### Technology
JSP, Spring, Hibernate; MS SQL; Objective-C, Swift, Ionic; AngularJS, HTML5, CSS.

### Documented Outcomes
Qualitative: cost savings for the client, an environmentally beneficial outcome from correct lubricant selection, and growing demand from additional lubricant suppliers.

### Documented Metrics
**23+ leading lubricant companies in APAC** using the application. Team: 8 people. Duration: 10 months, Time & Material.

### Evidence Status
DATA GAP — evidence provenance not explicitly documented.

### Campaign Fit
The core build (web/mobile application delivered by a design/development/QA/PM team) is the type of engagement `context/campaigns.md` routes to C2 by default in the absence of a dedicated campaign. The engagement also required direct integration with multiple premium lubricant supplier databases — genuine technical evidence for C4.

### Campaign Association
C2 (primary), C4 (secondary)

### External Usage Restrictions
Never name the client. **Do not use the "10-month UAE project" reference as a delivery-speed proof point.** Internal strategy material references a "10-month UAE project" in the context of delivery delays and the need for stricter delay clauses; it is not confirmed whether this is the same engagement as CS-03. Treat this project's timeline as unconfirmed for speed-related claims until resolved.

### Internal Notes
*(Internal only.)* DATA GAP — the possible link between this engagement and the internally-referenced "10-month UAE project" delay example remains unresolved and requires human confirmation before CS-03 is used in any timeline- or delivery-speed-related messaging.

### Status
HUMAN APPROVAL REQUIRED

---

## CS-04 — 11Wickets Scalability & Performance Optimisation

### Customer
**11Wickets** — a fantasy cricket platform based in India.

### Customer Disclosure Status
NAMED

### Confidentiality Classification
UNKNOWN — historical source states "Tier 1 — safe to name, published on zediant.com." Naming permission is documented; a full current-framework classification (e.g., PUBLIC) has not been separately confirmed for every detail in this entry.

### External Use Approval
HUMAN APPROVAL REQUIRED — naming permission is documented, but full-content external-use approval (which specific details/metrics are cleared) has not been separately established, per current policy.

### Business Problem
11Wickets' user base was growing faster than its infrastructure could support. Concurrent load and high write volume for game stats and results were producing slow performance and downtime.

### Business Challenge
Infrastructure not horizontally scalable; a single-node MySQL database becoming a bottleneck under write-heavy load; increased response times under concurrency; no high availability tolerant of node failure.

### Solution
A horizontally scalable AWS architecture — EC2, Auto Scaling, and Elastic Load Balancing — paired with a MySQL Galera cluster distributing write operations across multiple nodes with automatic failover.

### Services Delivered
Platform Engineering & Cloud DevOps; Advisory (architecture and performance assessment).

### Technology
AWS (EC2, Auto Scaling Groups, Elastic Load Balancing); MySQL, Galera Cluster.

### Documented Outcomes
Qualitative only: the platform could handle increasing concurrent users, a smoother and faster user experience, and stable service during a growth period.

### Documented Metrics
No published metric. The historical source explicitly states no percentage figures, user counts, or uptime numbers are published, and explicitly instructs that the "99.99% availability" claim published elsewhere on Zediant's site must **not** be attached to this engagement.

### Evidence Status
DATA GAP — evidence provenance not explicitly documented.

### Campaign Fit
The documented business problem — infrastructure not horizontally scalable, database bottleneck under write load, need for high availability — is a direct, exact match to C3's defined business problems (deployment, reliability, scaling, cloud cost). This is evidence-based on the technical work performed, not on the gaming industry.

### Campaign Association
C3

### External Usage Restrictions
Client name and the fact of the engagement are documented as safe to use. Never attach the unsupported "99.99% availability" claim, or any other unsupported metric, to this engagement.

### Internal Notes
*(Internal only.)* Team composition and project timeline are not published; do not state either externally.

### Status
HUMAN APPROVAL REQUIRED

---

## CS-05 — Real-Time Executive Dashboards (Diamond Professional Consultants / Zakaa Innovation Hub)

### Customer
**Diamond Professional Consultants** — a UAE-based consultancy specialising in performance management and data analytics, delivering the **Zakaa Innovation Hub** product to its own clients. This customer identity is confirmed.

### Customer Disclosure Status
NAMED

### Confidentiality Classification
UNKNOWN — historical source states "Tier 1 — named publicly by Zediant." Naming permission is documented; a full current-framework classification has not been separately confirmed for every detail in this entry.

### External Use Approval
HUMAN APPROVAL REQUIRED

### Business Problem
Senior leadership at the client needed a consolidated, real-time view of KPIs spanning multiple enterprise systems. Reporting was fragmented and largely manual, limiting timely, data-driven decision-making.

### Business Challenge
KPI reporting fragmented across multiple enterprise systems; manual, slow reporting; no single source of truth for management reporting; no role-based control over who could see which data.

### Solution
A secure, enterprise-grade management dashboard integrating data from multiple internal systems into a unified reporting layer, with role-based access control and a modular, integration-ready design for future data sources.

### Services Delivered
Architecture Design; Dashboard Development; Data Integration; Quality Assurance.

### Technology
Python; Oracle; ReactJS; REST APIs.

### Documented Outcomes
Qualitative only: unified visibility of enterprise KPIs, faster and more informed management decisions, reduced manual reporting effort, improved data accuracy, and a scalable foundation for advanced analytics.

### Documented Metrics
No published metric. Team: 6 people. Duration: 6 months, Time & Material.

### Evidence Status
DATA GAP — evidence provenance not explicitly documented.

### Campaign Fit
The documented business problem is data integration from multiple internal systems into a unified reporting layer — direct technical evidence for C4 (Middleware & API Integration). No genuine, independent evidence supports any other campaign association for this engagement; industry/channel framing is not used as the basis for campaign fit.

### Campaign Association
C4

### External Usage Restrictions
**Customer identity is confirmed as Diamond Professional Consultants / Zakaa Innovation Hub. Do not describe this customer as an Oil & Gas company, and do not create an Energy/Oil & Gas industry association for this case study.** An earlier version of this record carried an unresolved discrepancy suggesting a possible Oil & Gas end-client reading; that reading is not retained here and must not be reintroduced.

### Internal Notes
*(Internal only.)* The historical source's conditional secondary association of this engagement with C2 (framed as a "consultancy/channel-aggregator" reading) was explicitly tied to the now-rejected Oil & Gas interpretation and is therefore not carried forward as a campaign association in this file.

### Status
HUMAN APPROVAL REQUIRED

---

## CS-06 — Team Augmentation for Automotive Software

### Customer
Anonymised — a top international provider of SaaS and DaaS solutions for data-driven automobiles, operating in 186 countries with 50 OEM manufacturers and 250,000+ industry professionals. **This is the same customer/account as CS-02** — see the CS-02/CS-06 restriction above.

### Customer Disclosure Status
ANONYMISED

### Confidentiality Classification
UNKNOWN — historical "Tier 3 — never name," not yet mapped to the current classification framework.

### External Use Approval
HUMAN APPROVAL REQUIRED

### Business Problem
The client ran multiple internal development teams but lacked in-house expertise for a recently acquired customer relationship software product, and needed experienced developers to take long-term ownership of continuously changing requirements.

### Business Challenge
No in-house expertise for a newly acquired, undocumented software product; no dedicated testing team; no staging environment; no disaster recovery or failover capability; no internal mobile capability; strict security requirements.

### Solution
An embedded team that began with infrastructure and knowledge recovery — reverse-engineering the acquired software and delivering a developer's manual within one month — before feature work. Zediant built AWS-powered backup and disaster recovery, established a staging environment, raised test coverage, and then delivered continuing feature development (rep tracking, performance evaluation, automated invoice integration, predictive sales forecasting, and more) under a two-week Agile sprint cadence.

### Services Delivered
Staff Augmentation; Dedicated Engineering Pods; Platform Engineering & Cloud DevOps; QA & Test Automation; Mobile Application Development; Legacy/Acquired Code Modernisation.

### Technology
Objective-C, Swift (mobile); .NET, Entity Framework; Angular, SignalR; Microsoft SQL Server; AWS; CircleCI.

### Documented Outcomes
Qualitative: fail-safe continuous delivery of new features enabled; DevOps practices introduced to a project that had none; institutional knowledge recovered and documented rather than lost; continuing 3+ year relationship.

### Documented Metrics
**Test coverage raised from 70% to 93%.** Developer's manual delivered within **1 month** of engagement start. Relationship duration: **3+ years and continuing**. Client scale context (shared with CS-02, same account): the client's software runs in 186 countries with 50 OEM manufacturers and 250,000+ industry professionals.

### Evidence Status
DATA GAP — evidence provenance not explicitly documented (no source is cited for how the 70%→93% coverage figure was measured or verified, though the figure itself is preserved exactly as documented).

### Campaign Fit
The dominant, documented engagement shape is an embedded, long-term staff augmentation team taking ownership of a client's product — direct evidence for C2. The engagement also introduced DevOps practices, CI/CD via CircleCI, and AWS backup/disaster recovery — genuine documented technical work supporting a secondary C3 association (deployment reliability, automation, observability infrastructure), independent of industry.

### Campaign Association
C2 (primary), C3 (secondary)

### External Usage Restrictions
Never name the client. Never present CS-06 as a separate customer from CS-02, and never use both in the same conversation.

### Internal Notes
*(Internal only.)* **Historical C5 mapping conflict resolved.** An earlier version of `context/campaigns.md` listed CS-06 as a related case study for C5 (Enterprise Custom Development & Modernization) as well; that association was never independently supported by CS-06's own documented business problem/technical need in the historical source and is not carried forward here. `context/campaigns.md` no longer lists any case study for C5 — see the Campaign-to-Case-Study Mapping note for C5 below. Exact per-role team count is not published; only "project managers" and "multiple developers" are documented, with no QA role on the project (developers wrote the tests).

### Status
HUMAN APPROVAL REQUIRED

---

## CS-07 — Cryptocurrency Trading Application

### Customer
Anonymised — a consumer fintech platform; country and company size not published.

### Customer Disclosure Status
ANONYMISED

### Confidentiality Classification
UNKNOWN — historical "Tier 3 — never name," not yet mapped to the current classification framework.

### External Use Approval
HUMAN APPROVAL REQUIRED

### Business Problem
The client needed a secure, user-friendly cryptocurrency application to attract and retain customers in a market where trust and usability determine adoption.

### Business Challenge
Securing transactions in a low-trust market category; delivering an intuitive interface to non-expert users; supporting a wide range of digital currencies; demonstrating security credibly to prospective users.

### Solution
A cross-platform application built with Ionic, using multi-factor authentication and end-to-end encryption. Features included multi-exchange integration, real-time transaction processing, one-time and recurring investment plans, and real-time price comparison across exchanges.

### Services Delivered
Design; Development; Quality Assurance; Project Management.

### Technology
Ionic, Angular; .NET, C#; MS SQL Server; jQuery, HTML5, CSS; multi-factor authentication, end-to-end encryption.

### Documented Outcomes
Qualitative: a credible, secure product in a trust-sensitive category, delivered fixed-price by a small team; users could compare prices across exchanges and transact in multiple currencies in a single transaction.

### Documented Metrics
**4.9 rating on Google Play. 4.4 rating on the App Store.** Independent third-party security audit approval obtained. Team: 3 people. Duration: 5 months, Fixed Price.

### Evidence Status
DATA GAP — evidence provenance not explicitly documented (app-store ratings are attributable to the named platforms at the time of the historical source, but no verification date or source link is documented here).

### Campaign Fit
This is a discrete mobile application build delivered by a small design/development/QA/PM team. Mobile Application Development has no dedicated campaign under `context/campaigns.md` and is explicitly routed to C2 by default. This is not a C1 association — the engagement demonstrates secure mobile application delivery, not AI-Enabled Product Engineering, and is not assigned to C1 despite C1's current evidence gap.

### Campaign Association
C2

### External Usage Restrictions
Never name the client. **Escalate any SOC 2 attestation question rather than answering it directly**, even though this case study's own independent security-audit narrative makes such questions likely to arise naturally in conversation.

### Internal Notes
*(Internal only.)* No documented information on challenges during delivery; any such content would be an unconfirmed assumption and is excluded.

### Status
HUMAN APPROVAL REQUIRED

---

## CS-08 — Sitecore CMS Multisite Platform

### Customer
Anonymised — a top manufacturer of material handling equipment, Australia, with country-specific sites across multiple regions.

### Customer Disclosure Status
ANONYMISED

### Confidentiality Classification
UNKNOWN — historical "Tier 3 — never name," not yet mapped to the current classification framework.

### External Use Approval
HUMAN APPROVAL REQUIRED

### Business Problem
The manufacturer needed a content management system for its country-specific websites that maintained global branding while supporting multiple languages, geography-based personalisation, and synchronisation with Salesforce to track user behaviour.

### Business Challenge
Country-specific sites inconsistent with global branding; multiple languages requiring management; no personalisation by geography or behaviour; user behaviour and leads not reaching Salesforce without manual work; no standardised security across sites.

### Solution
A Sitecore-based multisite platform, architected with the client's future e-commerce plans in view. Delivered behavioural/geographic personalisation, bidirectional Salesforce synchronisation removing manual lead handoff, and built-in marketing automation.

### Services Delivered
Design; Development; Quality Assurance; Project Management.

### Technology
Sitecore; .NET, C#; MS SQL; jQuery, HTML5, CSS; AWS; Salesforce integration.

### Documented Outcomes
Qualitative: content managed in-house by marketing without developer dependency; better data-driven analytics; a stated foundation for continued digital growth.

### Documented Metrics
**30% increase in website traffic** (documented as "company-stated"). Team: 5 people. Duration: 6 months, Fixed Price.

### Evidence Status
DATA GAP — evidence provenance not explicitly documented. The 30% traffic figure is preserved exactly as documented and exactly as labeled ("company-stated"); its underlying measurement source is not documented.

### Campaign Fit
The core CMS build (design/development/QA/PM delivering a content platform) is routed to C2 by default under `context/campaigns.md`'s "delivered within a pod" logic for services without a dedicated campaign. The engagement also included genuine, documented bidirectional Salesforce integration — direct technical evidence for a secondary C4 association.

### Campaign Association
C2 (primary), C4 (secondary)

### External Usage Restrictions
Never name the client. Describe only by category (e.g., "an Australian material handling manufacturer"). Preserve the 30% traffic figure exactly as documented, including its "company-stated" qualifier — do not present it as independently verified.

### Internal Notes
*(Internal only.)* **Historical C5 mapping conflict resolved.** An earlier version of `context/campaigns.md` listed CS-08 as a related case study for C5 as well; that association was never independently supported by CS-08's own documented business problem/technical need in the historical source and is not carried forward here. `context/campaigns.md` no longer lists any case study for C5 — see the Campaign-to-Case-Study Mapping note for C5 below.

### Status
HUMAN APPROVAL REQUIRED

---

## CS-09 — BigCommerce Integration for Australia's Largest Office Supply Brand

### Customer
Anonymised — Australia's biggest office supply brand, a multi-channel retailer serving both business and consumer customers.

### Customer Disclosure Status
ANONYMISED

### Confidentiality Classification
UNKNOWN — historical "Tier 3 — never name," not yet mapped to the current classification framework.

### External Use Approval
HUMAN APPROVAL REQUIRED

### Business Problem
The brand needed an e-commerce platform capable of supporting rapid growth while serving both B2B and B2C customers with different pricing structures.

### Business Challenge
Differentiated B2B and B2C pricing logic on one platform; high-traffic, high-volume transaction handling; user experience not meeting expectations.

### Solution
BigCommerce integrated into the brand's existing e-commerce platform, streamlining B2B/B2C pricing.

### Services Delivered
E-commerce & CMS Development; Integration Engineering.

### Technology
BigCommerce. Detailed supporting stack is not published.

### Documented Outcomes
Qualitative only: user experience improved, pricing structure streamlined across customer types, and the platform supported the brand's growth and high traffic/sales volume.

### Documented Metrics
No published metric. Team size and project duration are not published.

### Evidence Status
DATA GAP — evidence provenance not explicitly documented; qualitative outcomes only, no figures to trace.

### Campaign Fit
This is an e-commerce platform build. E-commerce & CMS Development has no dedicated campaign under `context/campaigns.md` and is routed to C2 by default. The historical source does not document sufficient integration-specific technical detail to independently support a secondary C4 association here (unlike CS-01, CS-05, or CS-08, where the integration work is explicitly detailed), so no secondary campaign is assigned.

### Campaign Association
C2

### External Usage Restrictions
Never name the client. Describe only by category (e.g., "Australia's largest office supply brand"). Do not restate the historical source's "expert-level" BigCommerce capability claim — that claim was sourced to an internal skill matrix, not to documented case-outcome evidence, and is excluded from this record. Any BigCommerce capability claim must be sourced from `context/services.md` or `context/technology.md`, not asserted here.

### Internal Notes
*(Internal only.)* Detailed architecture is not published; do not describe beyond what is documented above.

### Status
HUMAN APPROVAL REQUIRED

---

## CS-10 — WordPress Migration for an Online Poker Platform

### Customer
Anonymised — an online poker game website; country and company size not published.

### Customer Disclosure Status
ANONYMISED

### Confidentiality Classification
UNKNOWN — historical "Tier 3 — never name," not yet mapped to the current classification framework.

### External Use Approval
HUMAN APPROVAL REQUIRED

### Business Problem
The website's backend was not functioning smoothly, content updates were difficult, SEO performance was poor, and load times were degrading user experience.

### Business Challenge
Backend functions not operating smoothly; slow, difficult content updates; poor SEO performance limiting organic traffic; slow page load harming user experience.

### Solution
Migration of the website to WordPress.

### Services Delivered
E-commerce & CMS Development; Web Application Development.

### Technology
WordPress. Detailed stack is not published.

### Documented Outcomes
Qualitative only: backend functions operating smoothly, content updates significantly easier, SEO compatibility improved with higher organic traffic, and reduced page load time.

### Documented Metrics
No published metric.

### Evidence Status
DATA GAP — evidence provenance not explicitly documented; qualitative outcomes only.

### Campaign Fit
This is a CMS migration build (Web/CMS development), routed to C2 by default under `context/campaigns.md`'s logic for services without a dedicated campaign. No other campaign is independently supported by the documented business problem.

### Campaign Association
C2

### External Usage Restrictions
Never name the client. Describe only by category. The historical source explicitly restricts this case study to low-priority, directly-relevant use only — **do not use it as a general lead-credibility proof point.** Its industry (online gaming / media & entertainment) is separately flagged in `context/icp.md` as a lower-priority vertical; do not build outbound campaigns around this case study.

### Internal Notes
*(Internal only.)* Team size and project duration are not published.

### Status
HUMAN APPROVAL REQUIRED

---

## Campaign-to-Case-Study Mapping

Campaign associations below reflect only what each case study's own documented business problem and technical need support. Campaign portfolio weightings (25/25/15/25/10) were not used to select or force any association.

### C1 — AI-Enabled Product Engineering
**Case Studies: NONE**

No case study currently demonstrates AI-Enabled Product Engineering. See the C1 Evidence Gap section above. This is an intentional, current DATA GAP — not an oversight to be silently filled.

### C2 — Engineering Pods & Staff Augmentation
Case Studies: CS-02 (primary), CS-03 (primary), CS-06 (primary), CS-07 (primary), CS-08 (primary), CS-09 (primary), CS-10 (primary)

Each of these is either a directly embedded team/staff-augmentation engagement (CS-02, CS-06) or a build delivered through Zediant's default pod-delivery model for services without a dedicated campaign (CS-03, CS-07, CS-08, CS-09, CS-10), per `context/campaigns.md`'s own routing logic.

### C3 — Platform Engineering & Cloud Modernization
Case Studies: CS-04 (primary), CS-06 (secondary)

CS-04's business problem (infrastructure scaling, database reliability) is a direct, exact match. CS-06's secondary association reflects genuinely documented DevOps/CI-CD/disaster-recovery work introduced during that engagement.

### C4 — Middleware & API Integration (ZCoupler)+
Case Studies: CS-01 (primary), CS-05 (primary), CS-02 (secondary), CS-03 (secondary), CS-08 (secondary)

Each carries a documented, genuine data-integration or middleware component (DMS integration, Salesforce sync, or supplier-database integration) as evidence — not the automotive/consultancy/retail industries these engagements happen to sit in.

**Note on ZCoupler:** no case study in this file documents use of "ZCoupler" as a named capability. Every engagement describes "Zediant Middleware" or generic integration/middleware work. Per `context/campaigns.md`'s own open item, "ZCoupler" is not confirmed as an approved externally-usable product name — it is not attached to any case study here, and none should imply ZCoupler-branded delivery.

### C5 — Enterprise Custom Development & Modernization
**Case Studies: NONE assigned**

**Historical C5 mapping conflict resolved.** An earlier version of `context/campaigns.md` listed "Related Case Studies: CS-06, CS-08, CS-01" for C5, but none of these three case studies' own documented business problems, as recorded above, independently establish Enterprise Custom Development & Modernization as their primary or secondary campaign fit in this file — their strongest evidence points to C2/C3 (CS-06), C2/C4 (CS-08), and C4 (CS-01) respectively. The current `context/campaigns.md` no longer lists any case study for C5. Current campaign mapping does not assign any case study to C5.

---

*Source: derived from `migration/original-source/case_studies.md`, current as of the human decisions recorded above. Historical source material — including its Oil & Gas framing of CS-05, its list of "Related Case Studies" for C1, and its Tier 1/2/3 confidentiality scheme — has been superseded where this file conflicts with it. No Instantly references, sequence IDs, sender mappings, CRM mappings, or retired campaign structures (List A–E, or any C6) appear in this file.*
