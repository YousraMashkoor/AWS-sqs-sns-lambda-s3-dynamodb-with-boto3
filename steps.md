
## 1. Create S3 bucket and Upload document:
awslocal s3 mb s3://yousrabucket
awslocal s3 cp data.json s3://yousrabucket
## 2. Generate presigned URL:
python read3.py 
