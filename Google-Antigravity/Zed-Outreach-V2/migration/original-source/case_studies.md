# Overview

This document is the retrieval layer between a prospect conversation and Zediant's delivery history. It exists so an AI agent can answer one question quickly and accurately: *which piece of proof is most relevant to the person in front of me?*

Ten case studies are documented. Each carries selection metadata — industry, technology, business problem, company size, decision maker, campaign, and service — so an agent can match proof to context rather than defaulting to the most impressive story.

## How to use this document

| Situation | Action |
|---|---|
| Writing outreach Email 2 | Select the case study matching the prospect's vertical; use one Sales Talking Point verbatim |
| Preparing a discovery call | Read the Customer Challenges and Discovery Questions sections for the closest match |
| Handling an objection | Check Objections Addressed across all case studies |
| Building a proposal | Use Business Outcomes and Technical Outcomes; never extrapolate beyond what is recorded |
| Prospect asks "have you done this before?" | Use AI Retrieval Rules to select, then answer with specifics, not generalities |

## Confidentiality rules — read before using any case study externally

Zediant's client information falls into three tiers. Misusing tier 2 or 3 creates legal and relationship risk.

| Tier | Clients | External use |
|---|---|---|
| **1 — Publicly named by Zediant** | 11Wickets, Diamond Professional Consultants / Zakaa Innovation Hub | Safe to name. Published on zediant.com. |
| **2 — Named in testimonials** | Networx, STAGER, Zwick Roell, DIJGTAL | Safe to quote the published testimonial. Do **not** extend beyond the quoted words or attribute additional projects. |
| **3 — Anonymised / NDA** | All Company Profile case studies; the automotive SaaS/DaaS client; the Australian office supply brand; the material handling manufacturer; the poker platform | **Never name.** Describe by category only ("a leading automotive parts dealer," "Australia's largest office supply brand"). |

**Absolute prohibition.** Internal documents name two clients in the context of revenue concentration. Those names appear in no public Zediant material and must **never** be used in any outbound message, proposal, deck, or conversation. If asked directly who Zediant's largest client is, decline politely and offer a reference introduction instead.

## Structural warnings

**Two case studies are the same client.** The Wholesale Parts CRM and Team Augmentation for Automotive Software case studies both describe a global provider of SaaS and DaaS solutions for data-driven automobiles. They are almost certainly the same account. Presenting them as two separate clients overstates Zediant's client diversity. Use one or the other in any single conversation, not both.

**Several flagship case studies belong to the concentrated account.** Given that approximately 90% of revenue comes from one client, an agent leaning heavily on the automotive case studies is showcasing the concentration risk, not diversity. Balance automotive proof with 11Wickets, Zakaa, BigCommerce, and Sitecore examples where the prospect context allows.

**Three website errors identified.** Do not repeat these when quoting from the site:

| Error | Location | Correct position |
|---|---|---|
| 11Wickets described as "an eCommerce solution... for this sports retailer" | Page meta description | It is AWS scaling and MySQL clustering for a fantasy cricket platform |
| "Zediant was chosen because of its extensive knowledge of the financial sector" | Team Augmentation (automotive) case study | Appears to be copy-paste from another case study. Do not cite |
| 11Wickets industry listed as "Cloud Solutions" | Case study header | Cloud Solutions is a service, not an industry. The industry is gaming / sports technology |

Cross-reference: `company.md` · `services.md` · `icp.md` · `campaigns.md`

---

# CS-01 — Middleware Integration for Multiple Large DMS

## Client Profile

| Attribute | Detail |
|---|---|
| Client | Anonymised — a leading automotive parts dealer's customised CRM product |
| Industry | Automotive — parts distribution and dealer systems |
| Company size | Enterprise; product serving multiple dealer vendors |
| Country | APAC, UK, USA |
| Business type | Software product company serving automotive dealers |
| Growth stage | Established, multi-region |
| Confidentiality | **Tier 3 — never name** |

## Business Situation

The client's CRM product needed to serve dealers running different dealership management systems. Customer and sales data sat siloed in each DMS with no path between them, so the CRM could not present a complete picture to the sales representatives who depended on it.

## Customer Challenges

- Customer and sales data siloed across multiple DMS platforms
- No visibility or insight into sales performance across the network
- Difficulty making informed decisions or responding to market trends in time
- Manual data entry consuming time and introducing errors
- Sales reps forced to consult multiple systems to serve one customer

## Technical Challenges

- Integrating with multiple heterogeneous DMS platforms — **ERA, CDK, and Pentana** among them
- No common data model across source systems
- Data requiring standardisation, enrichment, and validation before it could be trusted
- Real-time synchronisation rather than batch transfer
- Solution had to be repeatable across dealers, not bespoke per installation

## Existing Environment

Multiple third-party DMS platforms (ERA, CDK, Pentana), a customised CRM product, and manual data entry bridging the gap between them.

## Project Goals

- Give sales reps a single source of decision-ready customer and sales data inside the CRM
- Eliminate manual data entry between DMS and CRM
- Improve data quality through standardisation and validation
- Build a solution repeatable across the dealer base

## Proposed Solution

Zediant Middleware — an integration layer sitting between the DMS platforms and the CRM, enabling real-time synchronisation. Data is standardised, enriched, and validated in transit so that what reaches the CRM is accurate and current.

## Services Delivered

Integration & Middleware Engineering · Enterprise Custom Development · Platform Architecture & System Design. See `services.md`.

## Technology Stack

| Layer | Technologies |
|---|---|
| Languages | Java, JSP |
| Frameworks | Spring, EJB |
| Messaging | JMS, ActiveMQ |
| API | JAX-RS, REST |
| Database | NoSQL |
| Frontend | AngularJS, HTML5, CSS |
| Patterns | SOA, EAI, microservices, BPM |
| Integration targets | ERA, CDK, Pentana DMS platforms |

## Architecture Summary

A message-driven middleware layer. Adapters per DMS platform normalise source data into a common model; a transformation and validation stage standardises, enriches, and validates records; a messaging backbone (JMS/ActiveMQ) moves events between systems asynchronously; REST APIs expose the unified data to the CRM. The adapter pattern is what makes the solution repeatable across dealers rather than bespoke per installation.

## Team Composition

**Assumption** — team composition is not documented for this engagement. Based on comparable Zediant integration work, expect an architect, 3–5 backend engineers, QA, and a project manager. Do not state a team size externally without confirmation.

## Project Timeline

**Assumption** — no timeline is published. Comparable Zediant integration engagements run 6–12 months to production. Do not quote a duration without confirmation.

## Business Outcomes

Recorded outcomes, qualitative:

- **Improved data quality** — standardisation, enrichment, and validation applied before transfer
- **Increased visibility** — comprehensive view of customer and sales data across previously disconnected DMS
- **Streamlined processes** — manual data entry automated, reducing error risk and saving time
- **Cost savings** — reduced manual data entry cost and improved process efficiency for multiple vendors using the CRM product
- **Market adoption** — became a popular solution among leading automotive parts dealers across APAC, UK, and USA

**No percentage figures are published for this engagement.** Do not invent them.

## Technical Outcomes

| Dimension | Outcome |
|---|---|
| Performance | Real-time synchronisation replacing batch and manual transfer |
| Automation | Manual data entry eliminated between DMS and CRM |
| Scalability | Adapter architecture allowed extension to additional DMS platforms and dealers |
| Security | Not documented for this engagement |
| Maintainability | Repeatable, productised solution rather than per-dealer bespoke integration |

## Customer Benefits

Sales representatives make decisions from the CRM alone rather than consulting multiple systems. Management gains cross-network sales visibility. The client's CRM product became more competitive because it could serve dealers regardless of their DMS.

## Challenges During Delivery

**Assumption**, inferred from the nature of multi-party integration work rather than documented for this engagement:

- Third-party DMS access and credentials typically gate project start
- Source data quality is usually worse than the client believes
- Each additional DMS adds an adapter and a validation ruleset
- Live dealer operations cannot be disrupted during cutover

## Best Practices

- Build adapters per source system rather than point-to-point integrations — this is what made the solution resellable
- Standardise, enrich, and validate in transit, not at destination
- Design for the second dealer, not the first
- Treat middleware as a product with a roadmap, not a one-off project

## Similar Customers

Dealer groups and OEM suppliers running multiple DMS · Multi-store retailers with disconnected POS and ERP · Logistics operators exchanging data across carriers and warehouses · Any organisation where an acquisition created duplicate systems.

## Relevant Industries

Automotive (primary) · Logistics & supply chain · Retail & multi-store · Manufacturing · Healthcare (structurally similar, unproven).

## Relevant ICPs

`icp.md` → ICP 4 (Automotive & Dealer Networks) · ICP 3 (Product Companies) · ICP 7 (Logistics)

## Relevant Campaigns

`campaigns.md` → C4 (Middleware & API Integration (ZCoupler))

## Relevant Services

`services.md` → Integration & Middleware Engineering · Enterprise Custom Development

## Sales Talking Points

1. "We built the middleware that lets a CRM talk to ERA, CDK, and Pentana — three DMS platforms that don't talk to each other."
2. "It became a repeatable product, not a one-off integration. Leading automotive parts dealers across APAC, UK, and USA run it."
3. "Data is standardised, enriched, and validated before it moves — so what lands in the CRM is decision-ready."
4. "Sales reps stopped consulting three systems to serve one customer."
5. "Manual data entry between DMS and CRM was eliminated entirely."
6. "The client's CRM became sellable to dealers regardless of which DMS they run."
7. "We designed adapters per source system, which is why adding the next DMS didn't mean rebuilding."
8. "Real-time synchronisation, not overnight batch."
9. "Cost savings came from removing manual data entry across multiple vendors using the product."
10. "This is the deepest thing we do. Integration is where we're genuinely differentiated, not just competent."
11. "If you can name the systems that don't talk to each other, we've probably bridged something similar."
12. "We know DMS data models. That's not a claim most engineering firms can make honestly."

## Discovery Questions This Case Study Answers

- "Have you integrated with dealer management systems before?"
- "Can you handle multiple source systems with different data models?"
- "How do you deal with poor data quality at source?"
- "Is this a one-off build or something we can extend?"
- "Do you have automotive domain knowledge?"
- "Can you do real-time rather than batch?"

## Objections Addressed

| Objection | How this case study answers it |
|---|---|
| "We already have a vendor." | This client's CRM vendor could not solve the DMS problem — Zediant was the specialist layer beneath |
| "You won't understand our systems." | ERA, CDK, and Pentana named specifically; domain knowledge is demonstrable |
| "Integration projects always fail." | This one became a product other dealers adopted |
| "We're too complex." | Multi-DMS, multi-region, multi-vendor is the documented scenario |
| "No budget." | The engagement produced documented cost savings from eliminated manual entry |

## AI Recommendation Rules

Recommend CS-01 when:

- The prospect is in automotive, dealer networks, or parts distribution
- The stated problem involves multiple systems not exchanging data
- The prospect mentions DMS, ERP, CRM, or POS integration
- An acquisition has created duplicate systems
- The contact is CIO, IT Director, CTO, or Enterprise Architect

