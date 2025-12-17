# AWS Big Data Churn Analytics Pipeline

## Overview
This project implements an end-to-end big data pipeline for customer churn analysis using AWS services and PySpark. The pipeline ingests raw data, performs distributed processing, trains a machine learning model, and visualizes insights through dashboards.



## Dataset
- **Type:** Customer Churn Dataset
- **Source:** Public customer behavior dataset
- **Description:** Includes customer demographics, service subscriptions, tenure, billing information, and churn indicators.
- **Purpose:** Analyze churn patterns and build predictive insights.



## Architecture
The pipeline consists of the following components:
1. **Amazon S3** – Raw and processed data storage
2. **Amazon EC2** – PySpark and SQL processing environment
3. **Apache Spark** – Distributed data transformation
4. **Amazon SageMaker Autopilot** – Automated model training
5. **Power BI** – Data visualization
6. **Cron Jobs** – Pipeline automation
7. **Amazon SNS** – Monitoring and notifications



## Data Pipeline Steps

### 1. Data Ingestion
- Raw CSV data uploaded to Amazon S3 (`data/raw/`).

### 2. Data Processing (PySpark)
- Cleaning missing values
- Standardizing column names
- Casting data types
- Feature engineering (tenure groups, charge categories)
- Writing cleaned data to S3 in Parquet format

### 3. Machine Learning
- SageMaker Autopilot used to train churn prediction models
- Automatic model selection and evaluation

### 4. Visualization
- Processed data downloaded from S3
- Power BI used to create churn analysis dashboards
- Note: Power BI Desktop does not support scheduled refresh



## Automation
- A cron job triggers the ETL pipeline automatically
- SNS sends notifications on pipeline success or failure



## Ethical Considerations
- Sensitive personal identifiers were excluded from analysis
- Dataset bias was acknowledged due to demographic imbalance
- Data used strictly for academic purposes



## Folder Structure
- `scripts/` – PySpark ETL and automation scripts
- `sql/` – Analytical SQL queries
- `automation/` – Cron and SNS setup
- `visualization/` – Power BI dashboard
- `architecture/` – System architecture diagram



## How to Run
```bash
bash scripts/run_pipeline.sh
