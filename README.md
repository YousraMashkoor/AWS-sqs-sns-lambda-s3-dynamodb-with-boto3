### Setup localstack

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

export QUEUE_URL="http://localhost:4566/000000000000/yousra-queue"
export TOPIC_ARN="arn:aws:sns:us-east-1:000000000000:yousra-topic"
```
4. source .env
5. create a queue

```bash
aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name yousra-queue
```


## Commands:

### Secrets Manager Commands

List Secrets:  
 aws --endpoint-url=http://localhost:4566 --profile=localstack secretsmanager list-secrets


Create Secrets:  
aws --endpoint-url=http://localhost:4566 --profile=localstack secretsmanager create-secret --name=postgres --secret-string=[{"username":"postgres","password":"postgres"}]

OR

aws --endpoint-url=http://localhost:4566 --profile=localstack secretsmanager put-secret-value --secret-id=postgres --secret-string file://secrets.json


Put Secrets:  
aws --endpoint-url=http://localhost:4566 --profile=localstack secretsmanager put-secret-value --secret-id=postgres --secret-string=[{"username":"postgres"},{"password":"postgres"}]

Get Secrets:  
aws --endpoint-url=http://localhost:4566 --profile=localstack secretsmanager get-secret-value --secret-id=postgres

--------------------------------------------------------------------------------
