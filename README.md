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

### SNS Commands

aws --endpoint-url=http://localhost:4566 sns create-topic --name customqueue-topic

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
