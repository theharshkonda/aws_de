# AWS Free Tier Guide for Data Engineering

## Overview
AWS Free Tier allows you to practice and build data engineering projects without spending money. This guide covers everything you need to know.

## What is AWS Free Tier?

AWS offers three types of free tier:
1. **12 Months Free** - From signup date
2. **Always Free** - Never expires
3. **Trials** - Short-term free trials

## Free Tier Services for Data Engineering

### Storage Services

#### Amazon S3 (Always Free)
- **Capacity**: 5 GB standard storage
- **Requests**: 20,000 GET, 2,000 PUT
- **Data Transfer**: 100 GB/month out
- **Use for**: Data lakes, raw data storage, transformed data

#### Amazon RDS (12 Months Free)
- **Database**: 750 hours/month
- **Instance**: db.t2.micro or db.t3.micro
- **Storage**: 20 GB SSD
- **Backup**: 20 GB
- **Use for**: Relational databases (MySQL, PostgreSQL)

### Compute Services

#### AWS Lambda (Always Free)
- **Requests**: 1 Million/month
- **Compute**: 400,000 GB-seconds/month
- **Use for**: ETL transformations, data processing, automation

#### Amazon EC2 (12 Months Free)
- **Hours**: 750 hours/month
- **Instance**: t2.micro or t3.micro
- **Use for**: Running scripts, Airflow, custom applications

### Data Analytics Services

#### AWS Glue (Trial)
- **Crawler**: 1 Million objects discovered
- **ETL**: 1 Million requests/month (first month only)
- **Use for**: ETL pipelines, data cataloging

#### Amazon Athena (Always Free)
- **Queries**: 5 GB scanned data/month
- **Use for**: Query S3 data with SQL

#### Amazon Kinesis (12 Months Free)
- **Shard Hours**: 750 hours/month (Kinesis Data Streams)
- **Data**: 500 KB/second PUT
- **Use for**: Real-time streaming data

#### Amazon Redshift (Trial)
- **Trial**: 2 months free (750 hours)
- **Instance**: dc2.large
- **Use for**: Data warehouse

#### AWS Step Functions (Always Free)
- **Transitions**: 4,000 state transitions/month
- **Use for**: Workflow orchestration

#### Amazon QuickSight (Trial)
- **Trial**: 30 days free
- **Authors**: 1 user
- **Use for**: BI dashboards

### Developer Tools

#### AWS CloudFormation (Always Free)
- No additional charge
- **Use for**: Infrastructure as Code

#### AWS CloudWatch (Always Free)
- **Metrics**: 10 custom metrics
- **Logs**: 5 GB ingestion, 5 GB storage
- **Dashboard**: 3 dashboards
- **Use for**: Monitoring and logging

## Account Setup Guide

### Step 1: Create AWS Account
```
1. Go to https://aws.amazon.com
2. Click "Create an AWS Account"
3. Enter email address and account name
4. Choose "Personal" account type
5. Enter payment information (required, but won't be charged if you stay within Free Tier)
6. Verify phone number
7. Select "Basic Support" plan (free)
```

### Step 2: Secure Your Account
```
1. Enable MFA (Multi-Factor Authentication)
   - Go to IAM Console
   - Click on your username
   - Security credentials → Assign MFA device
   - Use Google Authenticator or Authy

2. Create IAM User (Don't use root account)
   - Go to IAM Console
   - Create new user
   - Attach policies: AdministratorAccess (for learning)
   - Enable console access
   - Save credentials securely

3. Set up Billing Alerts
   - CloudWatch → Billing
   - Create alarm for $5, $10, $20
```

### Step 3: Install AWS CLI
```bash
# Windows
# Download from: https://aws.amazon.com/cli/
# Run installer

# Mac
brew install awscli

# Linux
pip install awscli

# Verify installation
aws --version

# Configure AWS CLI
aws configure
# Enter:
# - AWS Access Key ID
# - AWS Secret Access Key
# - Default region: us-east-1
# - Default output: json
```

### Step 4: Install AWS SDKs

#### Boto3 (Python SDK)
```bash
pip install boto3
```

#### Test Connection
```python
import boto3

# Create S3 client
s3 = boto3.client('s3')

# List buckets
response = s3.list_buckets()
print("Buckets:", response['Buckets'])
```

## Cost Monitoring & Alerts

### Set Up Billing Dashboard
```
1. Go to AWS Billing Console
2. Enable "Receive Free Tier Usage Alerts"
3. Enter email address
4. Monitor daily
```

### Create Budget
```
1. AWS Budgets → Create budget
2. Select "Cost budget"
3. Set amount: $10/month
4. Alert threshold: 80%, 100%
5. Enter email for notifications
```

### Monitor Free Tier Usage
```
1. Billing Console → Free Tier
2. Check usage regularly
3. Track services approaching limits
```

## Cost Optimization Tips

### 1. Always Stop Resources When Not in Use
```
✅ DO:
- Stop EC2 instances when not coding
- Delete old S3 data
- Remove unused RDS databases

❌ DON'T:
- Leave EC2 running 24/7
- Keep large files in S3 indefinitely
- Forget about resources
```

### 2. Use Tags for Resource Management
```
Tag all resources:
- Project: DataEngineering
- Environment: Learning
- Owner: YourName
```

### 3. Set Up Auto-Shutdown
```python
# Lambda function to stop EC2 at 11 PM
import boto3
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instances = ['i-1234567890abcdef0']
    ec2.stop_instances(InstanceIds=instances)
    return "Stopped instances"
```

