
#Talk python to me

import json
import boto3

s3 = boto3.client('s3',
    aws_access_key_id="yousra", 
    aws_secret_access_key="yousra"
    )

def lambda_handler(event, context):
   bucket = 'transaction'
   key = 'transactions.json'

   response = s3.get_object(Bucket=bucket, Key=key)

   content = response['Body']

   jsonObject = json.loads(content.read())

   transactions = jsonObject['transactions']

   for record in transactions:
      print("TransactionType: " + record['transactionType'])
      print("TransactionAmount: " + str(record['amount']))
      print("---")