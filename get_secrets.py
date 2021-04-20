import boto3
import os
import json
import ast

def get_db_secrets(name):

    session = boto3.session.Session(
        profile_name=os.environ.get('AWS_LOCALSTACK'),
        region_name='eu-west-1')
    client = session.client(
        service_name='secretsmanager',
        endpoint_url=os.environ.get('ENDPOINT_URL')
    )
    
    get_secret_value_response = client.get_secret_value(
            SecretId=name
    )

    secret = get_secret_value_response['SecretString']
    try:
        secret = json.loads(secret)
    except json.decoder.JSONDecodeError:
        secret = ast.literal_eval(secret)

    return secret