# Week 8: Capstone Project - End-to-End Data Pipeline

## Project Overview

Build a complete, production-ready data engineering pipeline that demonstrates all skills learned in this bootcamp.

## Project Title
**E-Commerce Analytics Data Platform**

## Problem Statement

An e-commerce company needs a data platform to:
1. Ingest daily sales data from multiple sources
2. Transform and validate data
3. Store in data warehouse for analytics
4. Generate daily business reports
5. Create interactive dashboards
6. Monitor pipeline health

## Architecture

```
Data Sources → Ingestion → Transformation → Storage → Analytics → Visualization
     ↓             ↓            ↓             ↓          ↓           ↓
  CSV/JSON       S3/         Glue/         Redshift/  Athena/    QuickSight/
   Files      Kinesis       Lambda         S3        Queries     PowerBI
```

### Detailed Architecture
```
┌─────────────────┐
│  Data Sources   │
│  - Sales CSV    │
│  - Orders JSON  │
│  - User API     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   S3 Landing    │ (Raw data)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Lambda/Glue    │ (ETL)
│  - Validate     │
│  - Transform    │
│  - Enrich       │
└────────┬────────┘
         │
         ├──────► RDS (Metadata)
         │
         ▼
┌─────────────────┐
│ S3 Processed    │ (Cleaned data)
└────────┬────────┘
         │
         ├──────► Athena (Ad-hoc queries)
         │
         ▼
┌─────────────────┐
│    Redshift     │ (Data Warehouse)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Visualization  │
│  - QuickSight   │
│  - PowerBI      │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  CloudWatch     │ (Monitoring)
└─────────────────┘
```

## Data Sources

### 1. Sales Transactions (CSV)
```csv
transaction_id,customer_id,product_id,quantity,amount,transaction_date
T001,C123,P456,2,199.98,2024-03-15 10:30:00
T002,C124,P457,1,99.99,2024-03-15 11:45:00
```

### 2. Product Catalog (JSON)
```json
{
  "product_id": "P456",
  "name": "Wireless Mouse",
  "category": "Electronics",
  "price": 99.99,
  "stock": 150
}
```

### 3. Customer Data (API)
```json
{
  "customer_id": "C123",
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "city": "Seattle",
  "signup_date": "2024-01-15"
}
```

## Project Requirements

### Functional Requirements
1. ✅ Ingest data from multiple sources (CSV, JSON, API)
2. ✅ Validate data quality (nulls, duplicates, formats)
3. ✅ Transform data (clean, standardize, enrich)
4. ✅ Load data into data warehouse
5. ✅ Schedule daily automated runs
6. ✅ Generate business reports
7. ✅ Create interactive dashboards
8. ✅ Monitor pipeline health
9. ✅ Handle errors and retries
10. ✅ Log all operations

### Non-Functional Requirements
1. ✅ Scalable architecture
2. ✅ Cost-effective (Free Tier)
3. ✅ Automated (minimal manual intervention)
4. ✅ Documented (README, comments)
5. ✅ Version controlled (Git)
6. ✅ Testable
7. ✅ Secure (IAM policies)

## Implementation Plan

### Day 1: Planning & Setup
**Tasks:**
- [ ] Design architecture diagram
- [ ] Set up GitHub repository
- [ ] Create AWS resources (S3 buckets, IAM roles)
- [ ] Prepare sample datasets
- [ ] Document setup steps

**Deliverables:**
- Architecture diagram
- GitHub repo with README
- Sample data files

### Day 2: Data Ingestion
**Tasks:**
- [ ] Create S3 bucket structure (landing/processed/archive)
- [ ] Upload sample CSV files
- [ ] Create Lambda to fetch data from API
- [ ] Set up S3 event notifications
- [ ] Test data ingestion

**Deliverables:**
- S3 buckets configured
- Lambda function for API ingestion
- Test data uploaded