### 4. Monitor with CloudWatch
```
Create alarms for:
- EC2 instance running > 20 hours
- S3 storage > 4 GB
- Lambda invocations > 900K
```

## Data Engineering Free Tier Projects

### Project 1: Simple ETL Pipeline
**Cost**: $0 (within Free Tier)
```
Services Used:
- S3: Store raw and processed data
- Lambda: Transform data
- Glue: Catalog data
- Athena: Query data
```

### Project 2: Real-time Data Pipeline
**Cost**: $0 (within Free Tier)
```
Services Used:
- Kinesis: Stream data
- Lambda: Process stream
- S3: Store results
- CloudWatch: Monitor
```

### Project 3: Data Warehouse
**Cost**: ~$0-5 (Redshift trial)
```
Services Used:
- RDS: Source database
- Glue: ETL
- Redshift: Data warehouse
- QuickSight: Visualization
```

## Free Tier Limits by Service

### Detailed Limits

```
S3:
├── Storage: 5 GB
├── PUT Requests: 2,000
├── GET Requests: 20,000
└── Data Transfer Out: 100 GB

Lambda:
├── Requests: 1,000,000/month
├── Compute: 400,000 GB-seconds
└── Duration: 3.2M seconds of compute time

EC2:
├── Hours: 750/month (t2.micro)
├── Storage: 30 GB EBS
└── Data Transfer: 100 GB out

RDS:
├── Hours: 750/month (db.t2.micro)
├── Storage: 20 GB
├── Backup: 20 GB
└── Data Transfer: 100 GB out

Glue:
├── ETL: 1M requests (first month)
└── Catalog: 1M objects

Athena:
└── Queries: 5 GB scanned data

Kinesis:
├── Shard Hours: 750/month
├── PUT Payload: 500 KB/second
└── Records: 1,000,000 PUT/month

Redshift:
├── Trial: 750 hours (2 months)
└── Instance: dc2.large

Step Functions:
└── State Transitions: 4,000/month

CloudWatch:
├── Metrics: 10 custom
├── Alarms: 10
├── Logs: 5 GB
└── Dashboards: 3
```

## What Happens When You Exceed Free Tier?

### You'll be charged standard rates:
```
Example Costs (if you exceed):
- S3: $0.023/GB/month
- Lambda: $0.20 per 1M requests
- EC2 t2.micro: $0.0116/hour
- RDS db.t2.micro: $0.017/hour
- Athena: $5 per TB scanned
```

### How to Avoid Charges:
1. Monitor Free Tier usage daily
2. Set up billing alerts
3. Delete resources after practice
4. Use CloudWatch alarms
5. Review billing dashboard weekly

## Cleanup Checklist

After completing each project:
```
[ ] Delete S3 buckets (or empty them)
[ ] Terminate EC2 instances
[ ] Delete RDS databases
[ ] Delete Glue crawlers and jobs
[ ] Delete Lambda functions (optional)
[ ] Delete CloudWatch log groups
[ ] Delete Redshift clusters
[ ] Remove IAM roles (if created)
[ ] Check Billing Dashboard
```

## Common Mistakes to Avoid

### 1. Leaving EC2 Running
```
❌ Mistake: Forgetting to stop EC2 after practice
💰 Cost: $8.35/month (over 750 hours)
✅ Solution: Stop instance when done, set auto-shutdown
```

### 2. Large S3 Storage
```
❌ Mistake: Uploading 100 GB to S3
💰 Cost: $2.18/month (95 GB over limit)
✅ Solution: Use sample datasets, delete after practice
```

### 3. Redshift Running 24/7
```
❌ Mistake: Leaving Redshift cluster running after trial
💰 Cost: $180/month
✅ Solution: Pause or delete when not using
```

### 4. High Athena Scans
```
❌ Mistake: Scanning 100 GB data repeatedly
💰 Cost: $5.00 for 100 GB
✅ Solution: Partition data, use WHERE clauses
```

## Resources

### Official Documentation
- [AWS Free Tier](https://aws.amazon.com/free)
- [Free Tier FAQs](https://aws.amazon.com/free/free-tier-faqs/)
- [Pricing Calculator](https://calculator.aws)

### Monitoring Tools
- [AWS Billing Dashboard](https://console.aws.amazon.com/billing/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [Free Tier Usage](https://console.aws.amazon.com/billing/home?#/freetier)

### Learning Resources
- [AWS Training](https://www.aws.training/)
- [AWS Workshops](https://workshops.aws/)
- [Hands-on Tutorials](https://aws.amazon.com/getting-started/hands-on/)

## Support

If you're charged unexpectedly:
1. Check Billing Dashboard
2. Review AWS Cost Explorer
3. Contact AWS Support (may refund first-time mistakes)
4. Close account if needed (within 30 days for full refund)

---

## Quick Start Checklist

```
[ ] Create AWS account
[ ] Enable MFA
[ ] Create IAM user
[ ] Set up billing alerts
[ ] Install AWS CLI
[ ] Configure AWS CLI
[ ] Install Boto3
[ ] Test connection
[ ] Bookmark Billing Dashboard
[ ] Start with S3 + Lambda project
```

**Remember**: Monitor your usage daily for the first month to understand patterns!

---

**Next Steps**:
1. Complete account setup
2. Start with [Week 4: AWS Fundamentals](../../Week-04-AWS-Fundamentals/README.md)
3. Build your first S3 + Lambda project
