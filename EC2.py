import boto3
from datetime import datetime

# Configuracion del  bucket
bucket_name = 'proyecto-1jimj'
region = 'us-east-2'

# Conexion con  S3
s3 = boto3.client('s3', region_name=region)

# Listar archivos
response = s3.list_objects_v2(Bucket=bucket_name)

print(f"--- Archivos en el bucket ({datetime.now()}) ---")
for obj in response.get('Contents', []):
    print(f"Nombre: {obj['Key']}, Tamaño: {obj['Size']} bytes")