Do **not** recommend when the prospect needs product development rather than integration, or when the conversation is about engineering capacity rather than systems.

**Priority: HIGHEST.** This is Zediant's single strongest proof point and its most differentiated capability.

## Keywords

middleware, middleware integration, DMS integration, dealer management system, ERA, CDK, Pentana, automotive CRM, automotive parts, dealer network, real-time synchronisation, data synchronisation, data standardisation, data enrichment, data validation, data quality, siloed data, system integration, enterprise application integration, EAI, SOA, API integration, JMS, ActiveMQ, message queue, event driven, adapter pattern, Java, Spring, EJB, JSP, JAX-RS, REST, NoSQL, AngularJS, microservices, BPM, single source of truth, sales visibility, manual data entry elimination, cost savings, APAC, UK, USA, repeatable solution, productised integration, legacy integration, CRM integration, ERP integration, multi-system consolidation, OEM, aftermarket parts, sales performance visibility

---

# CS-02 — Wholesale Parts CRM for Automotive Dealers and OEMs

## Client Profile

| Attribute | Detail |
|---|---|
| Client | Anonymised — a global provider of SaaS and DaaS solutions for data-driven automobiles |
| Industry | Automotive technology / SaaS |
| Company size | Enterprise — software used in 186 countries by 50 OEM manufacturers and 250,000+ industry professionals |
| Country | APAC delivery focus; global client footprint |
| Business type | SaaS and DaaS product company |
| Growth stage | Established, global |
| Confidentiality | **Tier 3 — never name** |

**Important.** This client also appears in CS-06 (Team Augmentation for Automotive Software). Treat CS-02 and CS-06 as one account. Do not present them as two clients.

## Business Situation

The client offered a full product suite for customer-centric automotive service but had no robust CRM for dealers to manage sales and service representative activity. That gap was degrading the overall customer experience their platform was meant to deliver.

## Customer Challenges

- No CRM for dealers to manage sales and service rep activity
- Customer experience degraded despite a strong wider product suite
- Repetitive manual tasks consuming rep time
- Poor collaboration between departments
- No real-time analytics on sales performance or customer behaviour
- Sales and customer data locked inside dealer DMS platforms

## Technical Challenges

- Building an iPad-first CRM for field use by sales representatives
- Importing sales and customer data from heterogeneous dealer DMS platforms
- Generating statistics, reports, and forward projections from imported data
- Supporting 50+ dealers and thousands of end customers
- Integrating a mobile client, a web portal, and a middleware layer as one system

## Existing Environment

A mature SaaS and DaaS product suite for automotive data, dealer DMS platforms as the data source, and no CRM layer connecting the two.

## Project Goals

- Deliver proactive customer service capability to dealers
- Simplify repetitive rep tasks
- Improve inter-departmental collaboration
- Provide real-time analytics and predictive insight
- Align KPIs and support business continuity planning

## Proposed Solution

Zediant produced a transformational roadmap, then built the CRM: lead and customer management, task and issue management, and analytics — supported by a middleware layer that talks to dealer DMS platforms to import sales and customer data and generate statistics, reports, and projections.

## Services Delivered

Design · Development · Quality Assurance · Project Management · Integration & Middleware Engineering · Advisory (transformational roadmap). See `services.md`.

## Technology Stack

| Layer | Technologies |
|---|---|
| Mobile | Objective-C, Swift (iPad) |
| Backend | .NET, C# |
| Database | MS SQL Server |
| Data access | LINQ |
| Frontend | jQuery, AngularJS, HTML5, CSS |
| Integration | Middleware to dealer DMS |

## Architecture Summary

Three tiers. An iPad native client for field reps; a .NET backend with MS SQL Server holding CRM data and serving analytics; and a middleware layer importing from dealer DMS platforms. Analytics and projection logic sits server-side so the mobile client stays thin.

## Team Composition

| Role | Count |
|---|---|
| Total team | **12** |
| Composition | Design, development, QA, and project management disciplines documented; exact per-role split not published |

## Project Timeline

| Phase | Detail |
|---|---|
| Total duration | **18 months** |
| Engagement model | Time & Material |
| Phase breakdown | Not published — do not invent one |

This is the longest and largest documented Zediant engagement.

## Business Outcomes

Recorded outcomes:

- **50+ dealers** across APAC using the platform
- **5,700 customers** served through it
- Improved sales productivity
- Real-time analytics available to dealers
- Centralised data for managers
- Improved customer experience

## Technical Outcomes

| Dimension | Outcome |
|---|---|
| Performance | Real-time analytics on sales performance and customer behaviour |
| Automation | Repetitive rep tasks simplified; DMS data import automated |
| Scalability | Supported 50+ dealers and 5,700 customers |
| Security | Not documented for this engagement |
| Maintainability | Sustained over an 18-month build and continuing relationship |

## Customer Benefits

Dealers gained proactive service capability they previously lacked. Managers gained centralised visibility. The client's product suite became more complete and more competitive.

## Challenges During Delivery

**Assumption**, inferred from engagement shape rather than documented: an 18-month T&M engagement with 12 people implies evolving scope and continuous re-prioritisation. Heterogeneous DMS sources would have required per-platform handling. iPad-first design for field use imposes offline and connectivity considerations.

## Best Practices

- Lead with a transformational roadmap before building — this engagement started with strategy, not code
- Build the middleware alongside the application when the application depends on external data
- Design mobile-first when the primary user is in the field, not at a desk
- T&M suits an 18-month engagement with evolving requirements; fixed price would not have

## Similar Customers

Automotive SaaS and DaaS providers · Dealer-facing software vendors · Field-sales organisations needing mobile CRM · Companies whose product depends on data locked in third-party systems.

## Relevant Industries

Automotive (primary) · SaaS · Field services · Manufacturing distribution.

## Relevant ICPs

`icp.md` → ICP 4 (Automotive) · ICP 3 (Product Companies) · ICP 2 (SaaS)

## Relevant Campaigns

`campaigns.md` → C2 (Engineering Pods & Staff Augmentation) · C4 (Middleware & API Integration (ZCoupler))

## Relevant Services

`services.md` → Dedicated Engineering Pods · Mobile Application Development · Integration & Middleware Engineering · Advisory & Consulting

## Sales Talking Points

1. "We built a dealer CRM now used by 50+ dealers across APAC, serving 5,700 customers."
2. "Twelve people, eighteen months. We don't do drive-by projects."
3. "It started with a transformational roadmap, not a specification — we shaped the strategy before writing code."
4. "iPad-first, because the users were sales reps in dealerships, not analysts at desks."
5. "We built the CRM and the middleware feeding it. Most vendors do one or the other."
6. "Real-time analytics on sales performance, customer behaviour, and forward projections."
7. "The client had a strong product suite with a CRM-shaped hole in it. We filled it."
8. "Time and Material over eighteen months — the scope evolved, and the model let it."
9. "Objective-C and Swift on the device, .NET and SQL Server behind it."
10. "This client's software runs in 186 countries with 50 OEM manufacturers. We were trusted with a core piece of it."

## Discovery Questions This Case Study Answers

- "Can you handle a large multi-year engagement?"
- "Have you built mobile CRM for field teams?"
- "Can you do both application and integration work?"
- "Do you work with enterprise automotive clients?"
- "How do you handle evolving scope over a long project?"

## Objections Addressed

| Objection | How this case study answers it |
|---|---|
| "You're too small for our project." | 12-person team over 18 months on an enterprise account |
| "We need long-term commitment, not a project." | This relationship ran 18 months on the CRM alone and continues |
| "We're not ready — we don't have a spec." | The engagement opened with a transformational roadmap, not a spec |
| "We already have a vendor." | This client had a full product suite and still engaged Zediant for the gap |

## AI Recommendation Rules

Recommend CS-02 when:

- The prospect questions Zediant's capacity for a large or long engagement
- The need is mobile CRM, field-sales tooling, or dealer-facing software
- The prospect is an automotive technology or SaaS/DaaS company
- The prospect needs both application build and system integration
- The contact is CTO, Head of Product, or CIO

**Do not use alongside CS-06** — same client.

**Priority: HIGH.** Strongest evidence of scale and duration. Use carefully given concentration considerations.

## Keywords

automotive CRM, dealer CRM, wholesale parts, parts distribution, OEM, dealer productivity, sales rep, field sales, iPad application, mobile CRM, Objective-C, Swift, .NET, C#, MS SQL Server, LINQ, jQuery, AngularJS, HTML5, lead management, customer management, task management, issue management, real-time analytics, predictive insight, sales projections, KPI alignment, business continuity, transformational roadmap, DMS import, middleware, SaaS, DaaS, data-driven automotive, 18-month engagement, 12-person team, time and material, APAC, enterprise engagement, proactive customer service, departmental collaboration

---

# CS-03 — Lubricant Recommendation & Equipment Maintenance Application

## Client Profile

| Attribute | Detail |
|---|---|
| Client | Anonymised — a leading automotive technology company in APAC, partnered with premium lubricant suppliers |
| Industry | Automotive technology / industrial lubricants |
| Company size | Established; product adopted by 23+ lubricant companies |
| Country | APAC |
| Business type | Technology provider to lubricant manufacturers |
| Growth stage | Established |
| Confidentiality | **Tier 3 — never name** |

## Business Situation

Determining the correct lubricant for a given piece of engine equipment depended on frequently changing specifications managed on paper. The manual process was slow, error-prone, and did not scale across suppliers.

## Customer Challenges

- Manual, paper-based management of lubricant specifications
- Specifications changing frequently with no reliable propagation
- Non-technical stakeholders unable to determine correct products
- No scalable way to serve multiple lubricant suppliers
- Risk of incorrect recommendation damaging equipment

## Technical Challenges

- Integrating with multiple premium lubricant supplier databases
- Modelling complex vehicle and equipment specifications
- Maintaining a centralised, continuously accurate specification database
- Delivering the same recommendation logic to web and mobile clients across different suppliers
- Releasing new versions without disrupting existing users

## Existing Environment

Paper-based specification management, supplier databases held separately, no central system.

## Project Goals

- Automate identification and recommendation of correct lubricants
- Make the tool usable by non-technical stakeholders
- Centralise specification data with automatic updates
- Serve multiple lubricant suppliers from one platform
- Support both web and mobile delivery

## Proposed Solution

A web-based application automating lubricant recommendation for specific engine equipment, integrated with premium supplier databases and complex vehicle specifications, on a centralised database keeping recommendations current. The recommendation engine was exposed as an API consumed by both web and mobile clients across different suppliers.

## Services Delivered

Design · Development · Quality Assurance · Project Management. See `services.md`.

## Technology Stack

| Layer | Technologies |
|---|---|
| Backend | JSP, Spring, Hibernate |
| Database | MS SQL |
| Mobile | Objective-C, Swift, Ionic |
| Frontend | AngularJS, HTML5, CSS |
| Delivery | Recommendation API for web and mobile |

## Architecture Summary

A centralised specification database fed by supplier integrations, with a recommendation engine exposed as an API. Web and mobile clients consume the same API, which is what allowed one platform to serve 23+ lubricant companies without rebuilding per supplier.

## Team Composition

