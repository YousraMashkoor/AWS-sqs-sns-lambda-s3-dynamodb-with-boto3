import boto3
import json
import os

def main():
    sns = boto3.client(
        'sns', 
        aws_access_key_id=os.environ.get('AWS_ACCESS_ID'), 
        aws_secret_access_key=os.environ.get('AWS_ACCESS_KEY'), 
        endpoint_url=os.environ.get('ENDPOINT_URL')
    )

    publishObject =input("Publish your message: ")

    response = sns.publish(TopicArn=os.environ.get('TOPIC_ARN'),
                            Message=json.dumps(publishObject),
                            Subject="PURCHASE",
                            #MessageAttribute={"TransactionType":{"DataType":"String", "StringValue":"PURCHASE"}}
                            )
    print(response['ResponseMetadata']['HTTPStatusCode'])


main()