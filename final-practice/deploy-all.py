import boto3
import time
import subprocess
import socket
from botocore.config import Config
from botocore.exceptions import ClientError


my_config = Config(
    connect_timeout=5,
    read_timeout=5,
    retries={'max_attempts': 3}
)
KEY_PAIR_NAME = "klucz-aws-frankfurt"
KEY_FILE_PATH = "~/.ssh/klucz-aws-frankfurt.pem"


ec2_client = boto3.client('ec2', region_name='eu-central-1', config=my_config)
print("🚀 Inicjalizacja tworzenia nowej maszyny EC2 w AWS...")

try:
    response = ec2_client.run_instances(
        ImageId='ami-0303e2e4a29f041a3',
        InstanceType='t3.micro',
        MinCount=1,                       
        MaxCount=1,      
        KeyName=KEY_PAIR_NAME,                 
        TagSpecifications=[             
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': 'Serwer-Aplikacji-Dev'},
                    {'Key': 'Environment', 'Value': 'Dev'}
                ]
            }
        ]
    )

    new_instance_id = response['Instances'][0]['InstanceId']
    print(f"✅ SUKCES! Maszyna EC2 została zlecona do utworzenia.")
    print(f"🆔 ID nowej instancji: {new_instance_id}")

except ClientError as e:
    print(f"❌ BŁĄD AWS podczas tworzenia maszyny: {e}")

print("\n⏳ Czekam, az AWS przydzieli Publiczne IP...")
time.sleep(15)

instances_info = ec2_client.describe_instances(InstanceIds=[new_instance_id])
public_ip = instances_info['Reservations'][0]['Instances'][0].get('PublicIpAddress')

if not public_ip:
    raise Exception("Nie udalo sie pobrac Publicznego IP!")

print(f"📍 PUBLIC IP MASZYNY: {public_ip}")

inventory_content = f"""[webservers]
ec2_target ansible_host={public_ip} ansible_user=ubuntu ansible_ssh_private_key_file={KEY_FILE_PATH} ansible_ssh_common_args='-o StrictHostKeyChecking=no'
"""

with open("inventory.ini", "w") as f:
            f.write(inventory_content)


time.sleep(10)

ansible_cmd = ["ansible-playbook", "-i", "inventory.ini", "site.yml"]
result = subprocess.run(ansible_cmd, capture_output=False, text=True)