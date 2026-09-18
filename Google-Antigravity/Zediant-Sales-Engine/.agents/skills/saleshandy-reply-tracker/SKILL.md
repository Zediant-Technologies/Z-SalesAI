---
name: "saleshandy-reply-tracker"
description: "Zediant's lightweight reply monitoring for Saleshandy — fetches incoming replies and sends team alerts to the Cliq #Z-Outreach-Auto-Update channel. BDM manually updates Zoho Lead_Status to 'Engaged' after review. Runs on-demand or scheduled hourly (minimal overhead). No automatic Zoho updates. Future: event-driven when Saleshandy webhooks available. Use: 'Check Saleshandy replies' or schedule via Cowork."
metadata:
  version: "1.0"
---

# Saleshandy Reply Tracker (Lightweight)

Fetch incoming replies from Saleshandy and alert the team via the Cliq #Z-Outreach-Auto-Update channel. BDM manually updates Zoho Lead_Status to "Engaged".

---

## Overview

**What it does:**
1. Fetch unread replies from Saleshandy (on-demand or scheduled)
2. Match sender email to Zoho leads (for context)
3. Send team alert to the Cliq #Z-Outreach-Auto-Update channel with full reply details
4. Let BDM manually update Zoho: Lead_Status = "Engaged"
5. Hand off the reviewed engagement evidence to `ptb-scoring` for PTB calculation — this skill does not calculate PTB itself

**The one thing:** Replies are urgent. This gets them in front of your team immediately via the #Z-Outreach-Auto-Update channel.

---

## Scope

**Owns:**
- Fetching new replies from Saleshandy (on-demand or scheduled)
- Matching emails to Zoho leads (for context)
- Alerting team via the Cliq #Z-Outreach-Auto-Update channel
- Including full reply details in alert
- Capturing raw engagement evidence and making it available for `ptb-scoring`'s downstream PTB calculation

**Does not own:**
- Updating Zoho Lead_Status (BDM does manually after review)
- Responding to replies (BDM does from Saleshandy)
- Stopping sequences (Saleshandy handles automatically)
- Rescheduling or moving leads (BDM updates in Zoho)
- Calculating, re-scoring, or tiering PTB — `ptb-scoring` is the sole authority for PTB, and only acts once this skill's captured engagement evidence has been reviewed
- Managing campaign cadence or sequence configuration — cadence and sequence settings remain governed by Saleshandy/campaign configuration, not by this skill

**Note:** This is lightweight by design. BDM has full control over Zoho status updates. Future: when Saleshandy webhooks available, can make this fully event-driven.

---

## Trigger & Scheduling

**On-Demand:** 
```
"Check Saleshandy replies"
"Monitor Saleshandy for replies"
```

**Scheduled (Recommended):**
- Every hour Mon–Fri, 09:00–18:00 IST
- Or 3x daily at 10:00, 14:00, 17:00 IST
- Or on-demand only

**Why:** Catch replies quickly so BDMs can respond within hours, not days.

---

## Workflow

### Step 1: Fetch New Replies from Saleshandy

Call Saleshandy API to get unread/new replies:

```
{
  "unread_only": true,
  "status": "replied",
  "limit": 100,
  "sort": "newest_first"
}
```

**Fields to fetch:**
- Sender email
- Sender name
- Company name
- Reply timestamp
- Reply content (full text)
- Campaign/sequence ID (which C1–C5)
- Subject line of original email

**This is raw engagement evidence, not a score.** Reply Tracker captures it as-is for the Cliq alert and BDM review — it does not interpret, classify, or convert it into Engagement, Urgency Signal, Multi-threading, or Decision-maker points, and it never produces a PTB number or tier. That interpretation belongs exclusively to `ptb-scoring`, once BDM review confirms genuine engagement (see Step 4).

---

### Step 2: Match Email to Zoho Lead (Context Only)

For each reply:

1. Call `getRecords` on Zoho Leads with filter:
   ```
   Email = [reply_sender_email]
   ```

2. If found: Get Lead_Campaign_Category (which campaign)
3. If NOT found: Note as unmatched (still alert team)

**Purpose:** Enrich alert with Zoho context (for reference)

---

### Step 3: Send Team Alert to Cliq #Z-Outreach-Auto-Update Channel

Send single consolidated message to the #Z-Outreach-Auto-Update channel with **all replies**:

