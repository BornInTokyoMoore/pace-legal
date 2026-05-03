# Pace Privacy Policy

**Effective date:** May 3, 2026
**Last updated:** May 3, 2026
**Version:** 1.0
**Operator:** Born in Tokyo Digital LLC, a Minnesota limited liability company

---

## What this policy is

This Privacy Policy describes how Pace handles personal information. Pace is operated by **Born in Tokyo Digital LLC** (EIN 42-2068679), a Minnesota limited liability company. We refer to ourselves below as "Pace" or "we."

This policy applies to:

- The Pace iOS app
- The Pace backend services that the app communicates with
- The website at usepace.fit
- Any communications you have with us

This policy does **not** replace our **Consumer Health Data Privacy Policy** at <https://usepace.fit/health-privacy>. That separate document describes how we handle consumer health data of Washington State residents and consumers whose consumer health data is collected in Washington, as required by the Washington My Health My Data Act. If you are a Washington consumer, that policy controls your consumer health data; this policy continues to apply to your other personal information.

We are a small startup, not a large company. Several sections of this policy refer to that fact honestly, because the alternative — making promises we can't keep — is worse for you and worse for us.

> **Quick summary of the most important commitments in this policy:**
>
> - **We do not sell your personal information.** Not for money, not for any other valuable consideration.
> - **We do not share your personal information for cross-context behavioral advertising.**
> - **We do not use your personal information for targeted advertising.**
> - **We do not use your personal information to train AI models.**
> - **We do not implement geofencing.**
> - **We are not a HIPAA-covered entity** and do not display HIPAA-related seals or claim HIPAA compliance.
>
> The full policy below explains the details, your rights, and exactly which third parties receive what data and why.

---

## 1. Scope

This policy applies to personal information we collect about you when you use Pace or interact with us. "Personal information" in this policy means any information that is linked or reasonably linkable to you. We use the term broadly — different state laws use slightly different terms ("personal data," "personally identifiable information," "personal information"), but in this policy we treat them all the same.

**Geographic scope.** Pace is operated from the United States. The Pace app is distributed through the Apple App Store and is generally available in App Store regions, but Pace markets and supports the app in US English only. If you access Pace from outside the United States, your information will be processed in the United States, where data protection laws may differ from those in your country. By using Pace, you understand and agree to that processing.

**Relationship to the Consumer Health Data Privacy Policy.** Our Consumer Health Data Privacy Policy at <https://usepace.fit/health-privacy> covers consumer health data of Washington State residents and consumers whose consumer health data is collected in Washington, as required by the Washington My Health My Data Act (RCW 19.373). Where that policy and this one address the same data, the more protective treatment applies; where they address different data, each governs its scope.

---

## 2. Personal information we collect

### 2.1 Information you provide directly to Pace

When you create an account and use Pace, we collect:

