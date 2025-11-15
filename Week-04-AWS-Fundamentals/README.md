# Week 4: AWS Fundamentals for Data Engineering

## Overview
Master the core AWS services essential for data engineering: S3, RDS, Lambda, and IAM.

## Learning Objectives
By end of Week 4, you will:
- ✅ Set up AWS account with security best practices
- ✅ Work with S3 for data storage
- ✅ Create and manage RDS databases
- ✅ Build Lambda functions for data processing
- ✅ Understand IAM for access control

## Daily Schedule

### Day 1-2: AWS Account & S3
**Topics:**
- AWS account setup
- IAM users, roles, and policies
- S3 buckets, objects, and operations
- S3 storage classes
- Versioning and lifecycle policies

**Hands-on:**
- Create AWS account
- Set up MFA
- Create IAM user
- Create S3 bucket
- Upload/download files using Console, CLI, and Boto3

### Day 3-4: Amazon RDS
**Topics:**
- Relational Database Service overview
- Create MySQL/PostgreSQL database
- Security groups and access control
- Backup and restore
- Connect from Python

**Hands-on:**
- Launch RDS instance (db.t3.micro)
- Connect using MySQL Workbench/pgAdmin
- Create tables and insert data
- Connect from Python using pymysql/psycopg2
- Query database from Lambda

### Day 5: AWS Lambda
**Topics:**
- Serverless computing concepts
- Lambda function basics
- Triggers (S3, EventBridge, API Gateway)
- Environment variables
- IAM roles for Lambda

**Hands-on:**
- Create "Hello World" Lambda
- S3 trigger Lambda (file upload)
- Process CSV file with Lambda
- Write results back to S3

### Day 6-7: Integration Project
**Project:** Build a Simple ETL Pipeline
```
S3 (raw data) → Lambda (transform) → S3 (processed data)
```

**Steps:**
1. Upload CSV to S3 bucket
2. Lambda triggered on upload
3. Read CSV, transform data
4. Write JSON to another S3 bucket
5. Log results to CloudWatch

## AWS Services Deep Dive

### 1. Amazon S3 (Simple Storage Service)

