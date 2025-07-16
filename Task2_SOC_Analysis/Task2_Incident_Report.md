# 🚨 Incident Report: SOC Log Analysis
**Internship Task 2 – SOC Alert Monitoring & Incident Simulation**

**Analyst:** Christian K.  
**Date of Analysis:** July 16, 2025  
**Tools Used:** Elastic Stack (Filebeat, Elasticsearch, Kibana on Ubuntu VM)

---

## 🔍 Overview
As part of a SOC simulation, logs were ingested and analyzed from a provided sample file (`SOC_Task2_Sample_Logs.txt`). The goal was to detect malicious activity, identify and classify notable security events, and propose incident response actions. Data was collected using Filebeat and visualized within Kibana for correlation and pattern recognition.

---

## ⚠️ Identified Security Events

### 1. Ransomware Behavior Detected
- **Timestamp:** 2025-07-03 09:10:14  
- **User:** `bob`  
- **IP Address:** `172.16.0.3`  
- **Action:** `malware detected`  
- **Threat Type:** `Ransomware Behavior`  
- **Severity:** High  
- **Suggested Actions:**
  - Immediately isolate the affected machine.
  - Block all traffic from the source IP to contain the infection.
  - If the ransomware was isolated to Bob’s system, begin eradication by removing the malware and restoring clean backups.
  - Conduct forensic review to confirm no data exfiltration occurred.

---

### 2. Suspicious Reuse of IPs – Possible Unauthorized Access
- **Timestamp:** 2025-07-03 04:53:14  
- **User:** `alice`  
- **IP Address:** `203.0.113.77`  
- **Action:** `file accessed`  
- **Severity:** High  
- **Suggested Actions:**
  - Correlate this IP with other user activities to detect reuse or lateral movement.
  - Block the IP immediately if it appears repeatedly across accounts.
  - Enforce stronger login authentication mechanisms (e.g., MFA).
  - Investigate account access to determine if credential compromise occurred.

---

### 3. Brute Force or Login Spray Attempt
- **Timestamp:** 2025-07-03 07:22:14  
- **User:** `charlie`  
- **IP Address:** `192.168.1.101`  
- **Action:** `connection attempt`  
- **Severity:** Medium  
- **Suggested Actions:**
  - Implement brute-force protection measures (e.g., rate limiting, CAPTCHA).
  - Set up account lockout thresholds after failed attempts.
  - Log and alert all failed login attempts from internal IP ranges.

---

### 4. Overprivileged User Access
- **Timestamp:** 2025-07-03 06:01:14  
- **User:** `bob`  
- **IP Address:** `172.16.0.3`  
- **Action:** `file accessed`  
- **Severity:** Medium  
- **Suggested Actions:**
  - Review access rights associated with Bob’s account.
  - Apply the principle of least privilege across the organization.
  - Limit file upload and access based on user roles.
  - Implement data classification policies and audit file permissions.

---

### 5. Rootkit Signature Detected
- **Timestamp:** 2025-07-03 07:51:14  
- **User:** `eve`  
- **IP Address:** `10.0.0.5`  
- **Action:** `malware detected`  
- **Threat Type:** `Rootkit Signature`  
- **Severity:** High  
- **Suggested Actions:**
  - Immediately isolate the host from the network.
  - Perform a full memory and disk scan using EDR or antivirus tools.
  - Reset all credentials tied to Eve’s account.
  - Monitor for any privilege escalation behavior or persistence mechanisms.

---

## 🛠️ Log Ingestion Setup Summary

```bash
# Modified filebeat.yml input
filebeat.inputs:
  - type: log
    id: soc-task2-input
    enabled: true
    paths:
      - /home/azureuser/SOC_Task2_Sample_Logs.txt

# Reloaded Filebeat and monitored output
sudo systemctl restart filebeat
sudo tail -f /var/log/filebeat/filebeat
```

- Used index pattern: `.ds-filebeat-*`
- Filtered using: `message:"2025-07-03"` and keyword searches like `user`, `malware`, `file accessed`
- Correlated events based on usernames and IP addresses

---

## 🔚 Conclusion

The analysis of ingested log data revealed multiple indicators of compromise within the monitored environment, including evidence of malware deployment (ransomware and rootkit), brute-force connection attempts, and unauthorized file access from external sources. These events suggest an adversary was able to exploit insufficient access controls and weak authentication mechanisms to perform lateral movement and deploy malicious code.

Immediate containment steps should focus on isolating compromised systems, performing root-cause analysis, and validating the integrity of critical data. Long-term, this incident highlights the urgent need to implement **least privilege access**, enhance **authentication protocols** (e.g., MFA, IP filtering), and deploy **advanced endpoint protection** to detect and prevent future threats.

This investigation reinforces the importance of centralized log monitoring and correlation for early threat detection and rapid incident response across the organization.