import boto3

ec2_client = boto3.client('ec2', region_name='us-east-1')
ec2_resource = boto3.resource('ec2', region_name='us-east-1')

reservations = ec2_client.describe_instances()
for reservations in reservations['Reservations']:
    instances = reservations['Instances']
    for instance in instances:
        print(f"Status of Instance {instance['InstanceId']} is {instance['State']['Name']}")