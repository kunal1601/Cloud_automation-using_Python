"""Describe EC2 instances and fetch CloudWatch CPUUtilization (example)
Usage: python3 monitor_ec2.py
"""
import os
import boto3
import datetime
from dotenv import load_dotenv

load_dotenv()
REGION = os.getenv('AWS_REGION') or os.getenv('AWS_DEFAULT_REGION') or 'us-east-1'

def describe_instances():
    ec2 = boto3.client('ec2', region_name=REGION)
    resp = ec2.describe_instances()
    instances = []
    for r in resp.get('Reservations', []):
        for i in r.get('Instances', []):
            instances.append({
                'InstanceId': i.get('InstanceId'),
                'State': i.get('State', {}).get('Name'),
                'InstanceType': i.get('InstanceType'),
                'PublicIp': i.get('PublicIpAddress')
            })
    return instances

def get_cpu_utilization(instance_id, period_minutes=5):
    cw = boto3.client('cloudwatch', region_name=REGION)
    end = datetime.datetime.utcnow()
    start = end - datetime.timedelta(minutes=period_minutes)
    resp = cw.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name':'InstanceId','Value': instance_id}],
        StartTime=start,
        EndTime=end,
        Period=60,
        Statistics=['Average']
    )
    datapoints = resp.get('Datapoints', [])
    if not datapoints:
        return None
    latest = sorted(datapoints, key=lambda x: x['Timestamp'])[-1]
    return latest.get('Average')

if __name__ == '__main__':
    instances = describe_instances()
    if not instances:
        print('No instances found.')
    else:
        print('Instances:')
        for ins in instances:
            print(f" - {ins['InstanceId']} ({ins['State']}) Type: {ins['InstanceType']} PublicIp: {ins.get('PublicIp')}")
            cpu = get_cpu_utilization(ins['InstanceId'], period_minutes=10)
            print(f"   CPU Avg (last 10m): {cpu if cpu is not None else 'No data'}")
