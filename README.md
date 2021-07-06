### Setup localstack
http://localhost:4566/health

### Install AWS CLI
(CLI https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html)

>curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"  
>unzip awscliv2.zip  
>sudo ./aws/install  

>aws configure

### Getting started
 
 1. create a venv
 2. pip install -r requirements.txt
 3. add .env with following credentials/n

```bash
export AWS_ACCESS_ID="aws access id"
export AWS_ACCESS_KEY="aws secret access key"
export ENDPOINT_URL="http://localhost:4566" 
```
4. source .env
5. create a queue

```bash
aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name yousra-queue
```
#### Follow steps.md to run the function

## Commands:

### Dynamodb

Create DB:  
aws --endpoint-url=http://localhost:4566 dynamodb create-table --table-name test_table  --attribute-definitions AttributeName=first,AttributeType=S AttributeName=second,AttributeType=N --key-schema AttributeName=first,KeyType=HASH AttributeName=second,KeyType=RANGE --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5

List DB:  
aws --endpoint-url=http://localhost:4566 dynamodb list-tables

Describe DB:  
aws --endpoint-url=http://localhost:4566 dynamodb describe-table --table-name test_table

Put Item:  
aws --endpoint-url=http://localhost:4566 dynamodb put-item --table-name test_table  --item '{"first":{"S":"Jack"},"second":{"N":"42"}}'

Get Item:  
aws --endpoint-url=http://localhost:4566 dynamodb put-item --table-name test_table  --item '{"first":{"S":"Jack"},"second":{"N":"42"}}'

Scan/ Display content:  
aws --endpoint-url=http://localhost:4566 dynamodb scan --table-name test_table

Query DB:  
aws --endpoint-url=http://localhost:4566 dynamodb query --table-name test_table --projection-expression "#first, #second" --key-condition-expression "#first = :value" --expression-attribute-values '{":value" : {"S":"Jack"}}' --expression-attribute-names '{"#first":"first", "#second":"second"}'


### S3 Commands
Create Bucket:  
aws --endpoint-url=http://localhost:4566 s3 mb s3://yousrabucket

Upload Document:  
aws --endpoint-url=http://localhost:4566 s3 cp data.json s3://yousrabucket

List Contents:  
aws --endpoint-url=http://localhost:4566 s3 ls s3://yousrabucket

Delete File:  
aws --endpoint-url=http://localhost:4566 s3 rm s3://yousrabucket/data.json

List Buckets:  
aws --endpoint-url=http://localhost:4566 s3api list-buckets

Get Presigned URL:  
aws --endpoint-url=http://localhost:4566 s3 presign s3://yousrabucket/data.json




### SNS Commands

Create Topic:  
aws --endpoint-url=http://localhost:4566 sns create-topic --name customqueue-topic

List Topics:  
aws --endpoint-url=http://localhost:4566 sns list-topics

Subscribe to Topic:  
aws --endpoint-url=http://localhost:4566 sns subscribe --topic-arn arn:aws:sns:us-east-1:000000000000:yousra-topic --protocol sqs --notification-endpoint arn:aws:sns:us-east-1:000000000000:my_queue  

Publish a message:  
aws --endpoint-url=http://localhost:4566 sns publish  --topic-arn arn:aws:sns:us-east-1:000000000000:yousra-topic --message 'Hello from my app'

--------------------------------------------------------------------------------

### SQS Commands

Create a Queue:   
aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name yousra-queue

Send Message to the Queue:  
aws --endpoint-url=http://localhost:4566 sqs send-message --queue-url http://localhost:4566/000000000000/yousra-queue --message-body 'Test Message for my Queue!'

Receive message from the QUeue:  
aws --endpoint-url=http://localhost:4566 sqs receive-message --queue-url http://localhost:4566/000000000000/yousra-queue

Recieve 10 messages from Queue:  
aws --endpoint-url=http://localhost:4566 sqs receive-message --queue-url http://localhost:4566/000000000000/yousra-queue --attribute-names All --message-attribute-names All --max-number-of-messages 10

List Queues:  
aws --endpoint-url=http://localhost:4566 sqs list-queues 

List Subscriptions:  
aws --endpoint-url=http://localhost:4575 sns list-subscriptions

### Lambda

Create Function:  
awslocal --endpoint-url=http://localhost:4566 create-function --function-name my-function --zip-file fileb://function.zip --handler index.handler --runtime nodejs12.x --role arn:aws:iam::000000000000:role/lambda-ex

List Functions:  
awslocal lambda list-functions --max-items 10

Get Function:
awslocal lambda get-function --function-name my-function

Delete Function:
awslocal lambda delete-function --function-name my-function

## Cloudwatch and logs

