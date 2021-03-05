
#Talk python to me

import json
import boto3
import sys
import subprocess

subprocess.call('pip install requests -t /tmp/ --no-cache-dir'.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
sys.path.insert(1, '/tmp/')


import requests


def lambda_handler(event,context):
   print("lambda running")
