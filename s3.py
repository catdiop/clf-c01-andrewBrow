import boto3
from botocore.config import Config

s3 = boto3.resource('s3', config=Config(signature_version="s3v4"))
for bucket in s3.buckets.all():
  print(bucket.name)