### Day 3: Data Transformation
**Tasks:**
- [ ] Create Glue crawler for data catalog
- [ ] Write Glue ETL job or Lambda for transformation
- [ ] Implement data validation logic
- [ ] Handle nulls, duplicates, data types
- [ ] Add data quality checks
- [ ] Test transformations

**Deliverables:**
- Glue job or Lambda transformer
- Validation logic
- Transformed data in S3

### Day 4: Data Warehouse & Storage
**Tasks:**
- [ ] Create Redshift cluster (or use Athena)
- [ ] Define table schemas
- [ ] Load data into Redshift
- [ ] Create views for common queries
- [ ] Optimize with distribution/sort keys
- [ ] Test queries

**Deliverables:**
- Redshift cluster (optional)
- Tables created
- Data loaded
- Sample queries

### Day 5: Analytics & Querying
**Tasks:**
- [ ] Set up Athena for S3 data
- [ ] Create partitioned tables
- [ ] Write analytical queries
- [ ] Generate daily summary reports
- [ ] Export reports to S3
- [ ] Test query performance

**Deliverables:**
- Athena tables
- SQL queries
- Daily summary reports

### Day 6: Visualization & Dashboards
**Tasks:**
- [ ] Connect PowerBI/QuickSight to Redshift/Athena
- [ ] Create visualizations (charts, tables)
- [ ] Build interactive dashboards
- [ ] Set up filters and drill-downs
- [ ] Share dashboard
- [ ] Test interactivity

**Deliverables:**
- Interactive dashboard
- Screenshots for documentation

### Day 7: Orchestration & Monitoring
**Tasks:**
- [ ] Create Step Functions workflow
- [ ] Set up EventBridge schedule (daily)
- [ ] Configure CloudWatch alarms
- [ ] Set up SNS notifications
- [ ] Implement error handling
- [ ] Test end-to-end pipeline

**Deliverables:**
- Step Functions workflow
- CloudWatch dashboards
- Automated daily run

### Day 8: Documentation & Presentation
**Tasks:**
- [ ] Update GitHub README
- [ ] Document architecture
- [ ] Add code comments
- [ ] Create user guide
- [ ] Record demo video
- [ ] Prepare presentation
- [ ] Clean up resources (if needed)

**Deliverables:**
- Complete documentation
- Demo video
- Presentation slides

## Technical Implementation

### 1. S3 Bucket Structure
```
my-ecommerce-data-pipeline/
├── landing/
│   ├── sales/
│   ├── products/
│   └── customers/
├── processed/
│   ├── sales/
│   ├── products/
│   └── customers/
├── archive/
└── reports/
    └── daily/
```

### 2. Lambda Function - Data Transformer
```python
import json
import boto3
import pandas as pd
from datetime import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """
    Transform sales data from landing to processed
    """
    # Get file details from S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print(f"Processing {key} from {bucket}")

    try:
        # Read CSV from S3
        obj = s3.get_object(Bucket=bucket, Key=key)
        df = pd.read_csv(obj['Body'])

        # Data Quality Checks
        print(f"Original records: {len(df)}")

        # Remove duplicates
        df = df.drop_duplicates()

        # Handle missing values
        df = df.dropna(subset=['transaction_id', 'customer_id'])

        # Data type conversions
        df['transaction_date'] = pd.to_datetime(df['transaction_date'])
        df['amount'] = df['amount'].astype(float)

        # Add derived columns
        df['year'] = df['transaction_date'].dt.year
        df['month'] = df['transaction_date'].dt.month
        df['day'] = df['transaction_date'].dt.day

        # Validation
        assert df['amount'].min() >= 0, "Negative amounts found"
        assert df['quantity'].min() > 0, "Invalid quantities"

        print(f"Cleaned records: {len(df)}")

        # Write to processed bucket
        output_key = key.replace('landing', 'processed')
        output_bucket = 'my-ecommerce-data-pipeline'

        csv_buffer = df.to_csv(index=False)
        s3.put_object(
            Bucket=output_bucket,
            Key=output_key,
            Body=csv_buffer
        )

        # Write metadata
        metadata = {
            'source_file': key,
            'processed_date': datetime.now().isoformat(),
            'records_processed': len(df),
            'validation_passed': True
        }

        s3.put_object(
            Bucket=output_bucket,
            Key=output_key.replace('.csv', '_metadata.json'),
            Body=json.dumps(metadata)
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Success',
                'records_processed': len(df)
            })
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        # Send SNS notification on failure
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
```

