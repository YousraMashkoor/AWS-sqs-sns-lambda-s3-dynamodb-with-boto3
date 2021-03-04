import json
import boto3
import os

s3 = boto3.client(
      's3',
      aws_access_key_id=os.environ.get('AWS_ACCESS_ID'), 
      aws_secret_access_key=os.environ.get('AWS_ACCESS_KEY'), 
      endpoint_url=os.environ.get('ENDPOINT_URL')
   )

def lambda_handler(event, context):
   bucket = 'transaction'
   key = 'transactions.json'

   response = s3.get_object(Bucket=bucket, Key=key)

   content = response['Body']

   jsonObject = json.loads(content.read())

   transactions = jsonObject['transaction']

   for record in transactions:
      print("TransactionType: " + record['transactionType'])
      print("TransactionAmount: " + str(record['amount']))
      print("---")