| Role | Count |
|---|---|
| Total team | **8** |
| Composition | Design, development, QA, project management; exact split not published |

## Project Timeline

| Phase | Detail |
|---|---|
| Total duration | **10 months** |
| Engagement model | Time & Material |

**Note.** Internal strategy documents reference a "10-month UAE project" in the context of delivery delays and the need for stricter contracting with delay clauses. It is **not confirmed** whether this refers to the same engagement. Do not present this project as a delivery-speed proof point without checking.

## Business Outcomes

Recorded outcomes:

- **23+ leading lubricant companies in APAC** using the application
- Cost savings for the client
- Environmentally beneficial outcome (correct lubricant selection reduces waste)
- Growing demand from additional lubricant suppliers

## Technical Outcomes

| Dimension | Outcome |
|---|---|
| Performance | Instant recommendation replacing manual specification lookup |
| Automation | Paper-based specification management eliminated |
| Scalability | One platform serving 23+ supplier companies |
| Security | Not documented |
| Maintainability | Centralised data with automatic updates and controlled version release |

## Customer Benefits

Non-technical staff can determine correct lubricants without expert consultation. Specification changes propagate automatically. The client turned an internal capability into a product multiple suppliers pay for.

## Challenges During Delivery

Documented indirectly: the 10-month duration against an 8-person team suggests scope evolution. Internal strategy flags a 10-month project as an example motivating stricter milestone and delay clauses — treat the delivery timeline as a lesson learned rather than a selling point.

## Best Practices

- Build the recommendation engine as an API from the start — this enabled multi-client, multi-supplier reuse
- Centralise the data that changes most frequently
- Design the interface for the least technical user, not the most
- Agree milestone and delay clauses upfront on evolving-scope engagements

## Similar Customers

Industrial product manufacturers with complex specification matrices · Equipment maintenance and aftermarket businesses · Companies turning internal expertise into a customer-facing tool · Distributors serving multiple manufacturer brands.

## Relevant Industries

Automotive · Manufacturing & industrial · Energy & lubricants · Equipment maintenance.

## Relevant ICPs

`icp.md` → ICP 4 (Automotive) · ICP 6 (Manufacturing & Industrial) · ICP 3 (Product Companies)

## Relevant Campaigns

`campaigns.md` → C2 (Engineering Pods & Staff Augmentation) · C4 (Middleware & API Integration (ZCoupler))

## Relevant Services

`services.md` → Web Application Development · Mobile Application Development · Integration & Middleware Engineering · UI/UX Design

## Sales Talking Points

1. "We replaced a paper-based specification process with an application 23+ lubricant companies now use."
2. "One recommendation engine, exposed as an API, serving web and mobile across multiple supplier brands."
3. "The interface was built for non-technical staff — the people actually doing the job, not engineers."
4. "Specifications change constantly. We centralised them so updates propagate automatically."
5. "The client turned internal expertise into a product other companies pay for."
6. "Eight people, ten months, and it scaled to 23+ companies."
7. "Correct lubricant selection has an environmental benefit as well as a commercial one."
8. "We integrated directly with premium lubricant supplier databases."
9. "Complex vehicle and equipment specification modelling — this isn't a CRUD app."
10. "Demand grew from other suppliers after launch. That's the strongest signal a product works."

## Discovery Questions This Case Study Answers

- "Can you build something non-technical staff will actually use?"
- "Have you replaced manual or paper processes?"
- "Can you handle complex product specification data?"
- "Can one platform serve multiple brands or suppliers?"
- "Have you built API-first for web and mobile reuse?"

## Objections Addressed

| Objection | How this case study answers it |
|---|---|
| "Our users aren't technical." | The interface was explicitly designed for non-technical stakeholders |
| "Our specification data is too complex." | Complex vehicle and equipment specifications across multiple suppliers |
| "We'd need it on web and mobile." | One API, both clients, multiple supplier brands |
| "We're too small." | 8-person team, 10-month build — a mid-sized engagement |

## AI Recommendation Rules

Recommend CS-03 when:

- The prospect describes a manual or paper-based process
- Complex product specification or configuration data is involved
- The prospect needs both web and mobile from one codebase or API
- Non-technical end users are the primary audience
- The prospect is in manufacturing, automotive aftermarket, or industrial products

**Priority: HIGH.** Clean, non-concentrated proof point with strong adoption evidence.

## Keywords

lubricant recommendation, equipment maintenance, specification management, paper-based process, process automation, recommendation engine, API-first, centralised database, supplier integration, OEM fluid specifications, vehicle specifications, non-technical users, intuitive interface, JSP, Spring, Hibernate, MS SQL, Objective-C, Swift, Ionic, AngularJS, HTML5, web application, mobile application, multi-tenant, multi-brand, APAC, 23 companies, cost savings, environmental benefit, industrial products, aftermarket, equipment specifications, automatic updates, version release

---

# CS-04 — 11Wickets Scalability & Performance Optimisation

## Client Profile

| Attribute | Detail |
|---|---|
| Client | **11Wickets** — publicly named by Zediant |
| Industry | Online gaming / fantasy sports (website labels this "Cloud Solutions" — that is a service, not an industry) |
| Company size | Not published |
| Country | India |
| Business type | Consumer platform — online fantasy cricket |
| Growth stage | Scaling, growing user base |
| Confidentiality | **Tier 1 — safe to name** |

## Business Situation

11Wickets' user base was growing faster than its infrastructure could support. Concurrent load and the volume of write operations for game stats and results were producing slow performance and downtime.

## Customer Challenges

- Existing infrastructure unable to handle rising concurrent users
- Slow performance and downtime during peak usage
- Large write volume for game stats and results creating a bottleneck
- User experience degrading as the platform grew

## Technical Challenges

- Infrastructure not horizontally scalable
- MySQL database becoming the bottleneck under write-heavy load
- Increased response times under concurrency
- Need for high availability — node failure could not stop write operations

## Existing Environment

AWS infrastructure without auto-scaling, single-node MySQL, no load balancing.

## Project Goals

- Handle an increasing number of concurrent users without degradation
- Process large volumes of write operations for game stats and results
- Improve response times
- Achieve high availability tolerant of node failure

## Proposed Solution

A horizontally scalable AWS architecture using EC2, Auto Scaling, and Load Balancing, paired with a MySQL Galera cluster distributing write operations across multiple nodes.

## Services Delivered

Platform Engineering & Cloud DevOps · Advisory (architecture and performance assessment). See `services.md`.

## Technology Stack

| Layer | Technologies |
|---|---|
| Cloud | AWS — EC2, Auto Scaling Groups, Elastic Load Balancing |
| Database | MySQL, Galera Cluster |
| Architecture | Horizontally scalable, multi-node |

## Architecture Summary

An EC2 Auto Scaling group adds and removes instances against load, behind a load balancer distributing incoming traffic. Beneath, a multi-node MySQL Galera cluster distributes write operations, reducing single-node load and providing automatic failover when a node fails.

## Team Composition

**Assumption** — not published. Infrastructure engagements of this scope typically involve a cloud architect and one or two DevOps engineers. Do not state a team size without confirmation.

## Project Timeline

**Assumption** — not published. Comparable platform engagements run 6–12 weeks. Do not quote a duration without confirmation.

## Business Outcomes

Recorded outcomes, qualitative:

- Platform able to handle increasing concurrent users
- Smoother, faster user experience
- Stable and reliable service during growth

**No percentage figures, user counts, or uptime numbers are published.** Do not invent them. In particular, do not attach the "99.99% availability" claim from Zediant's Platform Engineering page to this engagement — it is unsupported.

## Technical Outcomes

| Dimension | Outcome |
|---|---|
| Performance | Reduced single-node load; improved response times |
| Automation | Auto Scaling adds and removes capacity against real load |
| Scalability | Horizontal scaling replacing fixed capacity |
| Security | Not documented |
| Maintainability | Automatic node-failure handling without manual intervention |

## Customer Benefits

The platform could grow without infrastructure becoming the constraint. Write operations continue through node failure. User experience stabilised during a growth period that had been degrading it.

## Challenges During Delivery

**Assumption** — not documented. Galera cluster migrations on a live write-heavy database carry real risk and typically require careful cutover planning.

## Best Practices

- Fix the database bottleneck and the compute layer together — scaling one without the other moves the problem rather than solving it
- Galera clustering suits write-heavy workloads where a read replica strategy would not help
- Auto Scaling only delivers value when the application layer is genuinely stateless
- Design for node failure as a normal event, not an exception

## Similar Customers

Consumer platforms with peak concurrency · Gaming and fantasy sports operators · Write-heavy transactional applications · E-commerce platforms with trading peaks · Any SaaS platform outgrowing its original infrastructure.

## Relevant Industries

Gaming & fantasy sports · Consumer internet · E-commerce · SaaS · Fintech (write-heavy transactional parallels).

## Relevant ICPs

`icp.md` → ICP 2 (SaaS Companies) · ICP 3 (Product Companies) · ICP 8 (Retail & E-commerce)

## Relevant Campaigns

`campaigns.md` → C3 (Platform Engineering & Cloud Modernization)

## Relevant Services

`services.md` → Platform Engineering & Cloud DevOps · Advisory & Consulting

## Sales Talking Points

1. "11Wickets — a fantasy cricket platform — came to us when growth was breaking their infrastructure. We can name them because they let us."
2. "We fixed both layers: horizontal scaling on AWS and a MySQL Galera cluster underneath."
3. "Auto Scaling and load balancing meant capacity followed real demand instead of guesswork."
4. "Their bottleneck was write volume, not reads. Read replicas wouldn't have helped. Galera did."
5. "The cluster handles node failure automatically — writes continue even when a node drops."
6. "Scaling compute without fixing the database just moves the bottleneck. We addressed both."
7. "This is one of the few engagements we can discuss by name, which makes it a useful reference."
8. "Concurrency and write-heavy workloads are a specific problem. We've solved it in production."

## Discovery Questions This Case Study Answers

- "Have you handled platforms that fell over under load?"
- "Can you work on AWS infrastructure, not just application code?"
- "Do you have database performance expertise?"
- "Can you deliver high availability?"
- "Do you have a client we can actually talk to?"

## Objections Addressed

| Objection | How this case study answers it |
|---|---|
| "We can't name your clients — do you have references?" | 11Wickets is publicly named and published |
| "Our problem is infrastructure, not code." | This engagement was purely infrastructure and database |
| "We need this fixed before our next peak." | Scoped platform work; shorter than an application build |
| "Our database is the bottleneck." | Exactly the documented problem here |

## AI Recommendation Rules

Recommend CS-04 when:

- The prospect has an outage, downtime, or performance incident
- Concurrency or scaling is the stated problem
- Database performance is the bottleneck
- The prospect is on AWS
- The contact is CTO, VP Engineering, Head of Infrastructure, or DevOps Lead
- **The prospect asks for a nameable reference** — this is the safest named case study available

**Priority: HIGH for platform conversations, HIGHEST when a named client is needed.**

## Keywords

