import boto3
import time
from botocore.config import Config

my_config = Config(connect_timeout=5, read_timeout=5)
ec2_client = boto3.client('ec2', region_name='eu-central-1', config=my_config)

# ⚠️ UPEWNIJ SIĘ, ŻE MASZ TEN KLUCZ W AWS (EC2 -> Key Pairs)!
KEY_PAIR_NAME = "klucz-aws-frankfurt"  # podmień na nazwę swojego klucza w AWS

print("🚀 Stawiam instancję EC2 pod konfigurację Ansible...")

try:
    response = ec2_client.run_instances(
        ImageId='ami-0303e2e4a29f041a3',  # Ubuntu 22.04/24.04 w eu-central-1
        InstanceType='t3.micro',
        MinCount=1,
        MaxCount=1,
        KeyName=KEY_PAIR_NAME,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': 'Ansible-Target-EC2'}]
            }
        ]
    )

    instance_id = response['Instances'][0]['InstanceId']
    print(f"⏳ Czekam na przydzielenie publicznego IP dla maszyny {instance_id}...")
    
    # Odczekujemy chwilę, aż AWS przydzieli adres IP
    time.sleep(15)

    instances_info = ec2_client.describe_instances(InstanceIds=[instance_id])
    public_ip = instances_info['Reservations'][0]['Instances'][0].get('PublicIpAddress')

    print(f"✅ Instancja gotowa!")
    print(f"📍 PUBLIC IP MASZYNY: {public_ip}")
    print(f"👉 Wpisz ten IP do swojego pliku inventory.ini!")

except Exception as e:
    print(f"❌ Błąd: {e}")