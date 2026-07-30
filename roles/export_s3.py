import csv

import boto3
from botocore.config import Config
from botocore.exceptions import ClientError

my_config = Config(connect_timeout=5, read_timeout=5)
s3_client = boto3.client('s3', region_name='eu-central-1', config=my_config)

BUCKET_NAME = "devops-maciek-test-bucket-2026"

obiekty = s3_client.list_objects_v2(Bucket=BUCKET_NAME)

with open('raport.csv', 'w', encoding='utf-8') as f:
    f.write("Nazwa,RozmiarKB\n")

    for obj in obiekty.get('Contents', []):
            obj_name = obj['Key']
            obj_size = obj['Size'] / 1024
            f.write(f"{obj_name},{obj_size:.2f}\n")