scalability, performance optimisation, AWS, EC2, Auto Scaling, load balancing, horizontal scaling, elastic scaling, MySQL, Galera Cluster, database performance, write operations, concurrent users, high availability, fault tolerance, node failure, failover, response time, downtime, bottleneck, infrastructure, cloud architecture, DevOps, platform engineering, fantasy sports, online gaming, 11Wickets, consumer platform, peak load, capacity planning, database clustering, multi-node, distributed writes, uptime, reliability

---

# CS-05 — Real-Time Executive Dashboards (Zakaa Innovation Hub)

## Client Profile

| Attribute | Detail |
|---|---|
| Client | **Diamond Professional Consultants** — consultancy specialising in performance management and data analytics. Product: Zakaa Innovation Hub |
| Industry | Professional services / consultancy — serving enterprise C-level clients |
| Company size | Not published |
| Country | UAE |
| Business type | Consultancy delivering analytics tooling to its own clients |
| Growth stage | Established |
| Confidentiality | **Tier 1 — named publicly by Zediant** |

## ⚠️ Source discrepancy

Zediant's Company Profile documents an "Enterprise Performance Monitoring Dashboard (UAE)" tagged **Oil & Gas | Enterprise Management | Analytics**, describing senior leadership needing consolidated KPI visibility. The website documents "Real-Time Executive Dashboards for Zakaa Innovation Hub" for **Diamond Professional Consultants, a consultancy**.

Two readings are possible:

1. **Same engagement** — Diamond is the consultancy, and the end client is an oil and gas organisation. This would make it a **channel/aggregator engagement**, and therefore evidence for the C2 agency-channel model as well as for data engineering.
2. **Two separate engagements** with similar deliverables.

**Do not assert either reading externally.** If the oil and gas framing matters to a prospect, confirm with a human first. This discrepancy also affects `icp.md` → ICP 9 (Energy, Oil & Gas), whose sole proof point is this engagement.

## Business Situation

Senior leadership needed a consolidated, real-time view of KPIs spanning multiple enterprise systems. Reporting was fragmented and largely manual, which limited timely, data-driven decision-making.

## Customer Challenges

- KPI reporting fragmented across multiple enterprise systems
- Reporting largely manual and slow to produce
- Decisions delayed or made on stale data
- No single source of truth for management reporting
- No control over which roles could see which data

## Technical Challenges

- Integrating data from multiple internal systems into a unified layer
- Eliminating data silos and manual reconciliation
- Enforcing role-based access over sensitive operational data
- Building for scalability and governance from the outset
- Designing an integration-ready architecture for future data sources

## Existing Environment

Multiple disconnected enterprise systems, manual reporting processes, no consolidated reporting layer.

## Project Goals

- Provide a single source of truth for management-level reporting
- Deliver role-specific views with enforced data access control
- Eliminate manual reconciliation
- Establish a scalable foundation for advanced analytics

## Proposed Solution

A secure, enterprise-grade management dashboard integrating data from multiple internal systems into a unified reporting layer, built modular and integration-ready for future data sources.

## Services Delivered

Architecture Design · Dashboard Development · Data Integration · Quality Assurance. See `services.md`.

## Technology Stack

| Layer | Technologies |
|---|---|
| Backend / data | Python |
| Database | Oracle |
| Frontend | ReactJS |
| Integration | REST APIs |
| Visualisation | Analytics and visualisation components |

## Architecture Summary

A data integration layer pulls from multiple internal systems into a unified reporting store, with role-based access control applied at the presentation layer. A ReactJS front end renders role-specific dashboards. The design is modular so additional data sources can be added without rework.

## Team Composition

| Role | Count |
|---|---|
| Total team | **6** |
| Composition | Architecture, dashboard development, data integration, QA; exact split not published |

## Project Timeline

| Phase | Detail |
|---|---|
| Total duration | **6 months** |
| Engagement model | Time & Material |

## Business Outcomes

Recorded outcomes, qualitative:

- Unified visibility of enterprise KPIs
- Faster and more informed management decisions
- Reduced manual reporting effort
- Improved data accuracy
- Scalable foundation for advanced analytics

**No percentage figures are published.** Do not invent them.

## Technical Outcomes

| Dimension | Outcome |
|---|---|
| Performance | Real-time consolidated reporting replacing manual cycles |
| Automation | Manual reconciliation eliminated |
| Scalability | Modular, integration-ready for future data sources |
| Security | Role-based dashboards with enforced data access controls |
| Maintainability | Built with governance in mind |

## Customer Benefits

Leadership sees one authoritative set of numbers. Different roles see appropriate subsets. Manual reporting effort is removed. The architecture supports adding analytics capability without a rebuild.

## Challenges During Delivery

**Assumption**, inferred from the nature of executive dashboard work: metric definition disputes between business units are the usual obstacle, alongside access to source systems and source data quality.

## Best Practices

- Build the integration layer before the visualisation layer — dashboards on unreconciled data create disputes rather than resolving them
- Enforce role-based access at design time, not as a later addition
- Design for the next data source, not just the current ones
- Get metric definitions agreed in writing before building

## Similar Customers

Enterprises with multiple business systems and manual board reporting · Consultancies delivering analytics to their own clients · Multi-business-unit organisations with disputed metrics · Energy, manufacturing, and logistics operators.

## Relevant Industries

Professional services / consultancy · Energy & oil and gas (subject to the discrepancy above) · Manufacturing · Logistics.

## Relevant ICPs

`icp.md` → ICP 9 (Energy, Oil & Gas — subject to discrepancy) · ICP 1 (Digital Agencies / consultancy channel) · ICP 6 (Manufacturing)

## Relevant Campaigns

`campaigns.md` → C4 (Middleware & API Integration (ZCoupler), primary — data engineering/integration driver) · C2 (Engineering Pods & Staff Augmentation) if read as a consultancy-channel engagement

## Relevant Services

`services.md` → Data Engineering & Analytics · Integration & Middleware Engineering · Enterprise Custom Development

## Sales Talking Points

1. "We built the executive dashboard layer for Diamond Professional Consultants' Zakaa Innovation Hub — real-time C-level visibility."
2. "Six people, six months, in the UAE."
3. "The problem wasn't visualisation. It was that the data lived in systems that didn't reconcile."
4. "Role-based dashboards — different seniority sees different data, enforced by design."
5. "We built the integration layer first. Dashboards on unreconciled data just create arguments."
6. "Modular and integration-ready, so the next data source doesn't mean a rebuild."
7. "Manual reconciliation was eliminated, not reduced."
8. "This is a client we can name, which matters when you want a reference."
9. "Python and Oracle behind it, ReactJS in front, REST between."
10. "A consultancy chose us to build the tool they put in front of their own C-level clients. That's a demanding audience."

## Discovery Questions This Case Study Answers

- "Can you consolidate reporting across multiple systems?"
- "Do you handle role-based access to sensitive data?"
- "Have you delivered in the UAE?"
- "Can you build something we can put in front of our own clients?"
- "Can you work with Oracle?"

## Objections Addressed

| Objection | How this case study answers it |
|---|---|
| "We already have BI tools." | The problem was upstream — data that didn't reconcile, not visualisation |
| "Our data isn't clean enough." | The integration layer addressed exactly that |
| "Have you worked in our region?" | Delivered in the UAE |
| "We'd be reselling this to our clients." | This client did precisely that |

## AI Recommendation Rules

Recommend CS-05 when:

- The prospect describes manual or fragmented management reporting
- Multiple enterprise systems need consolidating for reporting
- Role-based data access is a requirement
- The prospect is UAE-based
- The prospect is a consultancy building for its own clients
- The contact is CIO, CFO, Head of Data, or Transformation Manager

**Priority: HIGH for data and UAE conversations.** One of only two nameable clients.

## Keywords

executive dashboard, management dashboard, real-time dashboard, KPI aggregation, KPI reporting, business intelligence, data consolidation, data integration, single source of truth, role-based access, RBAC, data governance, manual reporting elimination, reconciliation, data accuracy, data silos, enterprise reporting, C-level reporting, board reporting, Python, Oracle, ReactJS, REST API, analytics, visualisation, scalable architecture, modular architecture, UAE, Dubai, Zakaa Innovation Hub, Diamond Professional Consultants, consultancy, performance management, decision latency, advanced analytics foundation

---

# CS-06 — Team Augmentation for Automotive Software

## Client Profile

| Attribute | Detail |
|---|---|
| Client | Anonymised — a top international provider of SaaS and DaaS solutions for data-driven automobiles |
| Industry | Automotive technology / SaaS |
| Company size | Enterprise — 186 countries, 50 OEM manufacturers, 250,000+ industry professionals |
| Country | Global |
| Business type | SaaS and DaaS product company |
| Growth stage | Established, global |
| Confidentiality | **Tier 3 — never name** |

**Same client as CS-02.** Do not present both in one conversation.

## Business Situation

The client ran multiple internal development teams but lacked in-house expertise for a recently acquired customer relationship software product. They needed experienced developers available for long-term collaboration who would take ownership of continuously changing requirements.

## Customer Challenges

- No in-house expertise for a newly acquired software product
- Requirement volatility with no team able to absorb it
- Need for long-term partnership rather than project delivery
- No dedicated testing team on the project
- Mobile experience needed to complement an existing responsive website, with no internal mobile capability
- Strict security requirements

## Technical Challenges

- Understanding an acquired codebase with no documentation
- Test coverage insufficient for safe continuous delivery
- No staging environment for pre-production validation
- No disaster recovery or failover capability
- Building iOS and Android applications from scratch
- Predictive sales forecasting from historical performance data

## Existing Environment

| Component | Stack |
|---|---|
| Mobile app | Objective-C, Swift |
| Manager portal | .NET, Angular, SignalR, Entity Framework, Microsoft SQL Server |
| DevOps | CircleCI pipelines |
| Hosting | AWS |

## Project Goals

- Take ownership of an acquired product without internal knowledge transfer
- Establish delivery infrastructure — DR, staging, test coverage
- Add mobile applications to a web-only experience
- Deliver continuous feature development under changing requirements
- Meet strict security requirements

## Proposed Solution

An embedded team that began with infrastructure and knowledge recovery before feature work. Zediant reverse-engineered the acquired software into its component parts and delivered a developer's manual within a month, built AWS-powered backup and disaster recovery, established a staging environment, and raised test coverage. Feature development followed.

Delivered features include rep tracking and location-based call planning, monthly rep performance evaluation, identification of low-value customers, automated invoice integration with customer DaaS systems, issue tracking, inter-rep information exchange, a marketer content upload portal, and predictive next-month sales forecasting from daily-adjusted historical data.

## Services Delivered

Staff Augmentation · Dedicated Engineering Pods · Platform Engineering & Cloud DevOps · QA & Test Automation · Mobile Application Development · Legacy/Acquired Code Modernisation. See `services.md`.

## Technology Stack

| Layer | Technologies |
|---|---|
| Mobile | Objective-C, Swift |
| Backend | .NET, Entity Framework |
| Frontend | Angular, SignalR |
| Database | Microsoft SQL Server |
| Cloud | AWS |
| DevOps | CircleCI |
| Testing | Unit, functional, and integration tests |

## Architecture Summary

