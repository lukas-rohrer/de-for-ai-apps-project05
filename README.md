# Data Engineer for AI Applications: Project 5 - Data Pipelines with Airflow

A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.

The task is to build an ETL pipeline that is dynamic and built from reusable tasks, can be monitored, and allow easy backfills. The source data resides in S3 and needs to be processed in the data warehouse in Amazon Redshift.

## How to run 

0. Get AWS credentials ready

1. Use *create_tables.sql* to create the neccessary tables

2. Open Airflow and set the credentials

3. Run the *project05_dag* DAG from inside Airflow