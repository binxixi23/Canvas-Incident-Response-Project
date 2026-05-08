# 🕵️ Technical Deep-Dive: The ShinyHunters Canvas Breach (2026)

## 1. Executive Summary
On May 7, 2026, a major security breach affected the Canvas LMS ecosystem. This report outlines the technical nuances of the attack and the proactive steps taken to secure personal and institutional data at Houston City College.

## 2. Methodology of the Attack
The breach leveraged **Modern Identity Extortion** rather than traditional ransomware. 
- **T1528 (Stealing OAuth Access Tokens):** By bypassing MFA through session hijacking, attackers gained persistent access to student records.
- **T1566 (Phishing/Vishing):** Use of AI-generated voice clones to compromise administrative help desks (SaaS Supply Chain vulnerability).

## 3. Proposed AI Mitigation Strategies
To defend against similar "Malware-less" attacks, I propose:
1.  **Sequence-Based Behavior Modeling:** Deploying **LSTM (Long Short-Term Memory)** networks to identify deviations in typical student login/download patterns.
2.  **Contextual Risk Scoring:** Real-time AI analysis of IP reputation, device fingerprints, and API request frequency.

## 4. My Incident Response Actions
Following the breach, I initiated the following protocol:
- **Audit:** Conducted a manual review of Microsoft 365 sign-in logs.
- **Containment:** Revoked all suspicious 3rd-party app permissions.
- **Communication:** Filed a formal technical incident report to HCC IT and faculty.