A .NET manager portal with an Angular front end and SignalR for real-time updates, backed by SQL Server on AWS, with native mobile clients. Zediant added an AWS backup and disaster recovery tier for on-demand failover, plus a staging environment mirroring production.

## Team Composition

| Role | Detail |
|---|---|
| Project managers | Documented as involved |
| Developers | Multiple; exact count not published |
| QA | **None on the project** — developers wrote unit, functional, and integration tests |

## Project Timeline

| Phase | Detail |
|---|---|
| Total duration | **3+ years and continuing** |
| Sprint cadence | 2-week sprints with sprint planning |
| Methodology | Agile |
| Early milestone | Developer's manual delivered within **one month** of engagement start |

This is Zediant's longest documented relationship.

## Business Outcomes

Recorded outcomes:

- **Test coverage raised from 70% to 93%** — the single most specific, verifiable metric in Zediant's entire case study library
- Fail-safe continuous delivery of new portal features enabled
- DevOps practices introduced to the project
- Developer's manual delivered within one month, recovering lost knowledge on an acquired codebase
- 3+ year continuing relationship
- Competitiveness of the client's software improved, supporting retention of long-standing clients

## Technical Outcomes

| Dimension | Outcome |
|---|---|
| Performance | Not documented |
| Automation | Unit, functional, and integration test automation; CI/CD via CircleCI |
| Scalability | Not documented |
| Security | AWS backup and DR with on-demand failover; strict security requirements met |
| Maintainability | Coverage 70%→93%; developer's manual; staging environment established |

## Customer Benefits

The client absorbed an acquisition they had no internal capability to support. They gained mobile applications without hiring mobile engineers. Continuous delivery became safe. Institutional knowledge was documented rather than lost.

## Challenges During Delivery

Documented in the engagement narrative:

- Acquired software arrived with no documentation, requiring reverse engineering before any feature work
- No testing team on the project, so developers absorbed test authorship
- No staging environment existed, so pre-production validation had to be built
- Requirements changed continuously — the reason a long-term team was preferred over project delivery

## Best Practices

- **Start with knowledge recovery, not features.** The developer's manual in month one is why the following three years worked
- Build test coverage before accelerating delivery — 70% to 93% is what made continuous delivery fail-safe
- Establish staging and DR before shipping to production
- On acquired codebases, reverse-engineer and document as a billable first phase rather than absorbing it silently
- Two-week sprints with mandatory planning suit clients with volatile requirements

## Similar Customers

Companies that have acquired software they cannot support · Organisations with undocumented codebases and departed original developers · Product companies needing mobile capability without mobile hires · Clients with no internal QA function.

## Relevant Industries

Automotive · SaaS · Any industry with acquired or inherited software.

## Relevant ICPs

`icp.md` → ICP 3 (Product Companies) · ICP 2 (SaaS) · ICP 4 (Automotive)

## Relevant Campaigns

`campaigns.md` → C2 (Engineering Pods & Staff Augmentation, primary — staff aug/pods) · C3 (Platform Engineering & Cloud Modernization, DevOps-introduction angle)

## Relevant Services

`services.md` → Staff Augmentation · Dedicated Engineering Pods · QA & Test Automation · Platform Engineering & Cloud DevOps · Legacy Modernisation

## Sales Talking Points

1. "We raised test coverage from 70% to 93%, which is what made their continuous delivery fail-safe."
2. "They acquired a product they had no expertise to support. We reverse-engineered it and delivered a developer's manual within a month."
3. "That relationship has run for over three years and is still going."
4. "There was no testing team, so our developers wrote unit, functional, and integration tests themselves."
5. "We built AWS backup and disaster recovery for on-demand failover before touching features."
6. "We set up their staging environment — they didn't have one."
7. "Two-week sprints with mandatory planning, because their requirements changed continuously."
8. "We introduced DevOps practices to a project that had none."
9. "Their software runs in 186 countries with 50 OEM manufacturers. We were trusted to own a piece of it."
10. "We added predictive sales forecasting — next month's number from daily-adjusted historical data."
11. "They wanted a team that would take ownership, not contractors who'd wait for tickets. That's what a pod is."
12. "The client had multiple internal development teams and still chose an external one for this. Capability gaps are specific, not general."

## Discovery Questions This Case Study Answers

- "Can you take over a codebase nobody understands?"
- "What happens if we have no documentation?"
- "Can you work without an internal QA team?"
- "Will you stay for the long term or churn people?"
- "Can you handle continuously changing requirements?"
- "Have you supported an acquisition?"

## Objections Addressed

| Objection | How this case study answers it |
|---|---|
| "Nobody here understands that system anymore." | Reverse-engineered an acquired codebase and documented it in one month |
| "We don't have documentation." | Producing it was the first deliverable |
| "We tried outsourcing and they churned." | 3+ years continuing on this account |
| "Our requirements change constantly." | Exactly why this client chose a long-term team |
| "We don't have QA." | Developers wrote the tests; coverage went 70%→93% |
| "We need long-term collaboration, not a project." | This is the documented example |

## AI Recommendation Rules

Recommend CS-06 when:

- The prospect has acquired or inherited software they cannot support
- Documentation is missing and original developers have left
- The prospect has no internal QA function
- The concern is partner longevity or team churn
- Requirements are described as volatile
- The contact is CTO, VP Engineering, or Engineering Manager

**Do not use alongside CS-02** — same client.

**Priority: HIGHEST for capacity and longevity conversations.** Contains the most specific verifiable metric available (70%→93%).

## Keywords

team augmentation, staff augmentation, dedicated team, embedded team, long-term partnership, 3 year relationship, acquired software, acquisition integration, reverse engineering, developer manual, knowledge recovery, undocumented codebase, test coverage, 70 to 93 percent, unit testing, functional testing, integration testing, continuous delivery, fail-safe delivery, DevOps introduction, CircleCI, CI/CD, staging environment, disaster recovery, backup, failover, AWS, .NET, Entity Framework, Angular, SignalR, Microsoft SQL Server, Objective-C, Swift, iOS, Android, agile, two-week sprints, sprint planning, volatile requirements, rep tracking, sales forecasting, predictive analytics, automated invoicing, DaaS integration, issue tracking, ownership, 186 countries, 50 OEM manufacturers

---

# CS-07 — Cryptocurrency Trading Application

## Client Profile

| Attribute | Detail |
|---|---|
| Client | Anonymised |
| Industry | Financial services / cryptocurrency |
| Company size | Not published |
| Country | Not published |
| Business type | Consumer fintech platform |
| Growth stage | Not published |
| Confidentiality | **Tier 3 — never name** |

## Business Situation

The client needed a secure, user-friendly cryptocurrency application to attract and retain customers in a market where trust and usability determine adoption.

## Customer Challenges

- Securing transactions in a low-trust market category
- Delivering an intuitive interface to non-expert users
- Supporting a wide range of digital currencies
- Competing on user experience against established platforms
- Demonstrating security credibly to prospective users

## Technical Challenges

- Multi-factor authentication and end-to-end encryption
- Integration across multiple cryptocurrency exchanges
- Real-time transaction processing
- Real-time price comparison across exchanges
- Multi-currency buy and sell in a single transaction
- Passing independent third-party security audit
- Near-native performance from a cross-platform framework

## Existing Environment

Greenfield build.

## Project Goals

- Secure transaction handling
- Intuitive interface for non-expert users
- Broad digital currency support
- Independent security audit approval
- Cross-platform delivery without sacrificing performance

## Proposed Solution

A cross-platform application built with Ionic, using multi-factor authentication and end-to-end encryption. Features include multi-exchange integration, real-time transaction processing, one-time and recurring investment plans, market data and analytics integration, single-transaction multi-currency trading, and price-based exchange comparison surfacing the best available price in real time.

## Services Delivered

Design · Development · Quality Assurance · Project Management. See `services.md`.

## Technology Stack

| Layer | Technologies |
|---|---|
| Mobile | Ionic, Angular |
| Backend | .NET, C# |
| Database | MS SQL Server |
| Frontend | jQuery, HTML5, CSS |
| Security | Multi-factor authentication, end-to-end encryption |
| Integration | Multiple exchange APIs, market data and analytics platforms |

## Architecture Summary

An Ionic cross-platform client over a .NET backend with SQL Server. The backend brokers connections to multiple exchange APIs and market data providers, with a price comparison layer surfacing the best available rate across exchanges in real time. Encryption applied end to end.

## Team Composition

| Role | Count |
|---|---|
| Total team | **3** |
| Composition | Design, development, QA, project management across 3 people |

## Project Timeline

| Phase | Detail |
|---|---|
| Total duration | **5 months** |
| Engagement model | **Fixed Price** |

Zediant's smallest and fastest documented delivery, and one of only two documented fixed-price engagements.

## Business Outcomes

Recorded outcomes:

- **4.9 rating on Google Play**
- **4.4 rating on the App Store**
- Praised for fluid performance and a near-native cross-platform experience
- Independent third-party security audit approval obtained

## Technical Outcomes

| Dimension | Outcome |
|---|---|
| Performance | Near-native experience from a cross-platform framework; noted in user reviews |
| Automation | One-time and recurring investment plans |
| Scalability | Not documented |
| Security | MFA, end-to-end encryption, independent third-party security audit approval |
| Maintainability | Single cross-platform codebase |

## Customer Benefits

A credible, secure product in a category where trust is the barrier to adoption, delivered in five months by three people at fixed price. Users can compare prices across exchanges and transact in multiple currencies at once.

## Challenges During Delivery

**Assumption** — not documented. Fixed-price delivery in a regulated-adjacent category with multiple third-party exchange integrations is commercially demanding; scope control would have been essential.

## Best Practices

- Design for independent security audit from day one rather than remediating afterwards
- Cross-platform can achieve near-native performance when the framework choice matches the use case
- Fixed price works when scope is genuinely definable — this engagement had a clear feature set
- A small senior team can outperform a larger mixed one on a well-defined build

## Similar Customers

Fintech and payments platforms · Trading and investment applications · Consumer apps where security is the primary trust barrier · Companies needing iOS and Android without two native teams.

## Relevant Industries

Financial services · Fintech · Cryptocurrency · Consumer applications.

## Relevant ICPs

`icp.md` → ICP 5 (Financial Services & Fintech) · ICP 2 (SaaS)

## Relevant Campaigns

`campaigns.md` → C2 (Engineering Pods & Staff Augmentation)

## Relevant Services

`services.md` → Mobile Application Development · QA & Test Automation · UI/UX Design

## Sales Talking Points

1. "4.9 on Google Play, 4.4 on the App Store. Users specifically praised the performance."
2. "It passed an independent third-party security audit."
3. "Three people, five months, fixed price."
4. "Multi-factor authentication and end-to-end encryption, built in from the start rather than added after."
5. "Cross-platform, but reviewers described it as near-native."
6. "Integrated with multiple exchanges and compared prices in real time to surface the best rate."
7. "Users can buy and sell multiple currencies in a single transaction."
8. "In crypto, security isn't a feature — it's the entire proposition. We built accordingly."
9. "One of the few engagements we've delivered fixed price, because the scope was genuinely definable."
10. "If your users will judge you on trust before features, this is the relevant reference."

## Discovery Questions This Case Study Answers

