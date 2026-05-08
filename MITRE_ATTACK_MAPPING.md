# 🗺️ MITRE ATT&CK® Mapping: Canvas/Instructure Incident (2026)
**Case Study:** Data Exfiltration by ShinyHunters  
**Analyst:** Cuong Dang

This document maps the observed and inferred tactics, techniques, and procedures (TTPs) used in the Canvas breach to the globally recognized MITRE ATT&CK framework.

## ⚔️ Observed Tactics & Techniques


| Tactic | ID | Technique | Description/Application |
| :--- | :--- | :--- | :--- |
| **Reconnaissance** | T1589 | Gather Victim Identity Information | Scraped faculty/student emails from public HCC directories. |
| **Initial Access** | T1566.004 | Phishing: Voice (Vishing) | Used AI-generated voice clones to deceive administrative support desks. |
| **Initial Access** | T1078.004 | Valid Accounts: Cloud Accounts | Gained access to legitimate student/faculty Canvas accounts. |
| **Persistence** | T1528 | Steal Application Access Token | Hijacked OAuth tokens to maintain access without needing credentials/MFA. |
| **Defense Evasion** | T1550.004 | Proxy: Adversary-in-the-Middle | Used tools like **Evilginx2** to intercept sessions in real-time. |
| **Exfiltration** | T1048.003 | Exfiltration Over Alternative Protocol | Used **Rclone** to move 3.65 TB of data via cloud-to-cloud transfers. |
| **Impact** | T1491 | Defacement: Internal Defacement | Targeted internal messaging systems to spread extortion threats. |

## 🛡️ AI-Enhanced Defensive Countermeasures

Based on the mapping above, we propose the following AI-driven mitigations:

1.  **Identity Intelligence (T1528 Detection):** 
    *   Implementing **Unsupervised Machine Learning** to establish a baseline of "Normal API Usage." 
    *   *Detection:* Identifying when a token is used to access an unusual volume of private messages in a short timeframe.

2.  **Voice Bio-Forensics (T1566.004 Defense):**
    *   Deploying **AI Audio Analysis** tools at help desks to detect synthetic frequency patterns common in Deepfake voice clones.

3.  **Adaptive Egress Filtering (T1048 Defense):**
    *   Using **Neural Networks** to monitor network egress. If a "Cloud-to-Cloud" transfer exceeds institutional norms, the AI automatically throttles the connection and alerts the SOC.
