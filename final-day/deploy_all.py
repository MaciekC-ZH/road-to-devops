import boto3
import time
import subprocess
import socket
from botocore.config import Config
from botocore.exceptions import ClientError

# --- KONFIGURACJA ---
KEY_PAIR_NAME = "klucz-aws-frankfurt"  # ⚠️ Wpisz nazwe swojego klucza w AWS
KEY_FILE_PATH = "~/.ssh/klucz-aws-frankfurt.pem"  # ⚠️ Ścieżka do klucza .pem w WSL
REGION = "eu-central-1"
AMI_ID = "ami-0303e2e4a29f041a3"  # Ubuntu w eu-central-1

my_config = Config(connect_timeout=5, read_timeout=5, retries={'max_attempts': 3})
ec2_client = boto3.client('ec2', region_name=REGION, config=my_config)


def wait_for_ssh(ip, port=22, timeout=60):
    """Pomocnicza funkcja: Czeka, az port SSH na serwerze faktycznie zacznie odpowiadac."""
    print(f"⏳ Czekam na otwarcie portu SSH ({ip}:{port})...")
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with socket.create_connection((ip, port), timeout=3):
                print("✅ Port SSH jest otwarty i gotowy na polaczenie!")
                return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            time.sleep(3)
    return False


def main():
    print("\n==================================================")
    print("🚀 [STEP 1/4] Tworzenie instancji EC2 za pomoca Boto3...")
    print("==================================================")

    try:
        response = ec2_client.run_instances(
            ImageId=AMI_ID,
            InstanceType='t3.micro',
            MinCount=1,
            MaxCount=1,
            KeyName=KEY_PAIR_NAME,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {'Key': 'Name', 'Value': 'Final-Hybrid-EC2'},
                        {'Key': 'Project', 'Value': 'Consolidation-Week'}
                    ]
                }
            ]
        )

        instance_id = response['Instances'][0]['InstanceId']
        print(f"✅ Utworzono instancje: {instance_id}")

        print("\n⏳ Czekam, az AWS przydzieli Publiczne IP...")
        time.sleep(15)

        # Pobieramy szczegóły maszyny
        instances_info = ec2_client.describe_instances(InstanceIds=[instance_id])
        public_ip = instances_info['Reservations'][0]['Instances'][0].get('PublicIpAddress')

        if not public_ip:
            raise Exception("Nie udalo sie pobrac Publicznego IP!")

        print(f"📍 PUBLIC IP MASZYNY: {public_ip}")

        # --- STEP 2: GENEROWANIE INVENTORY.INI ---
        print("\n==================================================")
        print("📝 [STEP 2/4] Generowanie dynamicznego pliku inventory.ini...")
        print("==================================================")

        inventory_content = f"""[webservers]
ec2_target ansible_host={public_ip} ansible_user=ubuntu ansible_ssh_private_key_file={KEY_FILE_PATH} ansible_ssh_common_args='-o StrictHostKeyChecking=no'
"""
        with open("inventory.ini", "w") as f:
            f.write(inventory_content)

        print("✅ Plik inventory.ini zostal wygenerowany pomyślnie!")

        # --- STEP 3: WAIT FOR SSH ---
        print("\n==================================================")
        print("🔍 [STEP 3/4] Weryfikacja gotowosci sieciowej serwera...")
        print("==================================================")
        
        if not wait_for_ssh(public_ip):
            print("❌ Port SSH nie odpowiedzial w wymaganym czasie!")
            return

        # Dajemy dodatkowe 5 sekund na stabilizacje SSH
        time.sleep(5)

        # --- STEP 4: URUCHOMIENIE ANSIBLE PLAYBOOK ---
        print("\n==================================================")
        print("🔧 [STEP 4/4] Automatyczne wywolanie Ansible Playbook...")
        print("==================================================")

        ansible_cmd = ["ansible-playbook", "-i", "inventory.ini", "site.yml"]
        
        # Wywołujemy Ansible z poziomu Pythona
        result = subprocess.run(ansible_cmd, capture_output=False, text=True)

        if result.returncode == 0:
            print("\n==================================================")
            print("🎉 SUCCESS! CAŁY PIPELINE ZAKOŃCZONY SUKCESEM!")
            print(f"🌐 Wejdz w przegladarce na: http://{public_ip}")
            print("==================================================")
        else:
            print(f"\n❌ Błąd podczas wykonywania Ansible Playbook! Kod wyjścia: {result.returncode}")

    except ClientError as e:
        print(f"❌ BŁĄD AWS API: {e}")
    except Exception as e:
        print(f"❌ BŁĄD SYSTEMOWY: {e}")


if __name__ == "__main__":
    main()