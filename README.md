# data-engineering

## Pre- requisites
- Python3 & Pip is installed
- Venv is created

## Solution to Question on User Interaction CSV

### Python Command to run program
``` bash
source .venv/bin/activate
python3 -m pip install wheel
python3 -m pip install pandas
python process_csv_user_interaction.py  user_visited.csv output.csv
```

### Explanation
- process_csv_user_interaction.py is the program that takes inputs csv and output csv file
- It generates the result as below
- - Total Interactions
- - Total Unique Users
- - Most Visited URL
- - Average Time Spent on Each URL

## Solution to Question on Online Purchases Interaction CSV

### Python Command to run program
``` bash
source .venv/bin/activate
python3 -m pip install wheel
python3 -m pip install pandas
python process_csv_online_purchases.py customer_input.txt output1.csv 
```

### Explanation
- process_csv_online_purchases.py is the program that takes inputs csv and output csv file
- It generates the result as below
- - date (str): Date of the transaction in the format 'YYYY-MM-DD'.
- - customer_id (int): Unique identifier for each customer.
- - total_spent (float): Total amount spent by the customer on that date.

## Solution to Question on Situation Based

### Explanation
``` bash
I am assuming we are interested in designing Batch Processing Pipeline

Process Involved for designing the pipeline would be as follows:

Extract > Transform > Load

The folloing components (AWS managed Services) might possibly be used:

Kinesis Streaming Agent -> Kinesis Data Firehose ->  Transform Records -> Save Intermediate records in S3 -> AWS Lamdba -> AWS Redshift 
                                        |
                                        |->   AWS Lambda (Save source data in S3)


- Kinesis Streaming Agent/Producer Library on the website pulling data from database & pushing to Kinesis Streams/Data Firehose [Extract]
- Kinesis Data Firehose - [Transform]
    - AWS Lambda (Save source data in S3) 
    - Kinesis Data Firehose - Transform Records  
    - Kinesis Data Firehose - Save Intermediate records in S3 
    - AWS Lambda - Load Transformed Records in AWS Redshift 
- Data base/ Blob Storage - AWS Redshift - [Load]]
- Analytic Tools - to provide an interface/ option to generate reports by providing queries to view analytics data and derive insights

```

