"""Provision a simple EC2 instance (example)
WARNING: This will create resources that may incur AWS charges.
Usage: python3 provision_ec2.py
"""
import os
import boto3
from dotenv import load_dotenv

load_dotenv()
REGION = os.getenv('AWS_REGION') or os.getenv('AWS_DEFAULT_REGION') or 'us-east-1'

def create_ec2_instance():
    ec2 = boto3.resource('ec2', region_name=REGION)

    # NOTE: Replace the AMI, InstanceType, KeyName and SecurityGroupIds as per your environment.
    # The following AMI is a placeholder and may not be available in your region.
    AMI = os.getenv('AMAZON_LINUX_2_AMI', 'ami-0c94855ba95c71c99')  # example for us-east-1 (may vary)
    INSTANCE_TYPE = os.getenv('INSTANCE_TYPE', 't2.micro')
    KEY_NAME = os.getenv('KEY_NAME')  # optional: your existing key pair name
    SECURITY_GROUP_IDS = []  # optional: add sg ids if needed

    print(f"Launching EC2 instance: AMI={AMI}, Type={INSTANCE_TYPE}")
    instances = ec2.create_instances(
        ImageId=AMI,
        MinCount=1,
        MaxCount=1,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME if KEY_NAME else None,
        SecurityGroupIds=SECURITY_GROUP_IDS if SECURITY_GROUP_IDS else None
    )

    instance = instances[0]
    print("Waiting for instance to run...")
    instance.wait_until_running()
    instance.reload()
    print(f"Instance launched. ID: {instance.id}, State: {instance.state['Name']}")
    print(f"Public DNS: {instance.public_dns_name}")
    return instance.id

if __name__ == '__main__':
    iid = create_ec2_instance()
    print("Launched instance id:", iid)

