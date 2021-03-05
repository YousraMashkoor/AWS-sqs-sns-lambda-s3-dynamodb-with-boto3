##Create data.json

# UPLOAD TO S3 BUCKET

## Create S3 bucket:
awslocal s3 mb s3://boto3customer

## Create Dynamodb:
awslocal dynamodb create-table --table-name customer  --attribute-definitions AttributeName=customerId,AttributeType=S --key-schema AttributeName=customerId,KeyType=HASH --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5

## Create an IAM Role
awslocal iam create-role --role-name lambda-ex --assume-role-policy-document file://trust-policy.json

awslocal iam list-roles

## Logs and Cloudwatch
awslocal logs describe-log-groups
awslocal cloudwatch list-metrics


# READ FROM S3 BUCKET

## Create S3 bucket:
awslocal s3 mb s3://boto3customer

aws --endpoint-url=http://localhost:4566 s3 cp transaction.json s3://transaction

# Create a lambda function

zip function.zip index.py

awslocal lambda create-function --function-name read-bucket --zip-file fileb://function.zip --handler index.handler --runtime python3.6 --role arn:aws:iam::000000000000:role/s3ReadWrite

awslocal lambda invoke --function-name read-bucket out --log-type Tail --query 'LogResult' --output text |  base64 -d
