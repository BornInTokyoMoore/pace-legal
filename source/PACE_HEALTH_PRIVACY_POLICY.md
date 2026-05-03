# Pace Consumer Health Data Privacy Policy

**Effective date:** May 3, 2026
**Last updated:** May 3, 2026
**Version:** 1.0
**Applies to:** Washington State residents and consumers whose consumer health data is collected in Washington

<!--
WHY THIS IS A STANDALONE DOCUMENT
This is Pace's standalone Consumer Health Data Privacy Policy required by the Washington My Health My Data Act, RCW 19.373.020(1)(a). The Washington Attorney General's published FAQ guidance (January 2024) states that this policy "must be a separate and distinct link" on the homepage and "may not contain additional information not required under the My Health My Data Act." This document is therefore drafted lean — it covers only what RCW 19.373.020 and 19.373.040 require, plus the closely-related FTC Health Breach Notification Rule cross-reference added in v1.1. The general Pace privacy policy (separate document, separate link) covers everything else.

STRUCTURE FOLLOWS RCW 19.373.020(1)(a) FIVE-ELEMENT REQUIREMENT:
- Section 1: categories of consumer health data and purposes (RCW 19.373.020(1)(a)(i))
- Section 2: sources of consumer health data (RCW 19.373.020(1)(a)(ii))
- Section 3: categories of consumer health data shared (RCW 19.373.020(1)(a)(iii))
- Section 4: third parties and specific affiliates (RCW 19.373.020(1)(a)(iv))
- Section 5: how to exercise consumer rights (RCW 19.373.020(1)(a)(v))
Plus rights and appeal mechanics under RCW 19.373.040 and breach notification reference under 16 CFR Part 318 in v1.1.
-->

---

## What this policy is

This Consumer Health Data Privacy Policy describes how Pace handles **consumer health data** under the Washington My Health My Data Act (RCW 19.373) for Washington State residents and any consumer whose consumer health data is collected in Washington.

Pace is operated by Born in Tokyo Digital LLC, a Minnesota limited liability company. We are a small startup, not a large company, and we treat that as a fact, not an excuse: every commitment in this policy is one we will actually meet at our scale.

