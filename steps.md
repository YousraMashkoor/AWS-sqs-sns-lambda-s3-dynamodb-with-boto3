## 1. Create an IAM Role
awslocal iam create-role --role-name general --assume-role-policy-document file://trust-policy.json

## 2. Create S3 bucket and Upload document:
awslocal s3 mb s3://transaction
awslocal s3 cp transactions.json s3://transaction

## 3. Create Lambda:
> zip function.zip reads3.py  

> awslocal lambda create-function --function-name my_func --zip-file fileb://function.zip --handler reads3.lambda_handler --runtime python3.6 --role arn:aws:iam::000000000000:general  

> awslocal lambda invoke --function-name my_func out --log-type Tail --query 'LogResult' --output text |  base64 -d  
