import json
import boto3
import os

s3 = boto3.client('s3')

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