import boto3

bucket_name = 'proyecto-1jimj'
archivo_s3 = 'archivo6.txt' #El nombre que tendra en S3
archivo_local = 'archivo6.txt' # Ruta local del archivo
s3 = boto3.client('s3', region_name='us-east-2') # Conectar VS Code con S3 
s3.upload_file(archivo_local, bucket_name, archivo_s3) # Subir archivo
print(f"Archivo '{archivo_local}' subido a S3 en '{bucket_name}' correctamente!") #Confirmacion