**Message format:**

```
📬 New Replies from Saleshandy

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

REPLY 1️⃣
From: John Doe (john@acme.com)
Company: Acme Inc
Campaign: C2 - Engineering Pods & Staff Augmentation
Timestamp: 2026-08-05 10:32 IST

Message:
"We'd be interested in learning more. Can you send over your case studies? When are you available for a call?"

Action: BDM to update Zoho Lead_Status to "Engaged"
Zoho Link: [direct link to lead record]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

REPLY 2️⃣
From: Jane Smith (jane@techco.com)
Company: TechCo Inc
Campaign: C3 - Platform Engineering & Cloud Modernization
Timestamp: 2026-08-05 10:15 IST

Message:
"Thanks for reaching out. We're currently evaluating options. Can we schedule a brief call next week?"

Action: BDM to update Zoho Lead_Status to "Engaged"
Zoho Link: [direct link to lead record]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Summary: 2 new replies | 2 campaigns affected | Action: Update Zoho status manually

Next: Review replies in the #Z-Outreach-Auto-Update channel, respond via Saleshandy, update Zoho as needed.
```

**One message per run, all replies consolidated.**

---

### Step 4: Hand Off Engagement Evidence to PTB Scoring

After the BDM reviews the alert and confirms genuine engagement, the captured reply/engagement evidence (sender, company, reply content, timestamp, campaign, subject) is made available for `ptb-scoring` to use for PTB calculation/re-scoring.

Reply Tracker's role ends at making that evidence available. It does NOT calculate PTB, assign PTB points, assign a PTB tier, apply a PTB threshold, or reject/filter a reply based on PTB. `ptb-scoring` alone performs the calculation, using its approved post-engagement model (Engagement 0–40, Urgency Signal 0–30, Multi-threading 0–15, Decision-maker Confirmed Reachable 0–15, Total 100), and any resulting PTB Score is written to CRM by `crm-update` — not by this skill.

---

## Decision Rules

| Condition | Action |
|---|---|
| Reply is new/unread | Include in Cliq alert |
| Reply is old (>24h) | Skip (assume already seen) |
| Sender email found in Zoho | Enrich alert with campaign info |
| Sender email NOT in Zoho | Still include in alert (note as "unmatched") |
| No new replies | Send message: "No new replies from Saleshandy" |

---

## Output Format