#### What is S3?
- Object storage service
- Store and retrieve any amount of data
- 99.999999999% (11 9's) durability
- Pay only for what you use

#### Key Concepts
```
Bucket → Container for objects
Object → File + metadata (up to 5 TB)
Key → Unique identifier (filename)
Region → Geographic location
```

#### S3 Storage Classes
```
Standard → Frequent access
Intelligent-Tiering → Automatic cost optimization
Standard-IA → Infrequent access
Glacier → Archive (retrieval time: minutes-hours)
Glacier Deep Archive → Long-term archive (12 hours)
```

#### Common Operations
```python
import boto3

s3 = boto3.client('s3')

# Create bucket
s3.create_bucket(Bucket='my-data-bucket')

# Upload file
s3.upload_file('data.csv', 'my-data-bucket', 'data.csv')

# Download file
s3.download_file('my-data-bucket', 'data.csv', 'local_data.csv')

# List objects
response = s3.list_objects_v2(Bucket='my-data-bucket')

# Delete object
s3.delete_object(Bucket='my-data-bucket', Key='data.csv')
```

#### Use Cases for Data Engineering
- Data lake storage
- ETL source and destination
- Log file storage
- Backup and archive
- Data sharing between services

### 2. Amazon RDS (Relational Database Service)

#### What is RDS?
- Managed relational database
- Supports MySQL, PostgreSQL, Oracle, SQL Server
- Automated backups, patching, scaling
- Multi-AZ for high availability

#### Instance Types
```
db.t3.micro → Free tier (1 vCPU, 1 GB RAM)
db.t3.small → 2 GB RAM
db.t3.medium → 4 GB RAM
db.r5.large → Memory-optimized
```

#### Create RDS Instance
```bash
# Using AWS CLI
aws rds create-db-instance \
    --db-instance-identifier my-database \
    --db-instance-class db.t3.micro \
    --engine mysql \
    --master-username admin \
    --master-user-password MyPassword123 \
    --allocated-storage 20 \
    --publicly-accessible
```

#### Connect from Python
```python
import pymysql

connection = pymysql.connect(
    host='your-rds-endpoint.amazonaws.com',
    user='admin',
    password='MyPassword123',
    database='mydb',
    cursorclass=pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM customers")
    results = cursor.fetchall()
    print(results)
```

#### Use Cases for Data Engineering
- Transactional data storage
- ETL source database
- Metadata storage
- Application database
- Data validation and quality checks

### 3. AWS Lambda

#### What is Lambda?
- Serverless compute service
- Run code without managing servers
- Pay only for compute time
- Automatic scaling

#### Lambda Pricing (Free Tier)
```
Requests: 1 Million/month free
Compute: 400,000 GB-seconds free
Duration: Up to 15 minutes per invocation
Memory: 128 MB to 10 GB
```

#### Create Lambda Function
```python
import json
import boto3
import pandas as pd
from io import StringIO

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """
    Triggered when CSV uploaded to S3
    Transform data and save as JSON
    """
    # Get bucket and file from event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Read CSV from S3
    obj = s3.get_object(Bucket=bucket, Key=key)
    df = pd.read_csv(obj['Body'])

    # Transform data
    df['total'] = df['quantity'] * df['price']
    df['processed_date'] = pd.Timestamp.now()

    # Write JSON to S3
    output_key = key.replace('.csv', '.json')
    output_bucket = 'processed-data-bucket'

    s3.put_object(
        Bucket=output_bucket,
        Key=output_key,
        Body=df.to_json(orient='records')
    )

    return {
        'statusCode': 200,
        'body': json.dumps(f'Processed {len(df)} records')
    }
```

#### Lambda Triggers
```
S3 → File upload
EventBridge → Schedule (cron)
API Gateway → HTTP request
DynamoDB → Stream changes
SQS → Queue messages
Kinesis → Stream data
```

#### Use Cases for Data Engineering
- ETL transformations
- Data validation
- File format conversion
- Trigger data pipelines
- Real-time processing
- Scheduled jobs

### 4. IAM (Identity and Access Management)

#### Key Concepts
```
User → Individual identity
Group → Collection of users
Role → Temporary credentials for services
Policy → Permissions document (JSON)
```

#### IAM Policy Example
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::my-data-bucket/*"
    }
  ]
}
```

#### Best Practices
- ✅ Use IAM users, not root account
- ✅ Enable MFA
- ✅ Use roles for services
- ✅ Principle of least privilege
- ✅ Rotate credentials regularly
- ✅ Use groups for permissions

## Hands-On Labs

### Lab 1: S3 Data Lake Setup
```
1. Create S3 bucket: data-lake-raw-[your-name]
2. Create folders: /landing, /processed, /archive
3. Upload sample CSV file
4. Set lifecycle policy: Move to Glacier after 90 days
5. Enable versioning
6. Create bucket policy for public read (optional)
```

### Lab 2: RDS Database Setup
```
1. Launch RDS MySQL instance (db.t3.micro)
2. Configure security group (allow port 3306)
3. Connect using MySQL Workbench
4. Create database 'sales_db'
5. Create tables (customers, orders, products)
6. Insert sample data
7. Query from Python
```

### Lab 3: Lambda CSV Processor
```
1. Create Lambda function (Python 3.11)
2. Add S3 trigger for CSV uploads
3. Code: Read CSV, calculate totals, write JSON
4. Set up IAM role with S3 permissions
5. Test with sample CSV
6. View results in CloudWatch Logs
```

### Lab 4: End-to-End Pipeline
```
1. Upload CSV to S3 bucket
2. Lambda triggered automatically
3. Transform data (add calculated columns)
4. Write results to RDS database
5. Query database to verify
6. Export results back to S3 as JSON
```

## AWS CLI Reference

### S3 Commands
```bash
# Create bucket
aws s3 mb s3://my-bucket-name

# Upload file
aws s3 cp data.csv s3://my-bucket-name/

# Download file
aws s3 cp s3://my-bucket-name/data.csv ./

# List objects
aws s3 ls s3://my-bucket-name/

# Sync folder
aws s3 sync ./local-folder s3://my-bucket-name/folder/

# Delete object
aws s3 rm s3://my-bucket-name/data.csv

# Delete bucket
aws s3 rb s3://my-bucket-name --force
```

### RDS Commands
```bash
# List DB instances
aws rds describe-db-instances

# Create DB instance
aws rds create-db-instance \
    --db-instance-identifier mydb \
    --db-instance-class db.t3.micro \
    --engine mysql \
    --master-username admin \
    --master-user-password MyPassword123 \
    --allocated-storage 20

# Delete DB instance
aws rds delete-db-instance \
    --db-instance-identifier mydb \
    --skip-final-snapshot
```

### Lambda Commands
```bash
# List functions
aws lambda list-functions

# Invoke function
aws lambda invoke \
    --function-name my-function \
    --payload '{"key":"value"}' \
    response.json

# Update function code
aws lambda update-function-code \
    --function-name my-function \
    --zip-file fileb://function.zip
```

## Common Errors & Solutions

### S3 Errors
```
AccessDenied → Check IAM policy and bucket policy
NoSuchBucket → Verify bucket name and region
404 Not Found → Check object key (filename)
```

### RDS Errors
```
Connection timeout → Check security group, allow port 3306
Access denied → Verify username/password
Endpoint not found → Wait for instance to be available
```

### Lambda Errors
```
Permission denied → Check IAM role
Timeout → Increase timeout or optimize code
Out of memory → Increase memory allocation
Module not found → Include dependencies in deployment package
```

## Week 4 Project: Simple ETL Pipeline

### Project Description
Build an automated data processing pipeline:
1. Upload sales CSV to S3
2. Lambda processes and validates data
3. Insert into RDS database
4. Export summary to S3 as JSON

### Architecture
```
[S3 Raw Data] → [Lambda Function] → [RDS Database]
                       ↓
                [S3 Processed Data]
```

### Implementation Steps
See: `06-Hands-On-Labs/week4_project.md`

## Resources

### Documentation
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/)
- [AWS RDS Documentation](https://docs.aws.amazon.com/rds/)
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [AWS IAM Documentation](https://docs.aws.amazon.com/iam/)

### Tutorials
- [AWS Hands-on Tutorials](https://aws.amazon.com/getting-started/hands-on/)
- [S3 Getting Started](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html)
- [Lambda Getting Started](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)

### Practice
- [AWS Workshops](https://workshops.aws/)
- [Qwiklabs](https://www.qwiklabs.com/catalog?keywords=aws)

## Success Checklist

By end of Week 4:
- [ ] AWS account created and secured
- [ ] MFA enabled
- [ ] IAM user created
- [ ] AWS CLI configured
- [ ] Created and managed S3 buckets
- [ ] Uploaded/downloaded files via CLI and Boto3
- [ ] Launched RDS database
- [ ] Connected to RDS from Python
- [ ] Created Lambda functions
- [ ] Built S3 → Lambda → S3 pipeline
- [ ] Completed Week 4 project
- [ ] Understand billing and Free Tier limits

## Interview Questions

### S3
1. What is S3 and what are its use cases?
2. Explain S3 storage classes
3. What is S3 versioning and lifecycle policies?
4. How do you secure S3 buckets?

### RDS
1. What is RDS and when would you use it?
2. Difference between RDS and EC2 with database?
3. How does RDS backup work?
4. What is Multi-AZ deployment?

### Lambda
1. What is serverless computing?
2. When would you use Lambda vs EC2?
3. What are Lambda triggers?
4. How do you handle dependencies in Lambda?

## Next Steps
- Move to [Week 5: AWS Data Services](../Week-05-AWS-Data-Services/README.md)
- Continue practicing S3 and Lambda
- Explore AWS Glue and Athena
