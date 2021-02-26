import boto3

sqs = boto3.client('sqs', aws_access_key_id='yousra', aws_secret_access_key='yousra', endpoint_url='http://localhost:4566')
queue_url='http://localhost:4566/000000000000/yousra-queue'
msg=input("Enter your message: ")
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=(
        msg
    )
)

print(response['MessageId'])