- **Profile information you provide at onboarding:** display name (free text), email address (provided through Sign in with Apple, which may be Apple's relay address), age in whole years (we do not collect your date of birth), self-reported weight and height, biological sex, activity level, dietary preferences and restrictions, food allergies, fitness goals, calculated daily macro targets derived from this information, step goal preference, sleep target preference.
- **Food and meal logs:** food entries, food photos you submit, photographs of nutrition labels you submit, scanned barcodes, free-text food searches, saved meals you create.
- **Coaching conversation content:** every message you send to the Pace coach and every coach response.
- **Exercise records:** workout entries you log through the coach (exercise name, sets, reps, weight, weight unit, RPE, duration, distance, notes).
- **Account and feature preferences:** notification preferences, units of measurement, app theme.
- **Consent and acknowledgment records:** the consent state recorded by the consent screen described in our Consumer Health Data Privacy Policy.

### 2.2 Information from your iOS device, with your authorization

Apple HealthKit data flows to Pace only when you grant permission through iOS system controls. The categories that Pace requests are listed in the iOS health permission prompts and described in detail in our Consumer Health Data Privacy Policy. They include: step count, active energy burned, heart rate, heart rate variability, resting heart rate, sleep stages, body weight, workouts (and route GPS only if you separately permit it), VO₂ max, and cardio recovery. You can change or revoke any HealthKit permission at any time in iOS Settings → Privacy & Security → Health.

### 2.3 Information collected automatically

When you use Pace, we and our infrastructure providers automatically receive:

- **Device and request metadata:** device timezone (IANA), UTC offset, app version, iOS version, iOS device model.
- **IP address:** logged by our hosting provider (Render Services, Inc.) for security, abuse-prevention, and debugging. IP addresses rotate with normal log retention.
- **Crash reports:** generated by Sentry when the app crashes, with personally identifying information scrubbed before transmission.
- **Anonymous app-usage events:** generated by PostHog (which feature was opened, which button was pressed). These events do not include health data and do not include your name, email, or other directly identifying information.

### 2.4 Information from Apple's subscription system

When you start a subscription, Apple's in-app purchase system processes the transaction. The Pace app forwards your subscription receipt to RevenueCat, which validates it with Apple and makes your subscription state available to Pace. Through this flow, RevenueCat receives the validated subscription receipt, the Pace internal user ID associated with the purchase, and a record of subscription transactions over time. Pace does not see your Apple ID password, your payment card, or your billing address — Apple processes those directly.

### 2.5 What we do not collect

For clarity, we do **not** collect: precise geolocation outside what HealthKit provides for workouts you've authorized; web browsing history; contacts; calendar entries; microphone recordings; **biometric identifiers used for identification of a specific individual** (such as fingerprints or face scans); genetic data; ad-network tracking identifiers; the iOS Advertising Identifier (IDFA); social-graph data; or any data category not listed in Sections 2.1 through 2.4.

For clarity, certain biometric *measurements* — heart rate, heart rate variability, and similar — are collected from HealthKit when you authorize that flow, as described in Section 2.2 and in detail in our Consumer Health Data Privacy Policy. These are not biometric identifiers in the sense of being used to identify you; you are already authenticated by Sign in with Apple. They are, however, consumer health data subject to the protections described in our Consumer Health Data Privacy Policy.

---

## 3. How we use personal information

We use personal information for these purposes, and no others:

- **To operate the Services.** Display your nutrition, activity, and recovery information; generate coach responses; identify food in photos and on labels; track your progress over time; sync your data across your iOS devices; provide search.
- **To authenticate you and protect your account.** Verify your identity via Sign in with Apple; detect and prevent abuse and fraud.
- **To handle subscriptions and billing.** Manage your trial, paid subscription, and any refunds. Apple processes payments; we receive subscription state from Apple via RevenueCat.
- **To diagnose technical problems.** Analyze crash reports to find and fix bugs.
- **To understand product use at the aggregate level.** Anonymous usage events tell us which features are used and how often. We use this to make decisions about what to build and what to fix. These events do not include health data or directly identifying information.
- **To improve the Services.** Where we use your information to improve Pace beyond bug-fixing — for example, evaluating the quality of food-photo identification — we use de-identified data (within the meaning of California Civil Code § 1798.140(m)) wherever doing so is reasonably possible.
- **To communicate with you about your account.** Respond to your support emails. Send transactional notifications about your account or your data.
- **To comply with law.** Respond to lawful regulatory or law enforcement requests, defend our legal rights, and meet legal obligations.

We do **not**:
- Sell your personal information to anyone.
- Share your personal information for cross-context behavioral advertising.
- Use your personal information for targeted advertising.
- Use your personal information for profiling that produces legal or similarly significant effects (decisions about credit, employment, housing, insurance, education enrollment, healthcare services, or access to essential goods or services).
- Use your personal information to train AI models — we use commercial AI APIs from providers who, under their applicable commercial terms, do not use customer API content to train their models by default.

---

## 4. How we share personal information

We share the minimum information each recipient needs to perform a specific function, and only with the recipients named below.

### 4.1 AI service providers (covered in detail in the Consumer Health Data Privacy Policy)

For consumer health data flows to Anthropic, xAI, OpenRouter, and OpenAI, our Consumer Health Data Privacy Policy at <https://usepace.fit/health-privacy> describes what we send to whom and why. The same flows are governed by this policy where they involve information that is not consumer health data, with the same disclosures and the same processor commitments.

### 4.2 Infrastructure providers

| Provider | What is shared | Purpose |
|---|---|---|
| **Apple, Inc.** | Sign in with Apple identifier; HealthKit permission scopes (data flows on-device through Apple's permission framework); App Store in-app purchase transaction identifiers | Authentication, on-device HealthKit boundary, subscription billing |
| **Supabase, Inc.** | All persistent personal information described in Section 2 | Database hosting on US-located PostgreSQL with row-level security; authentication; file storage |
| **Render Services, Inc.** | Personal information transits through Pace's backend during request processing; persistent storage is not on Render | Backend application hosting |
| **RevenueCat, Inc.** | Validated Apple subscription receipts, Pace internal user ID, subscription transaction history; no health data | Subscription state management |
| **PostHog, Inc.** | Anonymous app-usage events; no health data; no directly identifying information | Product analytics |
| **Functional Software, Inc. (Sentry)** | App crash reports with personally identifying information scrubbed before transmission | Crash diagnostics |

We have written agreements with each of these providers that limit their use of the personal information to the purpose for which we engage them.

### 4.3 HealthKit data flows — disclosure required by Apple

When you authorize Pace to read HealthKit data through iOS, Pace uses that data on-device and on Pace's backend for the purposes described in Section 3.

**What we transmit to Anthropic, PBC.** As part of providing AI-driven coaching responses, Pace transmits to Anthropic processed contextual summaries derived from your HealthKit data — for example, recent sleep summaries (typical hours and stage breakdown for the past several days), recent activity summaries (steps and active calories trends), and recent recovery markers (such as resting heart rate range and HRV range) relevant to the question you have asked the coach. **We do not transmit raw, full-history HealthKit exports.** Transmission occurs in response to your active interaction with the coach, not passively or in the background.

**What we never do with HealthKit data.** We do not use HealthKit data for: advertising, marketing, profiling for any purpose unrelated to providing the Services to you, training AI models (ours or third parties'), sale, sharing for cross-context behavioral advertising, or any purpose other than the AI processing described in this Section. We do not transmit HealthKit data to any third party other than the processors identified in Section 4.1 and our Consumer Health Data Privacy Policy.

**Why this complies with Apple's HealthKit terms.** Apple's App Review Guideline 5.1.3 permits the use of HealthKit data to "[improve] health, medical, and fitness management." Pace's transmission of HealthKit-derived context to Anthropic is for exactly that purpose: enabling the Pace coach to give you personalized, informed coaching responses about your training, recovery, and nutrition. Anthropic operates as Pace's processor under a written agreement; Anthropic's commercial API terms state that customer API content is not used to train Anthropic's models by default, and Pace does not opt in to model training.

**Your affirmative consent.** Your acceptance of Pace's consent screen during onboarding — including the AI-sharing acknowledgment — constitutes your affirmative consent to Pace's sharing of HealthKit-derived context with the AI service providers described in this policy and in our Consumer Health Data Privacy Policy. You may revoke specific HealthKit permissions at any time in iOS Settings → Privacy & Security → Health.

### 4.4 Other recipients

- **With your specific consent**, we may share your personal information with another service you affirmatively authorize.
- **Legal compliance:** to regulators or law enforcement in response to a lawful request, or as necessary to defend our legal rights.
- **Business transactions:** to an acquiring party in a sale of Pace or a merger involving Born in Tokyo Digital LLC, in which case the recipient must continue to honor this policy or obtain new consent.

### 4.5 We do not sell or share your personal information

We do not sell your personal information for monetary or other valuable consideration. We do not share your personal information for cross-context behavioral advertising. The CCPA, the Virginia CDPA, and similar laws use "sell" and "share" in technical ways that include some non-monetary exchanges; we do neither under any of these definitions.

### 4.6 Pace has no affiliates

Born in Tokyo Digital LLC has no parent, no subsidiary, and no other corporate affiliate. We share no personal information with affiliates because we have none.

---

## 5. Cookies, tracking technologies, and analytics

The Pace app is an iOS app, not a website. The app does not use traditional web browser cookies. The app does use software development kits (SDKs) for analytics and crash reporting:

- **PostHog** records anonymous app-usage events (which screens are opened, which buttons are pressed) tied to a randomly generated identifier. We do not associate these events with your name, email, or health data.
- **Sentry** records app crashes with personally identifying information scrubbed before transmission, so we can find and fix bugs.

The Pace app does **not** use:
- The iOS Advertising Identifier (IDFA)
- App Tracking Transparency (ATT) — Pace does not perform cross-app or cross-website tracking
- Tracking pixels of any kind
- Advertising networks
- Marketing attribution SDKs
- Session-recording or behavior-replay tools

If you visit our website at usepace.fit, the website is currently a static informational site and does not set marketing or analytics cookies. If we add web analytics later, we will update this policy.

---

## 6. Data retention

We retain personal information only as long as we need it for the purposes described in this policy, and we apply the following retention criteria:

| Category | Retention |
|---|---|
| Account profile, food logs, exercise logs, coaching messages, HealthKit snapshots, embeddings, saved meals | Until you delete the data through the app or delete your account |
| Consent records (for legal evidence of consent) | Until you delete your account, then for the period required to defend against legal claims; backup deletion within the ordinary backup cycle |
| Subscription records | As required to administer your subscription and meet tax and accounting obligations |
| Crash reports (Sentry) | Per Sentry's standard retention; PII scrubbed before transmission |
| Anonymous usage events (PostHog) | Per PostHog's standard retention; not linked to identifying information |
| Server access logs (Render) | Standard log rotation by Render; not stored persistently by Pace |

When you delete your Pace account, we delete your account, your profile, your food logs, your exercise logs, your coaching messages, your stored embeddings, and your HealthKit snapshots from our active production database systems. We initiate provider deletion requests where the provider's contract supports it. We delete or overwrite archived and backup copies in the ordinary backup cycle, in any case within the period required by applicable state law (for Washington consumer health data, see our Consumer Health Data Privacy Policy).

We may retain a minimal record that an account previously existed (a hashed identifier with no underlying personal information) for fraud prevention.

---

## 7. Security

We use the following security measures:

- TLS encryption for all data in transit between the Pace app, our backend, and our processors
- Encryption at rest in our Supabase database
- PostgreSQL row-level security policies that restrict your data to your account and authorized Pace systems
- Sign in with Apple — Pace never sees or stores your Apple ID password
- Personal information stored in iOS Keychain, not iOS UserDefaults, where Keychain is appropriate
- Written agreements with each processor that bind them to use the information only as we instruct
- No tracking pixels, no advertising SDKs, no cross-context behavioral advertising tooling

We honestly disclose what we are not:

- We are a small startup and do not currently hold SOC 2, ISO 27001, or any other independent security certification, and we do not claim to.
- We are not a HIPAA-covered entity or business associate. We do not display HIPAA-related seals.
- No system is perfectly secure. We commit to improving our security posture over time and to telling you the truth about what we have implemented.

---

## 8. Your universal rights

The rights in this section are available to all Pace users to the extent we can operationally provide them. Section 9 below describes additional rights available under specific state laws.

### 8.1 Right to know what we collect and why

You have the right to know what categories of personal information we have collected, the sources, the purposes, and the categories of recipients. Section 2, Section 3, and Section 4 of this policy answer those questions for all users. If you want a more specific explanation, contact us at legal@usepace.fit.

### 8.2 Right to access

You have the right to obtain a copy of your personal information that we hold. To exercise this right, email legal@usepace.fit. We will provide your data in a portable format within 45 days of receiving a verified request. Where the request is complex, we may extend our response by an additional 45 days, with notice to you.

### 8.3 Right to correct

You can correct most of your personal information directly in the Pace app — your profile, your goals, your logs. For information you cannot edit in-app, email legal@usepace.fit.

### 8.4 Right to delete

You can delete your Pace account at any time through the in-app Settings, which initiates the deletion described in Section 6. You can also request deletion by emailing legal@usepace.fit. Once we receive a verified deletion request, we will complete deletion within 45 days, with the same backup-cycle treatment described in Section 6.

### 8.5 Right to data portability

Where applicable law requires, we will provide your data in a portable, machine-readable format. Email legal@usepace.fit to request portability.

### 8.6 Right to opt out of sale, sharing, targeted advertising, and significant-effect profiling

You have the right under various state privacy laws to opt out of (a) the sale of your personal information, (b) sharing of your personal information for cross-context behavioral advertising, (c) targeted advertising, and (d) profiling that produces legal or similarly significant effects.

Pace does not engage in any of these activities (see Section 4.5 and the use limitations in Section 3). Because Pace does not engage in these activities, there is no opt-out mechanism for you to exercise — these activities do not occur in the first place. If we ever change our practices, we will update this policy, provide a clear opt-out mechanism before the change takes effect, and obtain affirmative consent before the change applies to your existing data.

### 8.7 Right to non-discrimination

We will not deny you services, charge you a different price, or provide you a different level of service for exercising any privacy right.

### 8.8 Right to withdraw consent

For processing based on your consent (including consumer health data — see our Consumer Health Data Privacy Policy), you may withdraw your consent at any time. Withdrawal does not affect the lawfulness of processing before withdrawal, and it may limit your ability to use Pace because some processing is necessary to provide the Services.

### 8.9 Right to appeal

If we deny any of the rights requests above, you have the right to appeal. Email legal@usepace.fit with the subject line "Appeal" and a reference to our original decision. We will respond to your appeal within 45 days of receipt and explain our reasoning. If we deny your appeal, we will tell you how to contact your state Attorney General to file a complaint.

### 8.10 How we verify your identity

To protect against fraudulent rights requests, we may need to verify that the request comes from you or your authorized representative. Where reasonable, verification is by authentication through your existing Pace account. We will not require you to create a new account to exercise your rights, and we will tell you what additional information we need if your request cannot be verified.

### 8.11 No charge

We will not charge you to exercise these rights, except where applicable law permits us to charge for excessive or repetitive requests.

---

## 9. State-specific privacy notices

This section describes additional rights and disclosures for residents of states with comprehensive privacy laws. The state-specific rights below supplement (and do not limit) the universal rights in Section 8.

### 9.1 California

If you are a California resident, the California Consumer Privacy Act, as amended by the California Privacy Rights Act ("CCPA"), gives you the rights below. Currently Pace's processing volume and revenue are below the CCPA's applicability thresholds (Cal. Civ. Code § 1798.140(d)). We honor these rights anyway as a matter of operational policy, and we will be required to honor them once Pace meets the thresholds.

**Categories of personal information collected, sold, and shared.** Sections 2 and 4 of this policy describe the categories collected and the categories of recipients. We do not sell personal information and do not share it for cross-context behavioral advertising.

**Sensitive personal information.** Cal. Civ. Code § 1798.140(ae) defines sensitive personal information to include health information. Pace collects sensitive personal information (specifically, health-related information). We use it only for the purposes described in Section 3 — operating the Services, providing AI coaching, and the other purposes described — and not for any purpose to which California's right to limit use of sensitive personal information would attach.

**California-specific consumer rights.** Right to know, right to delete, right to correct, right to know about sale/sharing (we don't sell or share for behavioral advertising — see Section 4.5), right to opt out of sale/sharing (see Section 8.6), right to limit use of sensitive personal information (not applicable because we do not use sensitive personal information for any purpose beyond providing the Service), right to non-discrimination, right to data portability. To exercise: email legal@usepace.fit.

**Authorized agent.** You may designate an authorized agent to make a request on your behalf. We may require the agent to provide proof of authorization and require you to verify your identity.

**Shine the Light (Cal. Civ. Code § 1798.83).** California residents may request a notice describing categories of personal information shared with third parties for those third parties' direct marketing purposes. Pace does not share personal information with third parties for those parties' direct marketing purposes.

**Automated decision-making (CCPA ADMT regulations effective January 1, 2026).** The CCPA's automated decision-making technology regulations apply to "significant decisions" about consumers — such as the provision or denial of financial services, lending, housing, insurance, education enrollment, employment opportunities, healthcare services, or access to essential goods or services. Pace's AI coach provides general wellness guidance. It does not make significant decisions of any of those types. The Pace coach is not a healthcare provider and does not determine your access to healthcare services. If you have questions about how the coach generates a particular response, email legal@usepace.fit.

### 9.2 Colorado

If you are a Colorado resident, the Colorado Privacy Act gives you rights to access, correct, delete, data portability, opt-out of sale, opt-out of targeted advertising, opt-out of profiling for decisions producing legal or significant effects, and to revoke consent. Colorado requires controllers to honor universal opt-out signals. Pace does not engage in sales, targeted advertising, or significant-effect profiling — see Section 8.6 for the consequence of that fact for your opt-out rights. For other rights, email legal@usepace.fit.

### 9.3 Connecticut

If you are a Connecticut resident, the Connecticut Data Privacy Act, as amended (Conn. Gen. Stat. § 42-526), treats consumer health data as sensitive data requiring opt-in consent. The consent screen described in our Consumer Health Data Privacy Policy obtains that opt-in. Connecticut also gives you rights to access, correct, delete, data portability, and opt-out as described for Colorado above.

**Geofencing.** Conn. Gen. Stat. § 42-526(a)(1)(C) prohibits geofencing within 1,750 feet of any mental health facility or reproductive or sexual health facility. Pace does not implement any geofence and does not use geofencing technology in the app.

### 9.4 Virginia, Utah, Indiana, Iowa, Kentucky, Tennessee, Montana, Delaware, New Hampshire, New Jersey, Oregon, Rhode Island

If you are a resident of any of these states, your state's comprehensive privacy law gives you rights to access, delete, data portability, opt-out of sale, opt-out of targeted advertising, and (in most states) opt-out of profiling for significant-effect decisions, plus a right to appeal denials. Most of these states also give you a right to correct your personal information; Iowa's law currently does not. Pace does not engage in sale, targeted advertising, or significant-effect profiling — see Section 8.6 for the consequence of that fact for your opt-out rights. For other rights, email legal@usepace.fit.

### 9.5 Texas

If you are a Texas resident, the Texas Data Privacy and Security Act (Tex. Bus. & Com. Code Ch. 541) gives you rights to access, correct, delete, data portability, and opt-out of sale, targeted advertising, and profiling. Born in Tokyo Digital LLC currently meets the U.S. Small Business Administration definition of a small business and is therefore exempt from most of the TDPSA's substantive requirements under the small-business exemption that the Texas statute provides. Pace remains prohibited from selling sensitive personal data without consent regardless of that exemption, and Pace does not sell any personal data. We honor the rights above operationally as a matter of policy. To exercise: email legal@usepace.fit.

### 9.6 Maryland

If you are a Maryland resident, the Maryland Online Data Privacy Act (effective October 1, 2025) gives you rights similar to those described above, with stricter limits on the processing of sensitive data and a more demanding data-minimization standard than the Virginia template. Pace's processing limits described in Sections 3 and 4 are designed to satisfy these stricter limits. To exercise rights: email legal@usepace.fit.

### 9.7 Minnesota (Pace's home state)

If you are a Minnesota resident, the Minnesota Consumer Data Privacy Act (Minn. Stat. Ch. 325M) gives you rights to access, correct, delete, data portability, and opt-out of sale, targeted advertising, and profiling. Born in Tokyo Digital LLC currently meets the U.S. Small Business Administration small-business definition and is exempt from most substantive provisions of the MCDPA. Even as an exempt small business, we may not sell sensitive personal data without consent, and we do not sell any personal data.

**Right to question profiling decisions.** Minnesota uniquely gives you the right to question results of profiling that produces legal or similarly significant effects, including the right to be informed of the reason for a particular outcome and to review the data used. Pace's AI coach does not produce decisions with legal or similarly significant effects. If you have questions about how the coach generated a particular response, email legal@usepace.fit and we will explain to the extent we can.

**Contact for Minnesota AG complaints:** Office of the Minnesota Attorney General, 445 Minnesota Street, Suite 600, St. Paul, MN 55101; (651) 296-3353; PrivacyMN.com.

### 9.8 Nebraska

If you are a Nebraska resident, the Nebraska Data Privacy Act provides rights to access, correct, delete, data portability, and opt-out of sale, targeted advertising, and profiling. Pace does not engage in these activities. To exercise other rights, email legal@usepace.fit.

### 9.9 Florida

The Florida Digital Bill of Rights applies primarily to controllers with $1 billion or more in global gross annual revenue. Pace is well below that threshold and is not a covered controller under the FDBR.

### 9.10 Washington — see standalone policy

Consumer health data of Washington residents is governed by our **Consumer Health Data Privacy Policy** at <https://usepace.fit/health-privacy>, which implements the Washington My Health My Data Act. If you are a Washington consumer, that document is the controlling document for your consumer health data.

### 9.11 Nevada

The Nevada Consumer Health Data Privacy Law (Nev. Rev. Stat., as enacted by SB 370) governs consumer health data of Nevada consumers. Pace does not currently maintain a separate Nevada consumer health data privacy policy. For Nevada-specific consumer health data inquiries, including questions about access, deletion, withdrawal of consent, or appeal, email legal@usepace.fit. We will respond consistent with the Nevada law's requirements as we operationally apply them. Nevada consumers also retain the rights described in this Section 9 to the extent operationally applicable.

---

## 10. International users (GDPR / UK GDPR)

Pace markets and supports the app in US English and is operated from the United States. We do not actively offer goods or services to data subjects in the European Economic Area or the United Kingdom. The Pace app is, however, available through the global Apple App Store, and EEA and UK residents may install and use Pace. If you do, the following applies.

**Lawful bases.** Where the EU General Data Protection Regulation or UK General Data Protection Regulation applies, our lawful bases for processing are:

- **Performance of a contract** (Article 6(1)(b)): processing necessary to provide the Pace Services to you.
- **Consent** (Article 6(1)(a) and Article 9(2)(a)): processing of health data and processing for purposes you have consented to through the consent screen described in our Consumer Health Data Privacy Policy.
- **Legal obligation** (Article 6(1)(c)): processing required by applicable law.
- **Legitimate interests** (Article 6(1)(f)): processing necessary for security, fraud prevention, and the operational stability of Pace.

**EU/UK rights.** You have the rights under GDPR / UK GDPR to access, rectification, erasure, restriction of processing, data portability, objection, and not to be subject to solely automated decisions producing legal or similarly significant effects (see Section 14). To exercise: email legal@usepace.fit. You also have the right to lodge a complaint with your national data protection authority.

**International data transfers.** Where EEA or UK personal data is transferred to the United States, transfers are made on the basis of (a) your explicit consent (Article 49(1)(a)) and/or (b) where applicable, the EU-US Data Privacy Framework or UK Extension where the recipient is certified, and/or (c) Standard Contractual Clauses where Pace and a recipient have agreed to them. As Pace scales, we will adopt SCCs across the processor stack.

**EU representative under GDPR Article 27 / UK representative.** Pace does not actively target EEA or UK users. To the extent any EEA or UK user nonetheless uses Pace, we will appoint an Article 27 representative in the EEA, and a UK representative under the UK GDPR, if and when our processing of EEA or UK residents' personal data ceases to be incidental — for example, if we begin marketing to EEA or UK users, or if our EEA or UK user base becomes substantial. We will update this section when that occurs.

---

## 11. Children's privacy

Pace is intended for adults. The Pace consent screen requires you to affirm that you are 18 years of age or older before any data collection begins.

We do not knowingly collect personal information from children under 13. The Children's Online Privacy Protection Act (COPPA) and corresponding rules apply to operators of online services directed to children under 13 or those with actual knowledge of collecting personal information from children under 13. Pace is not directed to children under 13.

If we learn that personal information of a child under 13 has been collected — for example, because a parent or guardian contacts us, because a user later identifies themselves as a child, or because account data otherwise indicates a user is a child — we will delete the personal information and the associated account. Parents or guardians who believe Pace has collected information from their child may email legal@usepace.fit.

---

## 12. Data breach notification

If we experience a security breach affecting your personal information, we will notify you, regulators, and (if required) the media in accordance with applicable law.

**FTC Health Breach Notification Rule (16 CFR Part 318).** Pace handles personal health information in a way that, in our analysis, makes Pace a vendor of personal health records under the FTC's amended Health Breach Notification Rule effective July 29, 2024. We will comply with the Rule's notification requirements for any qualifying breach of PHR identifiable health information, including notification to affected individuals, the FTC, and (for breaches of 500 or more records) the media, within the timelines the Rule requires (in no case later than 60 calendar days after discovery).

**State breach notification laws.** We will also notify you and applicable state regulators in accordance with the breach notification laws of your state of residence. Where state law and the FTC Rule both apply, we will follow the most stringent applicable timeline.

---

## 13. Changes to this policy

We may update this policy. When we do:

- For non-material changes (clarifications, contact information updates, typo corrections), we will update the "Last updated" date and the version number at the top of the policy.
- For material changes (changes to categories of personal information collected, purposes of processing, recipients, retention, or your rights), we will provide notice through the Pace app and through email to your account email at least 30 days before the change takes effect.
- For material changes to our handling of consumer health data, our Consumer Health Data Privacy Policy describes how we will obtain new affirmative consent before applying the change.

---

## 14. Automated decision-making and AI processing

The Pace coach is an AI feature that generates personalized wellness guidance. Pace uses Claude (Anthropic), Grok Vision (xAI), and OpenAI text-embedding-3-small to power Pace features as described in our Consumer Health Data Privacy Policy.

**Pace's AI does not make decisions producing legal or similarly significant effects.** Specifically, Pace's AI coach does not determine, and is not a basis for the determination of, your access to financial services, lending, housing, insurance, education enrollment, employment opportunities, healthcare services, or access to essential goods or services. Pace's coach is informational and offers general wellness guidance, not medical diagnosis, prescription, or treatment.

**Human review.** All AI-generated coaching guidance is informational and is not implemented automatically against your account or your data — you decide what to do with it. Pace's founder reviews user feedback about coaching outputs and uses that review to adjust system behavior.

**Right to know about AI processing.** If you want to know what data was sent to which AI provider in connection with a specific coach response, email legal@usepace.fit and we will provide the information we are able to provide.

**California ADMT regulations.** The CCPA's ADMT regulations effective January 1, 2026 apply to businesses meeting the CCPA's applicability thresholds, and apply ADMT-specific consumer notice, opt-out, and access rights effective January 1, 2027 to ADMT used for "significant decisions." As described above, Pace does not currently meet the CCPA thresholds and Pace's AI coaching is not used for "significant decisions" under that regulation. We will update this section as our position evolves.

**GDPR Article 22.** Article 22 limits decisions based solely on automated processing that produce legal or similarly significant effects. Pace's AI coaching is informational guidance and does not produce such decisions, so Article 22 does not apply to it. If you nonetheless want a human to review any specific Pace AI output, email legal@usepace.fit.

---

## 15. Contact

For privacy questions, to exercise your rights, or to file a complaint:

**Email:** legal@usepace.fit

**Mail:**
Born in Tokyo Digital LLC
ATTN: Privacy
6642 Wildflower Way
Minnetrista, MN 55331

**For Washington consumer health data:** see our Consumer Health Data Privacy Policy at <https://usepace.fit/health-privacy>.

**Regulatory complaints by state:**
- California: California Privacy Protection Agency, www.cppa.ca.gov; California Attorney General, oag.ca.gov
- Minnesota: Office of the Minnesota Attorney General, www.ag.state.mn.us; PrivacyMN.com
- Texas: Office of the Texas Attorney General, www.texasattorneygeneral.gov
- Washington: Office of the Washington Attorney General, www.atg.wa.gov/file-complaint
- Other states: your state Attorney General's office
- EEA / UK: your national data protection authority

To report a privacy concern with Pace specifically, please email us first so we have the opportunity to address it.

---

*Born in Tokyo Digital LLC, EIN 42-2068679. D-U-N-S 145W007149.*