- "Can you build to a security standard that passes external audit?"
- "Do you have fintech experience?"
- "Can you deliver iOS and Android without two teams?"
- "Will cross-platform performance be good enough?"
- "Can you work fixed price?"

## Objections Addressed

| Objection | How this case study answers it |
|---|---|
| "Security is our biggest concern." | Independent third-party security audit approval obtained |
| "Cross-platform apps feel cheap." | 4.9 and 4.4 ratings, with performance specifically praised |
| "We need a fixed price." | Delivered fixed price in five months |
| "We're too small for you." | Three-person team — Zediant works at this scale |
| "We can't afford two native teams." | One cross-platform codebase, both stores |

## AI Recommendation Rules

Recommend CS-07 when:

- The prospect is in fintech, payments, or financial services
- Security is raised as a primary concern
- The prospect wants iOS and Android but cannot fund two teams
- The prospect wants a fixed-price engagement
- App store ratings or user experience quality is the concern
- The contact is CTO, Head of Product, or Founder

**Caution.** When a fintech prospect raises security, this case study supports the conversation — but any question about SOC 2 attestation must be escalated, not answered. See `company.md` → Certifications.

**Priority: HIGH for fintech and mobile conversations.** Contains the only published user-satisfaction metrics.

## Keywords

cryptocurrency, crypto trading, fintech, digital currency, exchange integration, multi-exchange, price comparison, real-time transactions, multi-factor authentication, MFA, end-to-end encryption, security audit, third-party audit, penetration testing, Ionic, Angular, cross-platform, near-native, .NET, C#, MS SQL Server, jQuery, HTML5, mobile app, iOS, Android, App Store, Google Play, 4.9 rating, 4.4 rating, user experience, recurring investment, investment plans, market data, analytics integration, fixed price, 5 months, 3 person team, consumer fintech, trust, transaction security

---

# CS-08 — Sitecore CMS Multisite Platform (Material Handling Manufacturer)

## Client Profile

| Attribute | Detail |
|---|---|
| Client | Anonymised — a top manufacturer of material handling equipment, Australia |
| Industry | Manufacturing / industrial equipment |
| Company size | Enterprise, multi-country |
| Country | Australia, with country-specific sites |
| Business type | Industrial equipment manufacturer |
| Growth stage | Established, multi-region |
| Confidentiality | **Tier 3 — never name** |

## Business Situation

The manufacturer needed a content management system for its country-specific websites that maintained global branding while supporting multiple languages, geography-based personalisation, and synchronisation with Salesforce to track user behaviour, under standardised security.

## Customer Challenges

- Country-specific sites inconsistent with global branding
- Multiple languages requiring management
- No personalisation by geography or user behaviour
- User behaviour and leads not reaching Salesforce without manual work
- No standardised security across sites
- Marketing dependent on developers for content changes

## Technical Challenges

- Enterprise CMS supporting multi-language and multi-site governance
- Behavioural personalisation
- Bidirectional Salesforce synchronisation eliminating manual intervention
- Marketing automation integrated into the platform
- Architecting for future e-commerce alongside current CMS requirements
- Standardised security across a distributed site estate

## Existing Environment

Fragmented country-specific websites, Salesforce CRM operating separately, manual lead handling.

## Project Goals

- Consistent global branding with locally relevant content
- Content management moved in-house to marketing
- Automatic lead and behaviour sync to Salesforce
- Personalisation by user behaviour and geography
- A foundation supporting planned e-commerce

## Proposed Solution

A Sitecore-based multisite platform, architected with the client's future e-commerce plans in view rather than only the immediate CMS requirement. Delivered personalisation by behaviour and preference, Salesforce synchronisation removing manual handoff, and built-in marketing automation for campaign management and effectiveness measurement.

## Services Delivered

Design · Development · Quality Assurance · Project Management. See `services.md`.

## Technology Stack

| Layer | Technologies |
|---|---|
| CMS | Sitecore |
| Backend | .NET, C# |
| Database | MS SQL |
| Frontend | jQuery, HTML5, CSS |
| Cloud | AWS |
| Integration | Salesforce |

## Architecture Summary

A Sitecore multisite instance serving country-specific sites from shared templates and a common component library, with locale-specific content and behavioural personalisation rules. A Salesforce integration layer synchronises user behaviour and leads bidirectionally. Hosted on AWS. Architected so commerce capability could be added without re-platforming.

## Team Composition

| Role | Count |
|---|---|
| Total team | **5** |
| Composition | Design, development, QA, project management |

## Project Timeline

| Phase | Detail |
|---|---|
| Total duration | **6 months** |
| Engagement model | **Fixed Price** |

## Business Outcomes

Recorded outcomes:

- **30% increase in website traffic** (company-stated)
- Content managed in-house, removing developer dependency
- Better data-driven analytics
- A strong foundation for continued digital growth

## Technical Outcomes

| Dimension | Outcome |
|---|---|
| Performance | Not documented |
| Automation | Salesforce sync eliminating manual lead handoff; marketing automation built in |
| Scalability | Multisite architecture extensible to further countries; e-commerce-ready |
| Security | Standardised security across the site estate |
| Maintainability | Marketing manages content without developer involvement |

## Customer Benefits

Marketing gained independence from development for routine changes. Global brand consistency was achieved without removing local relevance. Leads reach Salesforce automatically. The platform will not need replacing when e-commerce is added.

## Challenges During Delivery

**Assumption** — not documented. Multi-country CMS projects are consistently gated by content migration volume and local stakeholder alignment on governance.

## Best Practices

- Architect for the client's stated next phase, not just the current brief — this is why the platform is e-commerce-ready
- Establish the CRM integration during the build; retrofitting lead sync is significantly harder
- Multi-site governance is an organisational problem as much as a technical one — agree who owns what before building
- Content migration should be scoped and owned explicitly; it is the usual cause of overrun

## Similar Customers

Multi-country manufacturers · Industrial equipment brands · Organisations with local marketing autonomy and global brand requirements · Companies planning e-commerce on an existing content estate.

## Relevant Industries

Manufacturing & industrial · Automotive · Retail & e-commerce · B2B distribution.

## Relevant ICPs

`icp.md` → ICP 6 (Manufacturing & Industrial) · ICP 8 (Retail & E-commerce)

## Relevant Campaigns

`campaigns.md` → C2 (Engineering Pods & Staff Augmentation, primary — CMS delivered within a pod) · C4 (Middleware & API Integration (ZCoupler), secondary — Salesforce sync)

## Relevant Services

`services.md` → E-commerce & CMS Development · Integration & Middleware Engineering · Web Application Development

## Sales Talking Points

1. "Website traffic rose 30% after launch."
2. "Marketing now manages content in-house. No developer ticket for a text change."
3. "Sitecore multisite across country-specific sites, with consistent global branding and local personalisation."
4. "Leads and user behaviour sync to Salesforce automatically — the manual handoff is gone."
5. "We architected for their e-commerce plans, not just the CMS brief. They won't need to replatform."
6. "Five people, six months, fixed price."
7. "Personalisation by behaviour and geography, not just language switching."
8. "Marketing automation built into the platform for campaign tracking and measurement."
9. "Sitecore expertise is uncommon at our size — it's usually the large integrators or nobody."
10. "Standardised security across every country site, not per-site improvisation."

## Discovery Questions This Case Study Answers

- "Have you done enterprise CMS, not just WordPress?"
- "Can you handle multi-country and multi-language?"
- "Can you integrate CMS with our CRM?"
- "Can marketing manage content without developers?"
- "Will this support e-commerce later?"

## Objections Addressed

| Objection | How this case study answers it |
|---|---|
| "We need enterprise CMS, not open source." | Sitecore delivered for a multi-country manufacturer |
| "We'd need to replatform again for e-commerce." | Architected for commerce from the start |
| "Our marketing team can't use complex systems." | Content moved in-house post-launch |
| "Our leads get lost between web and sales." | Automatic Salesforce sync, no manual intervention |
| "We need a fixed price." | Delivered fixed price in six months |

## AI Recommendation Rules

Recommend CS-08 when:

- The prospect runs multiple country or brand websites
- Enterprise CMS (Sitecore, Optimizely) is in scope
- CMS-to-CRM integration is required
- Marketing's developer dependency is the stated pain
- The prospect is a manufacturer or industrial brand
- The contact is Head of Digital, Head of Marketing, CIO, or IT Director

**Priority: HIGH for CMS and manufacturing conversations.** Contains one of only two published percentage outcomes.

## Keywords

Sitecore, enterprise CMS, multisite, multi-language, multi-region, content management, personalisation, behavioural targeting, geography-based content, Salesforce integration, CRM sync, lead capture, marketing automation, campaign tracking, global branding, brand consistency, in-house content management, developer dependency, website traffic increase, 30% traffic, .NET, C#, MS SQL, jQuery, HTML5, AWS, material handling, industrial equipment, manufacturer, Australia, e-commerce ready, digital experience platform, DXP, content governance, standardised security, fixed price, 6 months

---

# CS-09 — BigCommerce Integration for Australia's Largest Office Supply Brand

## Client Profile

| Attribute | Detail |
|---|---|
| Client | Anonymised — Australia's biggest office supply brand |
| Industry | Retail / B2B and B2C office supplies |
| Company size | Enterprise |
| Country | Australia |
| Business type | Multi-channel retailer serving both business and consumer customers |
| Growth stage | High growth |
| Confidentiality | **Tier 3 — never name** |

## Business Situation

The brand needed an e-commerce platform capable of supporting rapid growth while serving both B2B and B2C customers with different pricing structures.

## Customer Challenges

- Serving B2B and B2C customers with distinct pricing from one platform
- Platform needing to support significant growth
- High traffic and large sales volumes
- User experience not meeting expectations

## Technical Challenges

- Differentiated B2B and B2C pricing logic
- High-traffic, high-volume transaction handling
- Platform integration into existing e-commerce operations

## Existing Environment

Existing e-commerce operation; specific prior platform not published.

## Project Goals

- Improve user experience
- Streamline B2B and B2C pricing
- Support growth in traffic and sales volume

## Proposed Solution

BigCommerce integrated into the brand's e-commerce platform.

## Services Delivered

E-commerce & CMS Development · Integration Engineering. See `services.md`.

## Technology Stack

| Layer | Technologies |
|---|---|
| E-commerce | BigCommerce |
| Supporting | Zediant's documented BigCommerce capability is rated expert-level in the internal skill matrix |

Detailed stack not published.

## Architecture Summary

BigCommerce as the commerce platform with B2B/B2C pricing differentiation. Detailed architecture not published — do not describe beyond this.

## Team Composition

Not published. **Do not state a team size.**

## Project Timeline

Not published. **Do not state a duration.**

## Business Outcomes

Recorded outcomes, qualitative:

- User experience greatly improved
- B2B and B2C pricing structure streamlined
- Supported the brand's substantial growth
- Platform handled high traffic and large sales volumes

**No figures published.** Do not invent them.

## Technical Outcomes

| Dimension | Outcome |
|---|---|
| Performance | Handled high traffic and large sales volumes |
| Automation | Pricing structure streamlined across customer types |
| Scalability | Supported the brand's growth |
| Security | Not documented |
| Maintainability | Not documented |