**Cliq Alert (#Z-Outreach-Auto-Update channel):**
```
📬 New Replies from Saleshandy

REPLY 1️⃣
From: [Name] ([Email])
Company: [Company]
Campaign: [C1–C5]
Timestamp: [ISO date/time]

Message:
[Full reply text]

Action: Update Zoho Lead_Status to "Engaged"
Link: [Zoho lead record]

━━━━━━━━━━━━━━━━━━━

Summary: N replies | Action: Review above, respond via Saleshandy, update Zoho manually
```

**If no replies:**
```
✅ No new replies from Saleshandy
```

---

## Efficiency Metrics

| Metric | Target |
|---|---|
| Run time (5 replies) | < 3 seconds |
| Saleshandy API calls | 1 (fetch all unread) |
| Zoho reads (for context) | 1 batch fetch |
| Cliq alerts | 1 consolidated message |
| Apollo credits used | 0 |
| Claude tokens per run | < 5K |

---

## Error Handling

| Error | Response |
|---|---|
| No new replies | Send: "✅ No new replies from Saleshandy" |
| Saleshandy connection fails | Stop, send error message to the #Z-Outreach-Auto-Update channel |
| Zoho lookup fails (context) | Still send alert, note as "context unavailable" |
| Cliq send fails | Log error (non-critical, try again on next run) |

---

## Scheduling Options

### Option A: Every Hour
- **Frequency:** Hourly Mon–Fri, 09:00–18:00 IST
- **Best for:** Good balance of responsiveness + minimal overhead
- **Cost:** Very low (1 API call/hour)

### Option B: 3x Daily
- **Frequency:** 10:00 IST, 14:00 IST, 17:00 IST
- **Best for:** Key moments (morning, mid-day, evening)
- **Cost:** Minimal (3 API calls/day)

### Option C: On-Demand Only
- **Trigger:** Manual ("Check Saleshandy replies")
- **Best for:** If you prefer to check manually
- **Cost:** Zero unless triggered

**Recommendation:** Option A (every hour) — lightweight, catches replies timely, minimal cost. Or Option C (on-demand) if you prefer manual checks via Saleshandy dashboard.

---

## Unmatched Replies

If a reply sender is not found in Zoho:

1. **Possible causes:**
   - Email address doesn't match exactly
   - Lead never made it to Zoho (failed pre-engagement qualification, ICP mismatch, was excluded as a duplicate/existing CRM record, had invalid or incomplete data, or was excluded by another existing lead-population rule — see `scheduler-lead-population`)
   - Lead was rejected/deleted from Zoho
   - Typo in Zoho email field

2. **What happens:**
   - Reply still appears in the #Z-Outreach-Auto-Update channel alert
   - Noted as "unmatched" (no campaign info enrichment)
   - BDM can manually match and update in Zoho

3. **Future enhancement:**
   - Can add fuzzy matching (partial email match) if needed
   - Or cross-reference by company name + Saleshandy sequence

---

## Cliq Channel Routing

**All reply alerts go to:** `#Z-Outreach-Auto-Update` (Channel ID: `P1064180000001095002`) — team-wide visibility

**No individual direct messages** — everyone sees all replies at once, can coordinate responses.

**Benefit:** Team transparency, no missed replies, clear audit trail.

---

## Tools Required

- `get_emails` or `list_replies` (Saleshandy API) — fetch replies
- `getRecords` (Zoho CRM) — optional, for context enrichment only
- `ZohoCliq_send_message_to_channel` (Cliq) — send to #Z-Outreach-Auto-Update channel

---

## Success Criteria

| Measure | Target |
|---|---|
| All new replies fetched | 100% |
| Cliq alert sent to #Z-Outreach-Auto-Update | 100% |
| Alert includes reply content + Zoho link | 100% |
| BDM can easily identify lead + take action | 100% |
| Response time to reply detection | < 1 hour (if running hourly) |

---

## Known Limitations

- Relies on exact email match between Saleshandy and Zoho (for context enrichment)
- No automatic Zoho updates (by design — BDM has full control)
- Polling-based (scheduled checks) vs event-driven

---

## Future Enhancements

- [ ] **Saleshandy Webhooks** (when available) — event-driven alerts instead of polling. Instant notification on reply, zero delay.
- [ ] Fuzzy email matching (catch slight variations)
- [ ] Sentiment analysis ("positive", "negative", "neutral")
- [ ] Suggested next steps based on reply content
- [ ] Auto-log reply to Zoho activity timeline (as note)

---

## Integration with Other Skills

```
Scheduler 2 (8 AM)
  ↓ Push to Saleshandy
  ↓ Leads in Saleshandy sequences (Lead_Status = "Outreach Scheduled")
  
Saleshandy Sending
  ↓ Day 0–7 email sequences
  
Reply Detected in Saleshandy
  ↓ Sequence stops automatically (Saleshandy's own behavior — campaign cadence and sequence configuration are not managed by this skill)
  
Reply-Tracker (on-demand or hourly)
  ↓ Fetch replies from Saleshandy
  ↓ Send team alert to #Z-Outreach-Auto-Update channel
  ↓ Include: reply content, company, campaign, Zoho link
  
BDM Reviews Alert
  ↓ Reads reply in #Z-Outreach-Auto-Update channel
  ↓ Opens Zoho link
  ↓ Manually updates: Lead_Status = "Engaged"
  ↓ Responds to reply via Saleshandy dashboard
  ↓ Moves lead through pipeline (Meeting Scheduled, etc.)
  
Raw Engagement Evidence (captured by Reply-Tracker, reviewed by BDM)
  ↓ Handed off to `ptb-scoring` for PTB calculation/re-scoring (see Step 4) — Reply Tracker does not calculate PTB
  ↓ PTB Score → written to CRM by `crm-update`
```

---

**Version 1.0** · August 5, 2026 · Zediant Technologies · Saleshandy Edition (Lightweight)

---

## Future: Saleshandy Webhooks

**Note:** When Saleshandy supports webhooks (incoming reply events), this skill can transition to fully event-driven:
- Saleshandy webhook triggered on reply
- Calls Claude skill instantly (no polling)
- Sends Cliq alert to #Z-Outreach-Auto-Update channel in real-time
- Zero delay, zero API overhead

Check Saleshandy documentation or contact support to confirm webhook availability. Current implementation uses polling for compatibility.

