## Overview

This project focused on automating EC2 infrastructure on AWS and validating its operational state. I used Terraform to provision EC2 instances and the required networking components, then wrote Python scripts with boto3 to inspect instance status and health. The goal was to automate both deployment and verification, reducing manual checks and making infrastructure state easy to confirm.

## Stack and Environment

- Terraform was used to define and deploy EC2 resources as code. 
- Python with the boto3 SDK was used to query AWS APIs and inspect instance metadata, state, and health. 
- AWS EC2 served as the compute layer being provisioned and monitored.

## What I Learned

I gained hands-on experience using Terraform to manage AWS infrastructure in a repeatable and structured way. On the automation side, I learned how to use boto3 to retrieve EC2 instance details and interpret state and health information programmatically. This helped bridge infrastructure provisioning with runtime validation.

## Problems I Solved

One challenge was managing dependencies between AWS resources in Terraform, which I addressed through modular design and clear references. Another was aligning deployed infrastructure with real-time operational data, which I solved by combining Terraform workflows with boto3-based status checks.

## Takeaway

This project reinforced how infrastructure automation and monitoring work together in real environments. Automating provisioning is only part of the job—being able to programmatically verify that systems are healthy and running as expected is just as important for reliable cloud operations.