This policy supplements our [general Pace Privacy Policy](https://usepace.fit/privacy). It does not replace it. The general policy describes our overall privacy practices. This policy describes only what Washington law requires for consumer health data specifically, with one closely-related federal cross-reference in Section 6.

If you are not a Washington State resident and your consumer health data was not collected in Washington, this policy does not apply to you, but the protections in our general policy do.

---

## What "consumer health data" means

Under RCW 19.373.010(8), **consumer health data** is personal information that is linked or reasonably linkable to you and that identifies your past, present, or future physical or mental health status. This includes, among other categories specifically named in the statute, body measurements, fitness and activity data, dietary information, sleep records, biometric data, and any data Pace processes to associate with or identify your health status — including data we derive or infer from non-health data.

---

## 1. Categories of consumer health data we collect, and the purposes for collection

### 1.1 Information you provide directly

We collect the following categories of consumer health data when you provide them:

- **Body measurements:** age (in whole years; we do not collect your date of birth), weight, height, biological sex
- **Activity self-assessment:** activity level (sedentary, light, moderate, active, or very active), daily step goal preference, daily sleep target preference
- **Fitness goals:** lose fat, gain muscle, maintain, or improve energy
- **Dietary information:** dietary preferences and restrictions (free text and tag-based), food allergies, food log entries (food name, portion size, time of meal, meal type), food photos you submit, photographs of nutrition labels you submit, scanned barcodes you submit, free-text food searches
- **Coaching conversation content:** any health-related information you share with the Pace coach, including symptoms, sensations, training context, recovery state, dietary patterns, or related observations
- **Exercise records:** workouts you log through the coach, including exercise name, sets, reps, weight, weight unit, RPE (rating of perceived exertion), duration, distance, and any notes you add
- **Calculated targets derived from your inputs:** daily macro targets (calories, protein, carbohydrates, fat) computed from your profile

### 1.2 Information from your iOS device (only with your authorization)

When you authorize Pace to read Apple HealthKit data through iOS, we may receive any of the following categories you've authorized:

- Step count
- Active energy burned
- Heart rate (current and daily averages)
- Heart rate variability (HRV SDNN)
- Resting heart rate
- Sleep stages (asleep, awake, REM, deep, core, in bed) and sleep duration
- Body weight history
- Workouts (workout type, start time, end time, duration, calories, distance, source app or device, and route GPS only if you separately permit it)
- Cardio fitness (VO2 max)
- Cardio recovery (heart rate recovery measured one minute after exercise)

You control which HealthKit data types are shared with Pace through iOS Settings → Privacy & Security → Health. You can change or revoke your HealthKit permissions at any time.

### 1.3 Information we derive or infer

Under RCW 19.373.010(8)(b)(viii), consumer health data includes information we derive or extrapolate from non-health data when we use that information to identify your health status. The Pace coach generates the following derived or inferred consumer health data:

- **Recovery state estimates** synthesized from sleep, HRV, and resting heart rate
- **Training-load assessments** synthesized from workout volume and recovery markers
- **Nutritional balance assessments** comparing your logged intake to your calculated targets
- **Coaching insights** combining the above into personalized guidance

We use these derived inferences only to provide the Services to you. We do not share them as a category of data separate from the source data — they exist as part of your coaching conversations and are stored alongside that content.

### 1.4 Vector embeddings

To give the coach memory across conversations, we generate **vector embeddings** of your coaching messages and stored memory summaries. A vector embedding is a numerical representation of text that encodes meaning. Pace stores both the original text and the embedding. Embeddings are themselves linked to your account, and we treat them as consumer health data input.

### 1.5 Purposes for collection

We collect and use consumer health data for these purposes, and no others:

- **To operate the Services:** display your nutrition, activity, and recovery information; generate personalized coach responses; identify food in photos you submit; track your progress over time; sync your data across your iOS devices.
- **To improve the Services:** debug failures, evaluate AI quality, review how features are used at the aggregate level. Where we use data for service improvement, we use de-identified data (as defined in Cal. Civ. Code § 1798.140(m), the most rigorous statutory definition we are aware of) wherever doing so is reasonably possible.
- **To communicate with you about your account:** respond to your support requests, deliver transactional notifications (account creation, password reset, billing receipts when applicable).
- **To comply with law:** respond to lawful regulatory or law enforcement requests and defend our legal rights.

We do not use consumer health data for advertising, marketing, profiling for purposes unrelated to the Services, or any other purpose not listed above.

### 1.6 What we do not collect

For clarity, we do not collect: precise geolocation data outside what HealthKit provides for workouts you've authorized, browsing or search history outside the app, contacts, biometric identifiers (such as fingerprints or face scans) under RCW 19.375, genetic data, gender-affirming care information, reproductive or sexual health information, mental health diagnoses, medications, or any other category of consumer health data not listed in Sections 1.1, 1.2, 1.3, or 1.4.

---

## 2. Sources of consumer health data

We collect consumer health data from these sources:

- **Directly from you,** when you create your account, complete onboarding, log food, take photos, chat with the coach, log exercise, or interact with any Pace feature.
- **From your iOS device,** specifically through Apple HealthKit, with your explicit authorization granted through iOS system permissions (one HealthKit data type at a time, per Apple's permission framework).
- **From inferences we generate from the above,** as described in Section 1.3.

We do not purchase consumer health data from data brokers, receive consumer health data from advertising networks, or obtain consumer health data from any source other than you and your authorized iOS device.

---

## 3. Categories of consumer health data we share

We share the categories of consumer health data described in Section 1 with the third parties identified in Section 4, for the purposes identified in Section 4. We share the minimum each provider needs to perform its specific function.

**We do not sell consumer health data.** Under RCW 19.373.030(2), the sale of consumer health data requires separate, written authorization from the consumer that is "separate and distinct from the consent obtained to collect or share." We have never sold consumer health data, and we have no business reason to. If we ever change that, we will obtain the separate written authorization the statute requires.

**We do not share consumer health data with advertising networks.** We do not run advertising in the Pace app. We do not use consumer health data for cross-context behavioral advertising under any state's framework.

**We do not implement a geofence around any in-person health care facility.** RCW 19.373.080 prohibits any person from implementing a geofence around an entity that provides in-person health care services for the purpose of identifying or tracking consumers, collecting consumer health data, or sending notifications related to consumer health data. Pace does not do any of these things. We do not use geofencing technology in the app.

---

## 4. Third parties and specific affiliates with whom we share consumer health data

The following named third parties receive consumer health data from Pace. We name each one explicitly because RCW 19.373.020(1)(a)(iv) requires "a list of the categories of third parties **and specific affiliates** with whom" we share — and because vague disclosure language is the disclosure failure plaintiffs' lawyers attack.

### 4.1 AI service providers (processors)

| Third party | What we send | Purpose |
|---|---|---|
| **Anthropic, PBC** (anthropic.com) | Coaching conversation text; profile and training context relevant to the question being answered; nutrition label photo bytes you submit | Anthropic's Claude model generates Pace coach responses and reads nutrition labels you photograph |
| **xAI Corp.** (x.ai) | Food photos you submit, encoded as base64 image data | xAI's Grok Vision model identifies food items in your photos and estimates nutrition information |
| **OpenAI, OpC** (openai.com) | Selected text snippets from your coaching conversations and stored memory summaries | OpenAI's text-embedding-3-small model converts the text into numerical vector embeddings, which Pace uses to retrieve relevant context across coaching conversations |
| **OpenRouter, Inc.** (openrouter.ai) | Where used as a routing layer, OpenRouter receives the same request content being transmitted to the underlying provider (currently xAI for food vision) | OpenRouter routes AI requests to the disclosed provider only. For Pace's current AI features, OpenRouter routes only to the providers expressly identified in this Section. We will not route data through OpenRouter to any other provider without first updating this policy and obtaining your affirmative consent for the new disclosure (RCW 19.373.020(1)(c)) |

**Feature-to-provider mapping for clarity:**

- Food-photo analysis requests are sent to **xAI Corp.** Where these requests pass through **OpenRouter, Inc.**, OpenRouter acts only as the routing layer to xAI as the disclosed provider.
- Coach response generation, AI-generated daily briefings, and exercise log parsing requests are sent to **Anthropic, PBC**.
- Nutrition label OCR requests are sent to **Anthropic, PBC**.
- Embedding generation requests are sent to **OpenAI, OpC**.

**About AI provider data handling.** Pace contracts with each of these providers as a processor under RCW 19.373.060 — meaning the provider may process consumer health data only as Pace instructs and only for the purposes described above. For their commercial API offerings, Anthropic, xAI, and OpenAI publicly state that they do not use customer API content to train their models by default or without explicit permission. Some providers retain request and response data for limited periods for abuse prevention, security, or legal compliance reasons under their applicable terms. Where settings are available to minimize or eliminate such retention, Pace configures them. We will continue to verify these configurations as provider terms evolve.

### 4.1.1 HealthKit-derived context transmitted to Anthropic

When you authorize Pace to read HealthKit data through iOS and you interact with the Pace coach, Pace transmits to Anthropic, PBC processed contextual summaries derived from your HealthKit data — for example, recent sleep summaries (typical hours and stage breakdown for the past several days), recent activity summaries (steps and active calories trends), recent recovery markers (resting heart rate range, HRV range), and similar context relevant to the question you have asked the coach. **We do not transmit raw, full-history HealthKit exports.** Transmission occurs in response to your active interaction with the coach; Pace does not transmit HealthKit-derived context to Anthropic passively or in the background.

**What we never do with HealthKit data.** We never use HealthKit data — including any HealthKit-derived context transmitted to Anthropic — for: advertising, marketing, profiling for any purpose unrelated to providing the Services to you, training AI models (ours or third parties'), sale, sharing for cross-context behavioral advertising, or any purpose other than the AI processing described in this Section 4.1. We do not transmit HealthKit data to any third party other than the AI processors and infrastructure providers identified in Sections 4.1 and 4.2.

**Compliance with Apple's HealthKit terms.** Apple's App Review Guideline 5.1.3 permits the use of HealthKit data to "[improve] health, medical, and fitness management." Pace's transmission of HealthKit-derived context to Anthropic is for exactly that purpose: enabling the Pace coach to provide you with personalized, informed coaching responses about your training, recovery, and nutrition. Anthropic operates as Pace's processor under a written agreement under RCW 19.373.060. Anthropic's commercial API terms state that customer API content is not used to train Anthropic's models by default; Pace does not opt in to model training.

**Affirmative consent.** Your acceptance of Pace's consent screen during onboarding — including the AI-sharing acknowledgment — is your affirmative consent under RCW 19.373.030 to Pace's transmission of HealthKit-derived context to the AI providers identified in this Section. You may revoke specific HealthKit permissions at any time in iOS Settings → Privacy & Security → Health, and you may withdraw your consent at any time as described in Section 5.3.

### 4.2 Infrastructure providers (processors)

| Third party | What is shared | Purpose |
|---|---|---|
| **Supabase, Inc.** (supabase.com) | All persistent consumer health data: user profiles, food logs, exercise logs, coaching messages, embeddings, HealthKit snapshots, consent records | Database hosting on US-located PostgreSQL, authentication, file storage, with Postgres row-level security limiting data access to you and authorized Pace systems |
| **Render Services, Inc.** (render.com) | Consumer health data may transit through Pace's backend during request processing; Render does not store consumer health data persistently | Backend application hosting |
| **Apple, Inc.** | Sign in with Apple authentication tokens, HealthKit permission scopes, App Store in-app purchase transaction identifiers (no consumer health data is shared with Apple beyond the HealthKit permission boundary, which Apple controls on-device) | Authentication, on-device HealthKit access, subscription billing |

### 4.3 Specific affiliates

Pace is operated by Born in Tokyo Digital LLC. Born in Tokyo Digital LLC has no parent company, no subsidiary, and no other corporate affiliate. We share no consumer health data with affiliates because we have none.

### 4.4 Other recipients

- **With your specific consent** (separate from the consent obtained at sign-up), we may share consumer health data with another service you affirmatively authorize.
- **Legal compliance:** to regulators or law enforcement in response to a lawful request, or as necessary to defend our legal rights.
- **Business transactions:** to an acquiring party in a sale of Pace or a merger involving Born in Tokyo Digital LLC, in which case the recipient must continue to honor this policy or obtain new consent.

We do not share consumer health data with any party for any other purpose without your specific consent.

---

## 5. Your Washington consumer health data rights

Under RCW 19.373.040, Washington State residents and consumers whose consumer health data is collected in Washington have the rights described below.

### 5.1 Right to confirm and access

You have the right to confirm whether Pace is collecting, sharing, or selling your consumer health data, and to access that data. Upon a verified request, Pace will also provide, as required by RCW 19.373.040(1)(a), a list of all third parties and affiliates with whom Pace has shared or sold your consumer health data, and an active email address or other online mechanism that you may use to contact those recipients.

### 5.2 Right to deletion

You have the right to request deletion of your consumer health data. When you exercise this right, under RCW 19.373.040(1)(c), Pace will:

- Delete your consumer health data from our active records and systems.
- Notify all affiliates, processors, contractors, and other third parties with whom Pace has shared your consumer health data of your deletion request and direct them to delete the data they received from us.
- Delete or overwrite archived and backup copies in the ordinary backup cycle, in any case not exceeding the period permitted by RCW 19.373.040 (which permits archive and backup deletion to be completed within a reasonable time).

You may delete your account at any time through Pace's in-app Settings, which initiates the deletion process described above. You may also request deletion by emailing legal@usepace.fit.

We may decline a deletion request only where RCW 19.373.040(2) permits — for example, where retention is required to comply with another legal obligation. If we decline, we will explain why and inform you of your right to appeal under Section 5.5.

### 5.3 Right to withdraw consent

Under RCW 19.373.040(1)(b), you have the right to withdraw your consent for Pace's collection and sharing of your consumer health data at any time. Withdrawing consent will limit your use of the Services because Pace requires consumer health data to provide its core features.

You can withdraw consent by:

- Revoking specific HealthKit permissions in iOS Settings → Privacy & Security → Health
- Adjusting consent toggles in Pace's in-app Settings
- Deleting your account
- Emailing legal@usepace.fit

Withdrawal stops Pace's future collection and sharing for the consent withdrawn. It does not by itself delete the data we already hold — for that, exercise the deletion right under Section 5.2.

### 5.4 How to exercise your rights

To exercise any of the rights above, you may:

- Submit the request through the in-app Settings if that option is available to you, or
- Email **legal@usepace.fit** with a description of your request.

We will not require you to create a new account to exercise these rights. We may require you to authenticate through your existing Pace account where reasonable to verify the request comes from you.

We will:

- Acknowledge receipt of your request within 5 business days
- Respond substantively within 45 days of receipt of the request, or notify you of an extension of up to an additional 45 days for complex requests, as permitted by RCW 19.373.040(1)(d)
- Respond at no charge to you and without discriminating against you for exercising your rights

If we cannot verify your identity from the information you provide, we will tell you what additional information is needed to authenticate the request.

### 5.5 Right to appeal a denied request

Under RCW 19.373.040(1)(h), if we deny your request, you have the right to appeal. To submit an appeal:

- Email **legal@usepace.fit** with the subject line "Appeal"
- Include a copy of or reference to our original decision
- Explain why you believe the decision should be reconsidered

Within 45 days of receipt of an appeal, we will inform you in writing of the action taken or not taken in response to the appeal, including a written explanation of the reasons for our decision. If we deny your appeal, we will provide you with an online mechanism (or, if no online mechanism is available, another method) through which you may contact the Washington Attorney General to submit a complaint. The Washington Attorney General's Office accepts complaints at **www.atg.wa.gov/file-complaint**.

---

## 6. Security of consumer health data

Under RCW 19.373.050, we maintain administrative, technical, and physical data security practices that are appropriate to the volume and nature of the consumer health data we process. These practices currently include:

- TLS encryption for all data in transit between the Pace app, the Pace backend, and our processors
- Encryption at rest in our Supabase database
- PostgreSQL row-level security policies that limit consumer health data access to your account and authorized Pace systems
- Sign in with Apple as the authentication mechanism — Pace never sees or stores your Apple ID password
- Processor contracts with each third party named in Section 4 that bind them to appropriate confidentiality and use limitations under RCW 19.373.060
- No advertising trackers in the iOS app

We are a small company. We do not currently hold SOC 2, ISO 27001, or HIPAA certifications, and we do not claim to. We will improve our security posture over time and update this policy as those practices evolve.

**FTC Health Breach Notification Rule (16 CFR Part 318).** In addition to the security measures above, we are subject to the Federal Trade Commission's Health Breach Notification Rule (16 CFR Part 318) and will notify affected individuals, the FTC, and (where required) the media of any qualifying breach of PHR identifiable health information within the timelines the Rule requires, as further described in our general Privacy Policy at <https://usepace.fit/privacy>.

---

## 7. Updates to this policy

We may update this policy. For any material change to how we collect, use, or share consumer health data, we will obtain your affirmative consent before applying the change to data we already hold, as required by RCW 19.373.030(1)(c)–(d). For non-material changes (typo corrections, contact information updates, clarifying language), we will update the "Last updated" date at the top of this policy and the version number.

---

## 8. Contact

For questions about this policy, to exercise your rights, or to file a complaint:

**Email:** legal@usepace.fit

**Mail:**
Born in Tokyo Digital LLC
ATTN: Privacy / Consumer Health Data
6642 Wildflower Way
Minnetrista, MN 55331

To file a complaint with the State of Washington, contact the Washington Attorney General's Office at **www.atg.wa.gov/file-complaint**.

---

*Born in Tokyo Digital LLC, EIN 42-2068679. D-U-N-S 145W007149.*