## Customer Benefits

One platform serving two customer types with appropriate pricing, capable of absorbing growth without degradation.

## Challenges During Delivery

Not documented.

## Best Practices

- B2B and B2C on one platform requires the pricing model resolved before the build, not during
- Platform selection should be driven by peak-load capability, not feature checklists

## Similar Customers

Multi-channel retailers · B2B and B2C hybrid businesses · High-growth e-commerce operators · Distributors with tiered customer pricing.

## Relevant Industries

Retail & e-commerce · B2B distribution · Office and industrial supplies.

## Relevant ICPs

`icp.md` → ICP 8 (Retail & E-commerce)

## Relevant Campaigns

`campaigns.md` → C2 (Engineering Pods & Staff Augmentation)

## Relevant Services

`services.md` → E-commerce & CMS Development · Integration & Middleware Engineering

## Sales Talking Points

1. "We delivered the BigCommerce platform for Australia's largest office supply brand."
2. "B2B and B2C on one platform, with pricing structures that actually differ by customer type."
3. "It handled high traffic and large sales volumes through a period of significant growth."
4. "BigCommerce is one of our expert-rated platforms, not a first attempt."
5. "Australian retail delivery — we know the market and the trading calendar."

## Discovery Questions This Case Study Answers

- "Have you delivered BigCommerce at scale?"
- "Can you handle B2B and B2C pricing on one platform?"
- "Have you worked with Australian retailers?"
- "Will the platform cope with our peak volumes?"

## Objections Addressed

| Objection | How this case study answers it |
|---|---|
| "We need B2B and B2C on one site." | Documented on this engagement |
| "Our volumes are high." | Australia's largest office supply brand |
| "Have you worked in Australia?" | Yes, in retail specifically |

## AI Recommendation Rules

Recommend CS-09 when:

- The prospect runs B2B and B2C from one platform
- BigCommerce is under consideration
- The prospect is an Australian retailer
- Peak-volume capability is the concern
- The contact is E-commerce Director, Head of Digital, or CIO

**Priority: MEDIUM.** Strong logo credibility, but thin published detail. Do not over-elaborate.

## Keywords

BigCommerce, e-commerce, e-commerce integration, replatforming, B2B e-commerce, B2C e-commerce, hybrid commerce, tiered pricing, pricing structure, office supplies, Australian retail, high traffic, high volume, peak load, sales volume, growth support, user experience, multi-channel retail, catalogue management, online store, commerce platform

---

# CS-10 — WordPress Migration for an Online Poker Platform

## Client Profile

| Attribute | Detail |
|---|---|
| Client | Anonymised — an online poker game website |
| Industry | Online gaming |
| Company size | Not published |
| Country | Not published |
| Business type | Consumer gaming platform |
| Growth stage | Not published |
| Confidentiality | **Tier 3 — never name** |

## Business Situation

The website's backend was not functioning smoothly, content updates were difficult, SEO performance was poor, and load times were degrading user experience.

## Customer Challenges

- Backend functions not operating smoothly
- Content updates difficult and slow
- Poor SEO performance limiting organic traffic
- Slow page load harming user experience

## Technical Challenges

- Migrating an existing site to WordPress without losing content or rankings
- Improving SEO compatibility
- Reducing load time

## Existing Environment

Prior platform not published.

## Project Goals

- Stabilise backend operation
- Make content updates straightforward
- Improve SEO compatibility and organic traffic
- Reduce page load time

## Proposed Solution

Migration of the website to WordPress.

## Services Delivered

E-commerce & CMS Development · Web Application Development. See `services.md`.

## Technology Stack

WordPress. Detailed stack not published.

## Architecture Summary

WordPress-based content platform. Detailed architecture not published.

## Team Composition

Not published. **Do not state a team size.**

## Project Timeline

Not published. **Do not state a duration.**

## Business Outcomes

Recorded outcomes, qualitative:

- Backend functions operating smoothly
- Content updates significantly easier
- SEO compatibility greatly improved, producing higher organic traffic
- Load time reduced, improving user experience

**No figures published.**

## Technical Outcomes

| Dimension | Outcome |
|---|---|
| Performance | Load time reduced |
| Automation | Content updates simplified |
| Scalability | Not documented |
| Security | Not documented |
| Maintainability | Content manageable without developer involvement |

## Customer Benefits

A site the team can update themselves, that loads faster and ranks better.

## Challenges During Delivery

Not documented. **Assumption**: SEO-preserving migration always requires redirect mapping; ranking loss is the standard risk.

## Best Practices

- Plan redirects before migration — organic traffic is the asset most easily destroyed by replatforming
- Measure load time and rankings before and after so improvement is demonstrable

## Similar Customers

Content-heavy consumer sites · Gaming and entertainment platforms · Businesses whose organic traffic is commercially critical · Organisations replatforming from bespoke CMS to WordPress.

## Relevant Industries

Online gaming · Media & entertainment · Consumer internet.

## Relevant ICPs

`icp.md` → ICP 3 (Product Companies). Note: media & entertainment is a Tier 3 industry in `icp.md` — do not build campaigns around this case study.

## Relevant Campaigns

`campaigns.md` → C2 (Engineering Pods & Staff Augmentation)

## Relevant Services

`services.md` → E-commerce & CMS Development · Web Application Development

## Sales Talking Points

1. "We migrated an online poker platform to WordPress — backend stability, faster loads, better SEO."
2. "Organic traffic rose after the migration because SEO compatibility improved."
3. "Content updates stopped being a developer task."
4. "Load time came down, which showed up directly in user experience."

## Discovery Questions This Case Study Answers

- "Can you migrate us to WordPress without losing rankings?"
- "Can you improve our page load times?"
- "Can you make content updates easier for our team?"

## Objections Addressed

| Objection | How this case study answers it |
|---|---|
| "We'll lose our SEO if we migrate." | SEO compatibility improved and organic traffic rose |
| "Our site is slow." | Load time reduced |
| "Updating content requires a developer." | Resolved through the migration |

## AI Recommendation Rules

Recommend CS-10 when:

- The prospect is migrating to WordPress
- SEO preservation during migration is the concern
- Site performance or load time is the stated problem
- Content update friction is the pain

**Priority: LOW.** Thin detail, small engagement, and the industry is Tier 3. Use only when directly relevant; never as a lead credibility proof point.

## Keywords

WordPress, WordPress migration, CMS migration, replatforming, SEO, SEO compatibility, organic traffic, page load time, site performance, content management, content updates, backend stability, online gaming, poker platform, consumer website, redirect mapping, user experience

---

# CASE STUDY MATRIX

| ID | Case Study | Industry | Business Problem | Key Technology | Services | Campaign | ICP | Priority |
|---|---|---|---|---|---|---|---|---|
| CS-01 | Middleware Integration for Multiple Large DMS | Automotive | Siloed data across incompatible systems | Java, Spring, JMS, ActiveMQ | Integration & Middleware | C4 | 4, 3, 7 | **Highest** |
| CS-02 | Wholesale Parts CRM | Automotive / SaaS | No CRM for dealer sales and service reps | .NET, Swift, MS SQL | Pods, Mobile, Integration | C2, C4 | 4, 3, 2 | High |
| CS-03 | Lubricant Recommendation Application | Automotive / Industrial | Paper-based specification management | Spring, Hibernate, Ionic | Web, Mobile, Integration | C2, C4 | 4, 6, 3 | High |
| CS-04 | 11Wickets Scalability | Gaming / Consumer | Infrastructure failing under concurrency | AWS, MySQL Galera | Platform Engineering | C3 | 2, 3, 8 | **Highest (named)** |
| CS-05 | Zakaa Executive Dashboards | Consultancy / Energy | Fragmented manual KPI reporting | Python, Oracle, ReactJS | Data Engineering, Integration | C4 | 9, 1, 6 | High |
| CS-06 | Team Augmentation for Automotive Software | Automotive / SaaS | Acquired software with no internal expertise | .NET, Angular, AWS, CircleCI | Staff Aug, Pods, QA, DevOps | C2, C3 | 3, 2, 4 | **Highest** |
| CS-07 | Cryptocurrency Trading Application | Fintech | Security and trust in a low-trust category | Ionic, .NET, MS SQL | Mobile, QA, Design | C2 | 5, 2 | High |
| CS-08 | Sitecore CMS Multisite | Manufacturing | Fragmented multi-country digital estate | Sitecore, .NET, Salesforce | CMS, Integration | C2, C4 | 6, 8 | High |
| CS-09 | BigCommerce Office Supply Brand | Retail | B2B and B2C pricing on one platform | BigCommerce | E-commerce | C2 | 8 | Medium |
| CS-10 | WordPress Poker Platform Migration | Online gaming | Slow, hard-to-update, poorly ranking site | WordPress | CMS, Web | C2 | 3 | Low |

---

# INDUSTRY MAPPING

| Industry | Primary Case Studies | Secondary | Notes |
|---|---|---|---|
| **Automotive & dealer networks** | CS-01, CS-02 | CS-03, CS-06 | Deepest evidence. CS-02 and CS-06 are the same client — use one |
| **SaaS / software product** | CS-06, CS-04 | CS-02, CS-07 | CS-06 for longevity, CS-04 for scaling |
| **Fintech & payments** | CS-07 | CS-04 (write-heavy parallels) | Escalate SOC 2 questions |
| **Manufacturing & industrial** | CS-08, CS-03 | CS-05 | CS-08 for digital estate, CS-03 for specification data |
| **Retail & e-commerce** | CS-09, CS-08 | CS-04 (peak load) | CS-09 for B2B/B2C, CS-08 for multi-site |
| **Logistics & supply chain** | CS-01 (structurally analogous) | CS-05 | **No direct logistics case study.** Be honest about this |
| **Energy, oil & gas** | CS-05 | — | Subject to the CS-05 source discrepancy |
| **Gaming & consumer internet** | CS-04 | CS-10 | CS-04 is nameable |
| **Professional services / consultancy** | CS-05 | — | Consultancy as a channel, per the aggregator model |
| **Healthcare, education, construction** | **None** | — | No case studies. Do not imply experience |

---

# TECHNOLOGY MAPPING

| Technology | Case Studies |
|---|---|
| **.NET / C#** | CS-02, CS-06, CS-07, CS-08 |
| **Java / Spring / Hibernate** | CS-01, CS-03 |
| **JSP / EJB / JMS / ActiveMQ** | CS-01, CS-03 |
| **Python** | CS-05 |
| **Node.js** | None documented |
| **React / ReactJS** | CS-05 |
| **Angular / AngularJS** | CS-01, CS-02, CS-03, CS-06, CS-07 |
| **jQuery** | CS-02, CS-07, CS-08 |
| **SignalR** | CS-06 |
| **Swift / Objective-C** | CS-02, CS-03, CS-06 |
| **Ionic** | CS-03, CS-07 |
| **MS SQL Server** | CS-02, CS-03, CS-06, CS-07, CS-08 |
| **Oracle** | CS-05 |
| **MySQL / Galera** | CS-04 |
| **NoSQL** | CS-01 |
| **Entity Framework / LINQ** | CS-02, CS-06 |
| **AWS** | CS-04, CS-06, CS-08 |
| **CircleCI** | CS-06 |
| **Sitecore** | CS-08 |
| **BigCommerce** | CS-09 |
| **WordPress** | CS-10 |
| **Salesforce integration** | CS-08 |
| **REST / JAX-RS** | CS-01, CS-05 |
| **Test automation** | CS-06 (70%→93%) |
| **Kubernetes / Docker / Terraform** | **None documented** — capability claimed in `services.md` but no case study evidence |
| **OpenAI / LangChain / RAG** | **None documented** — no AI product case study exists |

