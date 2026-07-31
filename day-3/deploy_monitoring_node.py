import boto3
from botocore.config import Config
from botocore.exceptions import ClientError

# 1. Konfiguracja połączenia
my_config = Config(connect_timeout=5, read_timeout=5, retries={'max_attempts': 3})
ec2_client = boto3.client('ec2', region_name='eu-central-1', config=my_config)

# 2. Skrypt Bash (User Data), który wykona się SAM na nowej maszynie!
user_data_script = """#!/bin/bash
apt-get update -y
apt-get install -y nginx
apt-get install -y htop
systemctl start nginx
systemctl enable nginx
echo "<h1>📊 NODE MONITORING REPORT</h1>" > /var/www/html/index.html
echo "<p>Nazwa hosta: $(hostname)</p>" >> /var/www/html/index.html
echo "<p>Czas działania systemu: $(uptime -p)</p>" >> /var/www/html/index.html
echo "<p>Wersja jądra: $(uname -r)</p>" >> /var/www/html/index.html
"""

print("🚀 Tworzę serwer EC2 z automatyczną konfiguracją Nginx...")

try:
    response = ec2_client.run_instances(
        ImageId='ami-0303e2e4a29f041a3',  # Przykładowe AMI Ubuntu w eu-central-1 (lub użyj swojego sprawdzonego)
        InstanceType='t3.micro',
        MinCount=1,
        MaxCount=1,
        UserData=user_data_script,  # 👈 TUTAJ Przekazujemy nasz skrypt Bash!
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': 'Monitoring-Node-Dev'},
                    {'Key': 'Role', 'Value': 'Monitoring'},
                    {'Key': 'Owner', 'Value': 'Maciek'}
                ]
            }
        ]
    )

    instance_id = response['Instances'][0]['InstanceId']
    print(f"✅ Maszyna utworzona! Instance ID: {instance_id}")
    print("⏳ AWS uruchamia serwer i wykonuje Twój skrypt Bash w tle...")

except ClientError as e:
    print(f"❌ BŁĄD AWS: {e}")