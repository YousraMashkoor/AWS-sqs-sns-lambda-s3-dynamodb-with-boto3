import boto3

sqs = boto3.resource('sqs', aws_access_key_id='yousra', aws_secret_access_key='yousra', endpoint_url='http://localhost:4566')
queue_url='http://localhost:4566/000000000000/yousra-queue'

queue = sqs.get_queue_by_name(QueueName = 'yousra-queue')

for message in queue.receive_messages():
    print(message.body)