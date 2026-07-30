import boto3
from botocore.config import Config

my_config = Config(connect_timeout=5, read_timeout=5)
s3_client = boto3.client('s3', region_name='eu-central-1', config=my_config)

BUCKET_NAME = "devops-maciek-test-bucket-2026"

print("🐳 [DOCKER] Uruchamiam skrypt Boto3 wewnątrz kontenera...")

try:
    response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)

    with open('/app/output/raport_docker.csv', 'w', encoding='utf-8') as f:
        f.write("Nazwa,RozmiarB\n")
        for obj in response.get('Contents', []):
            f.write(f"{obj['Key']},{obj['Size']}\n")

    print("✅ [DOCKER] Raport zapisany pomyślnie w /app/output/raport_docker.csv!")

except Exception as e:
    print(f"❌ [DOCKER] Błąd: {e}")

try:
    response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)
    liczba_plikow = 0
    laczny_rozmiar_kb = 0
    for obj in response.get('Contents', []):
        liczba_plikow += 1
        laczny_rozmiar_kb += obj['Size'] / 1024

    with open('/app/output/podsumowanie.txt', 'w', encoding='utf-8') as podsumowanie:
        podsumowanie.write("=== AUDYT S3 DOCKER ===\n")
        podsumowanie.write(f"Liczba plików: {liczba_plikow}\n")
        podsumowanie.write(f"Łączny rozmiar: {laczny_rozmiar_kb:.2f} KB\n")

except Exception as e:
    print(f"❌ [DOCKER] Błąd podczas pobierania listy obiektów: {e}")
    