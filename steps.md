##Create data.json


## Create S3 bucket:
aswlocal s3 mb s3://boto3customer

## Create Dynamodb:
awslocal dynamodb create-table --table-name customer  --attribute-definitions AttributeName=customerId,AttributeType=S --key-schema AttributeName=customerId,KeyType=HASH --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5

## Create an IAM Role
awslocal iam create-role --role-name lambda-ex --assume-role-policy-document file://trust-policy.json

## Logs and Cloudwatch
awslocal logs describe-log-groups
awslocal cloudwatch list-metrics