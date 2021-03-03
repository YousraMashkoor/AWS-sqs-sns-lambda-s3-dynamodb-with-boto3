#Code snippet

import json
import boto3
dynamodb =  boto3.resource('dynamodb')
s3_client = boto3.client('s3')

table = dynamodb.Table('customer')

def lambda_handler(event, context):
   # Retrieve File Information
   bucket_name =   event['Records'][0]['s3']['bucket']['name']
   s3_file_name =  event['Records'][0]['s3']['object']['key']

   # Load Data in object
   json_object =   s3_client.get_object(Bucket=bucket_name, Key= s3_file_name)
   jsonFileReader  =   json_object['Body'].read()
   jsonDict    =   json.loads(jsonFileReader)

   # Save date in dynamodb table
   table.put_item( Item=jsonDict)