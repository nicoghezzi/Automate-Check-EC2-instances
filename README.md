# 🚀 Infras Automation & Validation: Terraform + EC2 + Python

![Infrastructure: Terraform](https://img.shields.io/badge/Infrastructure-Terraform-%235835CC?style=for-the-badge&logo=terraform&logoColor=white)
![Cloud: AWS](https://img.shields.io/badge/Cloud-AWS-%23FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Compute: EC2](https://img.shields.io/badge/Compute-EC2-%23FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Automation: Python](https://img.shields.io/badge/Automation-Python-%233776AB?style=for-the-badge&logo=python&logoColor=white)
![SDK: boto3](https://img.shields.io/badge/SDK-boto3-green?style=for-the-badge&logo=amazon-aws&logoColor=white)

A hands-on project that automates AWS EC2 infrastructure provisioning with Terraform and validates runtime state using Python and boto3.

---

## 📌 Overview

This project demonstrates an end-to-end workflow combining infrastructure deployment and validation:

- Provisioned EC2 instances and networking using Terraform  
- Automated infrastructure checks using Python (boto3)  
- Retrieved instance state, metadata, and health programmatically  
- Reduced reliance on manual verification of cloud resources  

---

## ⚙️ Workflow

### 1. Infrastructure Provisioning
- Defined EC2 instances and networking in Terraform  
- Applied infrastructure using repeatable IaC workflows  

### 2. AWS Integration
- Connected to AWS services using boto3 SDK  
- Queried EC2 APIs for instance data  

### 3. Validation & Inspection
- Retrieved instance state (running, stopped, etc.)  
- Checked health and status programmatically  
- Validated deployed infrastructure in real time  

---

## 🧰 Tech Stack

- Terraform (Infrastructure as Code)  
- AWS EC2 (Compute)  
- Python (Automation)  
- boto3 (AWS SDK)  

---

## ⚠️ Challenges & Fixes

- **Terraform resource dependencies** → Structured modules and explicit references  
- **Mismatch between deployed vs actual state** → Introduced boto3 validation layer  
- **Manual verification overhead** → Automated health and status checks  

---

## 💡 Key Learnings

- Infrastructure provisioning must be paired with validation  
- Terraform enables repeatable, structured infrastructure deployment  
- boto3 allows deep visibility into AWS resource state  
- Automation reduces operational risk and manual effort  

---

## ✅ Outcome

- ✔ EC2 infrastructure provisioned via Terraform  
- ✔ Automated validation of instance state and health  
- ✔ Programmatic inspection of AWS resources  
- ✔ Reduced need for manual infrastructure checks  

---

## 🧪 Takeaway

This project highlights the importance of combining infrastructure automation with runtime validation. Provisioning resources is only part of the process—ensuring they are healthy and operating as expected is critical for reliable cloud systems.
