### Setup localstack

### Install AWS CLI
(CLI https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html)

>curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
>unzip awscliv2.zip
>sudo ./aws/install

>aws configure



### SQS Commands

aws --endpoint-url=http://localhost:4566 sns create-topic --name customqueue-topic

aws --endpoint-url=http://localhost:4566 sns subscribe --topic-arn arn:aws:sns:us-east-1:000000000000:customqueue-topic --protocol email --notification-endpoint abc@def.com


aws --endpoint-url=http://localhost:4566 sns publish  --topic-arn arn:aws:sns:us-east-1:000000000000:customqueue-topic --message 'Hello from my app'

--------------------------------------------------------------------------------
Create a Queue:
aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name customqueue-queue

Send Message to the Queue:
aws --endpoint-url=http://localhost:4566 sqs send-message --queue-url http://localhost:4566/000000000000/customqueue-queue --message-body 'Test Message for my Queue!'

Receive message from the QUeue:
aws --endpoint-url=http://localhost:4566 sqs receive-message --queue-url http://localhost:4566/000000000000/customqueue-queue

Recieve 10 messages from Queue:
aws --endpoint-url=http://localhost:4566 sqs receive-message --queue-url http://localhost:4566/000000000000/customqueue-queue --attribute-names All --message-attribute-names All --max-number-of-messages 10

