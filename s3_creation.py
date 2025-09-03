"""Create an S3 bucket and list buckets (example)
Usage: python3 provision_s3.py <bucket-name>
"""
import sys, os
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()

REGION = os.getenv('AWS_REGION') or os.getenv('AWS_DEFAULT_REGION') or 'us-east-1'

def create_bucket(bucket_name, region=REGION):
    s3 = boto3.client('s3', region_name=region)
    try:
        if region == 'us-east-1':
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(Bucket=bucket_name,
                             CreateBucketConfiguration={'LocationConstraint': region})
        print(f"Created bucket: {bucket_name}")
    except ClientError as e:
        print("Error creating bucket:", e)
        raise

def list_buckets():
    s3 = boto3.client('s3', region_name=REGION)
    resp = s3.list_buckets()
    print("Buckets:")
    for b in resp.get('Buckets', []):
        print(" -", b['Name'])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 provision_s3.py <bucket-name>")
        sys.exit(1)
    bucket = sys.argv[1]
    create_bucket(bucket)
    list_buckets()

Kun
