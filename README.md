Cloud Automation using Python (Boto3)
====================================

This repository contains example scripts to automate common AWS cloud tasks using Python and boto3:
 - Create an S3 bucket
 - Provision an EC2 instance (simple example)
 - Monitor EC2 (describe instances + CloudWatch CPU metric sample)

IMPORTANT
- These are example scripts intended for learning and automation prototypes.
- Do NOT commit real credentials. Use IAM roles, AWS CLI config, or environment variables.
- The EC2 provisioning script is minimal; review and adapt for production use (VPC/Subnet/KeyPair/SecurityGroup).

Files
-----
- provision_s3.py     : Create an S3 bucket and list buckets
- provision_ec2.py    : Launch a simple EC2 instance (uses AMI id placeholder)
- monitor_ec2.py      : Describe EC2 instances and fetch CloudWatch CPU utilization sample
- requirements.txt    : Python dependencies
- env.example.txt     : Example environment variables (AWS credentials - don't commit real values)
- load_env.sh         : Helper to load env vars from .env (for local testing)

Quick start (local)
-------------------
1) Create a virtualenv and install deps:
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

2) Provide credentials (recommended: use AWS CLI & IAM roles). For local testing you can create .env file:
   cp env.example.txt .env

   Note: edit .env with your AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY / AWS_REGION (or rely on AWS CLI profile)

3) Load env vars (optional):
   source load_env.sh

4) Run examples:
   python3 provision_s3.py my-unique-bucket-name-12345
   python3 provision_ec2.py
   python3 monitor_ec2.py

Notes on safety
---------------
- The EC2 script launches resources that may incur charges. Terminate instances you don't need.
- Prefer IAM roles for EC2 or AWS CLI profiles rather than embedding long-lived keys.
- Review AWS limits and region-specific AMI IDs before launching instances.
# Cloud_automation_python