### 3. Glue ETL Job (Alternative to Lambda)
```python
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read from S3
datasource = glueContext.create_dynamic_frame.from_catalog(
    database = "ecommerce_db",
    table_name = "sales_raw"
)

# Transform
transformed = datasource.filter(lambda x: x["amount"] > 0)

# Write to S3
glueContext.write_dynamic_frame.from_options(
    frame = transformed,
    connection_type = "s3",
    connection_options = {"path": "s3://processed-data/sales/"},
    format = "parquet"
)

job.commit()
```

### 4. Redshift Table Schema
```sql
CREATE SCHEMA ecommerce;

CREATE TABLE ecommerce.sales (
    transaction_id VARCHAR(50) PRIMARY KEY,
    customer_id VARCHAR(50) NOT NULL,
    product_id VARCHAR(50) NOT NULL,
    quantity INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    transaction_date TIMESTAMP NOT NULL,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    processed_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
DISTSTYLE KEY
DISTKEY (customer_id)
SORTKEY (transaction_date);

CREATE TABLE ecommerce.customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50),
    signup_date DATE
);

CREATE TABLE ecommerce.products (
    product_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10, 2),
    stock INTEGER
);

-- Aggregate table for faster queries
CREATE TABLE ecommerce.daily_sales_summary AS
SELECT
    transaction_date::DATE AS date,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_revenue,
    AVG(amount) AS avg_order_value,
    COUNT(DISTINCT customer_id) AS unique_customers
FROM ecommerce.sales
GROUP BY transaction_date::DATE;
```

### 5. Step Functions Workflow
```json
{
  "Comment": "E-commerce Data Pipeline",
  "StartAt": "IngestData",
  "States": {
    "IngestData": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789:function:DataIngestion",
      "Next": "TransformData",
      "Catch": [{
        "ErrorEquals": ["States.ALL"],
        "Next": "NotifyFailure"
      }]
    },
    "TransformData": {
      "Type": "Task",
      "Resource": "arn:aws:states:::glue:startJobRun.sync",
      "Parameters": {
        "JobName": "TransformSalesData"
      },
      "Next": "LoadToRedshift",
      "Catch": [{
        "ErrorEquals": ["States.ALL"],
        "Next": "NotifyFailure"
      }]
    },
    "LoadToRedshift": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789:function:LoadRedshift",
      "Next": "GenerateReports"
    },
    "GenerateReports": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789:function:GenerateReports",
      "Next": "NotifySuccess"
    },
    "NotifySuccess": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sns:publish",
      "Parameters": {
        "TopicArn": "arn:aws:sns:us-east-1:123456789:pipeline-notifications",
        "Message": "Pipeline completed successfully"
      },
      "End": true
    },
    "NotifyFailure": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sns:publish",
      "Parameters": {
        "TopicArn": "arn:aws:sns:us-east-1:123456789:pipeline-notifications",
        "Message": "Pipeline failed"
      },
      "End": true
    }
  }
}
```

### 6. Analytical Queries
```sql
-- Daily Sales Report
SELECT
    transaction_date::DATE AS date,
    COUNT(*) AS transactions,
    SUM(amount) AS revenue,
    AVG(amount) AS avg_order_value
FROM ecommerce.sales
WHERE transaction_date >= CURRENT_DATE - 30
GROUP BY transaction_date::DATE
ORDER BY date DESC;

-- Top 10 Products
SELECT
    p.name,
    COUNT(s.transaction_id) AS order_count,
    SUM(s.amount) AS revenue
FROM ecommerce.sales s
JOIN ecommerce.products p ON s.product_id = p.product_id
GROUP BY p.product_id, p.name
ORDER BY revenue DESC
LIMIT 10;

-- Customer Lifetime Value
SELECT
    c.customer_id,
    c.name,
    COUNT(s.transaction_id) AS total_orders,
    SUM(s.amount) AS lifetime_value,
    MIN(s.transaction_date) AS first_order,
    MAX(s.transaction_date) AS last_order
FROM ecommerce.customers c
JOIN ecommerce.sales s ON c.customer_id = s.customer_id
GROUP BY c.customer_id, c.name
ORDER BY lifetime_value DESC;
```

