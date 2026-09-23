# 🛡️ Cybersecurity Automation Labs

A collection of practical, hands-on security engineering labs built to demonstrate automated threat detection, log parsing workflows, and secure cloud infrastructure auditing. 

---

## 💻 Lab 1: Automated Threat Detection & Log Parser (`soc_detector.py`)

### 📋 Overview
In an enterprise environment, security logs handle millions of authentication requests daily. Manual log inspection is impossible. This project simulates a standard **Security Operations Center (SOC)** workflow by implementing a signature-based threat detection engine to catch **Brute-Force attacks**.

### 🔧 Key Technical Mechanics
* **Memory Optimization:** Ingests raw server data (`security_log.txt`) chronologically using a line-by-line file streaming architecture (`for line in file:`), preventing system memory leaks on large enterprise files.
* **Signature Filtering:** Isolates failed authentication sequences via string-matching flags, dropping benign traffic to preserve computing power.
* **Data Aggregation:** Leverages a Python dictionary to map source IP addresses to real-time failure counts, using the default `.get()` method to handle missing keys dynamically and ensure stable script execution.
* **Incident Alerting:** Evaluates data against an active threshold (`count > 3`) to immediately print high-priority alerts for human triage.

---

## ☁️ Lab 2: Automated Cloud Storage Compliance Auditor (`cloud_audit.py`)

### 📋 Overview
Cloud infrastructure misconfigurations—like leaving storage folders wide open to the open internet—are the leading cause of modern enterprise data breaches. This project acts as an automated compliance auditor for cloud environments hosted on **Amazon Web Services (AWS)**.

### 🔧 Key Technical Mechanics
* **Cloud Infrastructure Architecture:** Implements a locked-down **AWS S3 storage bucket** configured with strict master Public Access Blocks and default Server-Side Encryption (SSE-S3) to secure data at rest.
* **Programmatic Auditing:** Integrates the **Python Boto3 SDK** to communicate directly with the AWS API and verify bucket configuration status.
* **Configuration Drift Alerts:** Queries the bucket's access configurations and returns instant warning flags to cloud administrators if an unauthorized script attempts to expose data parameters.

---

## 🚀 Skills Showcased
* **Languages & Frameworks:** Python, Boto3 SDK, Bash/Shell Scripting
* **Cloud Providers:** Amazon Web Services (AWS S3, IAM Basics)
* **Defensive Engineering:** Log Ingestion, Alert Automation, Rule-Based Threat Filtering, Least-Privilege Architecture Concepts