---

# SERVICE MAPPING

| Service | Case Studies | Strength of proof |
|---|---|---|
| Dedicated Engineering Pods | CS-02, CS-06 | Strong — 12-person/18-month and 3+ year engagements |
| Staff Augmentation | CS-06 | Strong |
| Integration & Middleware Engineering | CS-01, CS-02, CS-05, CS-08 | **Strongest in the portfolio** |
| Enterprise Custom Development | CS-01, CS-02, CS-05 | Strong |
| Platform Engineering & Cloud DevOps | CS-04, CS-06 | Moderate |
| Legacy Modernisation | CS-06 (acquired codebase) | Moderate — no full monolith-to-microservices case study |
| Mobile Application Development | CS-02, CS-03, CS-06, CS-07 | Strong — includes published ratings |
| Web Application Development | CS-03, CS-05, CS-10 | Moderate |
| E-commerce & CMS Development | CS-08, CS-09, CS-10 | Strong |
| QA & Test Automation | CS-06 | Moderate — one strong metric (70%→93%) |
| Data Engineering & Analytics | CS-05 | **Thin — single case study** |
| Maintenance & Managed Services | CS-06 | Moderate — evidenced by 3+ year duration |
| Advisory & Consulting | CS-02 (roadmap), CS-04 | Moderate |
| UI/UX Design | CS-03, CS-07 | **Thin** |
| AI-Enabled Product Engineering | **None** | **No case study exists.** Never imply otherwise |

---

# CAMPAIGN MAPPING

| Campaign | Primary Case Study for Email 2 | Alternatives | Selection note |
|---|---|---|---|
| **C1 — AI-Enabled Product Engineering** | **None — no case study exists.** Never imply otherwise. | — | Per the Service Mapping table above. Note: `services.md`'s AI-Enabled Product Engineering section cross-references CS-07/CS-02 as "Relevant Case Studies" — that conflicts with this document's own Service Mapping table. Flag to a human; do not resolve unilaterally. |
| **C2 — Engineering Pods & Staff Augmentation** | CS-06 (70%→93%, 3+ years) | CS-02 (12-person/18-month), CS-03, CS-07, CS-08, CS-09, CS-10 | Folds in Mobile, Web, E-commerce/CMS, and QA, all "delivered within a pod" per `services.md` |
| **C3 — Platform Engineering & Cloud Modernization** | CS-04 (nameable, scaling) | CS-06 (DevOps introduction angle) | CS-04 is the safest — publicly named and directly about scaling |
| **C4 — Middleware & API Integration (ZCoupler)** | CS-01 (integration — strongest proof in the portfolio) | CS-05, CS-08, CS-02 | Select by vertical |
| **C5 — Enterprise Custom Development & Modernization** | CS-01 or CS-05 | CS-02, CS-06 (legacy/acquired-codebase angle) | Select by vertical; overlaps with C4 since integration evidence doubles as enterprise custom development evidence |

---

# DECISION MAKER MAPPING

| Job Title | Primary Case Studies | What resonates |
|---|---|---|
| **CTO** | CS-06, CS-04, CS-01 | Test coverage, architecture decisions, technical specificity |
| **VP Engineering / Head of Engineering** | CS-06, CS-04 | Team ownership, delivery infrastructure, DevOps introduction |
| **Engineering Manager** | CS-06 | Sprint cadence, test coverage, onboarding speed |
| **Founder / CEO** | CS-02, CS-04, CS-07 | Adoption numbers, ratings, business outcomes |
| **COO (agency)** | CS-06, CS-05 | Continuity, long-term relationships, white-label delivery |
| **Managing Director (agency)** | CS-05, CS-09 | Client-facing delivery, capacity, brand-safe execution |
| **CIO** | CS-01, CS-05, CS-08 | Governance, integration, role-based access, security |
| **IT Director / IT Manager** | CS-01, CS-08 | System consolidation, reduced manual effort |
| **Enterprise Architect** | CS-01, CS-05 | Architecture patterns, adapter design, modularity |
| **Head of Product** | CS-02, CS-07, CS-03 | Feature delivery, user ratings, adoption |
| **Head of Digital / Marketing** | CS-08, CS-09, CS-10 | Traffic, content independence, CRM sync |
| **CFO** | CS-05 | Reporting latency, manual effort cost |
| **Operations Head** | CS-03, CS-01 | Manual process elimination |
| **CISO / Head of Compliance** | CS-07 | Independent security audit — **escalate SOC 2 questions** |
| **QA Lead / SDET** | CS-06 | 70%→93% coverage, test automation without a QA team |
| **Head of Infrastructure / DevOps Lead** | CS-04, CS-06 | AWS scaling, Galera clustering, DR and staging |

---

# AI RETRIEVAL RULES

## Selection algorithm

Apply in order. Stop at the first decisive match.

```
1. Does the prospect need a NAMEABLE reference?
   → CS-04 (11Wickets) or CS-05 (Diamond / Zakaa)
   These are the only Tier 1 clients. Everything else must stay anonymised.

2. Does the prospect's BUSINESS PROBLEM match a case study exactly?
   → Select on problem match. This outranks industry match.
     Systems not talking to each other      → CS-01
     Acquired software nobody understands   → CS-06
     Platform failing under load            → CS-04
     Manual/paper process                   → CS-03
     Fragmented management reporting        → CS-05
     Multi-country digital estate           → CS-08
     Security as the trust barrier          → CS-07
     B2B and B2C pricing on one platform    → CS-09

3. Does the INDUSTRY match?
   → Use INDUSTRY MAPPING. Prefer same-vertical proof.

4. Does the TECHNOLOGY match?
   → Use TECHNOLOGY MAPPING. Useful with technical personas who
     will ask "have you worked with X?"

5. Does COMPANY SIZE match?
   Enterprise prospect  → CS-02, CS-06, CS-08, CS-09
   Mid-market prospect  → CS-03, CS-05, CS-08
   Smaller prospect     → CS-07 (3 people), CS-04

6. Match to DECISION MAKER
   → Use DECISION MAKER MAPPING to select the framing, not the case study

7. Match to CAMPAIGN
   → Use CAMPAIGN MAPPING for the default Email 2 proof point
```

## Hard rules

| Rule | Detail |
|---|---|
| **Never name a Tier 3 client** | Describe by category only |
| **Never use CS-02 and CS-06 together** | Same client; presenting both overstates diversity |
| **Never invent metrics** | Only these figures are published: 50+ dealers, 5,700 customers, 23+ lubricant companies, 70%→93% coverage, 4.9 / 4.4 ratings, 30% traffic increase, 186 countries / 50 OEMs / 250,000 professionals |
| **Never attach 99.99% availability to CS-04** | That website claim is unsupported and unrelated to this engagement |
| **Never imply AI product delivery** | No AI product case study exists |
| **Never imply healthcare, education, or construction experience** | No case studies |
| **Never claim Kubernetes, Docker, Terraform, or RAG delivery** | Capability is claimed in `services.md` but no case study evidences it |
| **One case study per email** | Two proof points in one message dilutes both |
| **Escalate SOC 2 questions** | Even when CS-07's security audit makes the conversation go well |

## When no case study fits

Say so. Zediant's internal guidance is explicit that honest scoping builds more credibility than overstatement. The correct response is: *"We haven't done exactly that. The closest is [X], which shares [specific structural similarity]. Happy to talk through whether that transfers."*

---

# DOCUMENT CONTROL

| Attribute | Value |
|---|---|
| Document | `case_studies.md` |
| Purpose | Case study retrieval for AI sales, proposal, and meeting-prep agents |
| Case studies documented | 10 |
| Nameable clients | 2 (11Wickets, Diamond Professional Consultants / Zakaa Innovation Hub) |
| Testimonial clients | 4 (Networx, STAGER, Zwick Roell, DIJGTAL) |
| Sources | zediant.com case studies (10 pages), Zediant Company Profile 2026, Zediant Sales Bible v1.0, 12-Month Sales & Growth Strategy |
| Last verified | August 2026 |

## Published metrics — the complete list

These are the only quantified outcomes Zediant can evidence. Nothing beyond this list may be stated as a client outcome.

| Metric | Case study |
|---|---|
| 50+ dealers, 5,700 customers | CS-02 |
| 23+ lubricant companies | CS-03 |
| Test coverage 70% → 93% | CS-06 |
| Developer's manual delivered in 1 month | CS-06 |
| 3+ year relationship | CS-06 |
| 4.9 Google Play / 4.4 App Store | CS-07 |
| 30% website traffic increase | CS-08 |
| Client scale: 186 countries, 50 OEMs, 250,000+ professionals | CS-02, CS-06 |

## Open items requiring human confirmation

1. **CS-05 industry discrepancy** — Company Profile says Oil & Gas; website says Diamond Professional Consultants, a consultancy. Same engagement or two? Affects `icp.md` → ICP 9, whose only proof this is.
2. **CS-02 and CS-06 are the same client** — confirm, and decide which to lead with.
3. **CS-03 possible link to the "10-month UAE project"** referenced in internal strategy as a delivery-delay example. Confirm before using as a speed proof point.
4. **Team composition and timelines missing** for CS-01, CS-04, CS-09, CS-10.
5. **Three website errors** — 11Wickets meta description, financial-sector line in the automotive case study, 11Wickets industry labelled "Cloud Solutions."
6. **No logistics, healthcare, education, or construction case studies** despite some being listed as focus industries in the company profile.
7. **No AI product case study** despite AI-Enabled Product Engineering being a headline service.
8. **No case study evidences Kubernetes, Docker, Terraform, or modern AI tooling** in client delivery.

## Handling rules for AI agents

1. Items marked **Assumption** are inferences. Never present them as fact.
2. Respect the three confidentiality tiers absolutely.
3. Never name the concentrated-account clients identified in internal documents.
4. Use only the published metrics listed above.
5. One case study per outreach message.
6. Where a case study has no published team size or duration, say it is not published rather than estimating.
7. Escalate any SOC 2 attestation request regardless of how the conversation is going.
8. When nothing fits, say so and offer the nearest structural parallel.

## Related Context Files

| File | Relationship |
|---|---|
| `company.md` | Capability claims these case studies do and do not evidence |
| `services.md` | Service definitions; see Service Mapping for which have proof |
| `icp.md` | Segment and vertical definitions; CS-05 affects ICP 9 |
| `campaigns.md` | Campaign structures; see Campaign Mapping for Email 2 proof selection |
| `competitors.md` | Alternatives these proof points are competing against |
| `pricing.md` | Engagement models and deal sizes referenced per case study |
