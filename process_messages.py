import boto3
import json

sqs = boto3.resource('sqs', aws_access_key_id='yousra', aws_secret_access_key='yousra', endpoint_url='http://localhost:4566')
queue_url='http://localhost:4566/000000000000/yousra-queue'

queue = sqs.get_queue_by_name(QueueName = 'yousra-queue')

for message in queue.receive_messages():
    response = json.dumps(message.body)
    # if (response.Type == 'Notification'):
    #     print("notification recieved")
    # else:
    print(message.body)