## Dashboard Requirements

### Key Metrics
1. Total Revenue (today, week, month)
2. Number of Transactions
3. Average Order Value
4. Unique Customers
5. Top Products
6. Sales by Category
7. Revenue Trend (last 30 days)
8. Customer Segmentation

### Visualizations
1. **Line Chart**: Revenue over time
2. **Bar Chart**: Top 10 products
3. **Pie Chart**: Sales by category
4. **KPI Cards**: Total revenue, transactions, customers
5. **Table**: Recent transactions
6. **Heatmap**: Sales by day/hour

## Testing Plan

### Unit Tests
- [ ] Lambda function logic
- [ ] Data transformation functions
- [ ] Validation rules

### Integration Tests
- [ ] S3 to Lambda trigger
- [ ] Lambda to Redshift load
- [ ] End-to-end pipeline

### Data Quality Tests
- [ ] No duplicates
- [ ] No nulls in required fields
- [ ] Data types correct
- [ ] Date ranges valid

## Monitoring & Alerts

### CloudWatch Metrics
- Lambda execution duration
- Glue job status
- S3 bucket size
- Redshift query performance

### Alarms
- Pipeline failure
- High error rate
- Slow query performance
- Cost threshold exceeded

## Cost Estimation (Free Tier)

```
Service          Free Tier           Expected Usage    Cost
-----------------------------------------------------------
S3               5 GB                2 GB              $0
Lambda           1M requests         10K requests      $0
Glue             1M requests         5K requests       $0
Athena           5 GB scanned        3 GB              $0
Redshift         750 hours (trial)   Daily (2 hrs)     $0
CloudWatch       10 metrics          5 metrics         $0
-----------------------------------------------------------
Total Monthly Cost: $0 (within Free Tier)
```

## Deliverables

### Code Repository
- [ ] Python scripts
- [ ] SQL queries
- [ ] CloudFormation/Terraform (optional)
- [ ] README with setup instructions
- [ ] requirements.txt

### Documentation
- [ ] Architecture diagram
- [ ] Data flow diagram
- [ ] Setup guide
- [ ] User guide
- [ ] Troubleshooting guide

### Presentation
- [ ] Problem statement
- [ ] Solution architecture
- [ ] Demo (live or video)
- [ ] Challenges faced
- [ ] Future improvements

## Success Criteria

✅ Pipeline runs end-to-end automatically
✅ Data quality checks pass
✅ Dashboard shows real-time metrics
✅ Error handling works
✅ Monitoring alerts function
✅ Code is well-documented
✅ Demo presentation ready

## Bonus Features (Optional)

- [ ] Data lineage tracking
- [ ] Incremental loads (only new data)
- [ ] Machine learning predictions
- [ ] Real-time streaming (Kinesis)
- [ ] Multi-region setup
- [ ] CI/CD pipeline
- [ ] Docker containers
- [ ] dbt for transformations

## Resources

### Sample Datasets
- Kaggle e-commerce datasets
- Generate fake data with Faker library
- AWS sample datasets

### Tools
- VS Code
- Git/GitHub
- AWS Console
- PowerBI Desktop
- Draw.io (diagrams)

## Next Steps After Completion

1. Add project to resume
2. Create LinkedIn post with demo
3. Write blog post about learnings
4. Upload to GitHub portfolio
5. Use in job interviews

---

**This is your showcase project. Make it impressive!** 🚀

Start Date: __________
Target Completion: __________
