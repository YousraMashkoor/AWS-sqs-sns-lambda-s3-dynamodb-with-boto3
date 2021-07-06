
#Talk python to me

import json
import boto3
import os
from botocore.client import Config
from botocore.exceptions import ClientError
import logging

# s3 = boto3.client('s3',
#     aws_access_key_id="yousra", 
#     aws_secret_access_key="yousra",
#     endpoint_url='http://%s:4566' % os.environ['LOCALSTACK_HOSTNAME']
#     )

def create_presigned_url(bucket_name, bucket_key):
    """Generate a presigned URL for the S3 object
    :param bucket_name: string
    :param bucket_key: string
    :return: Presigned URL as string. If error, returns None.
    """
    expiration=3600
    signature_version='s3v4'
    # region = config.get('aws_default_region')

    s3_client = boto3.client('s3',
                             config=Config(signature_version=signature_version),
                             region_name='us-east-1',
                             endpoint_url='http://localhost:4566'
                             )
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': bucket_key},
                                                    ExpiresIn=expiration)
        # print(s3_client.list_buckets()['Owner'])

        # for key in s3_client.list_objects(Bucket=bucket_name, Prefix=bucket_key)['Contents']:
        #     print(key['Key'])
    except ClientError as e:
        logging.error(e)
        return None
    # The response contains the presigned URL
    return response

generated_signed_url = create_presigned_url('yousrabucket', 'data.json')
print(generated_signed_url)

