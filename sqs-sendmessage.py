import os
import boto3

sqs = boto3.client(
    'sqs', 
    aws_access_key_id=os.environ.get('AWS_ACCESS_ID'), 
    aws_secret_access_key=os.environ.get('AWS_ACCESS_KEY'), 
    endpoint_url=os.environ.get('ENDPOINT_URL')
)


queue_url=os.environ.get('QUEUE_URL')
msg=input("Enter your message: ")
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=(
        msg
    )
)

print(response['MessageId'])