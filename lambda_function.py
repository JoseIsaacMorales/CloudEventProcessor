import boto3
import json
from datetime import datetime, timedelta


dynamodb = boto3.resource('dynamodb', region_name="us-east-2")
table = dynamodb.Table("ArchivosS3")
sns = boto3.client('sns', region_name="us-east-2")
topic_arn = "arn:aws:sns:us-east-2:720736520711:Alertas-proyecto1" 



def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        size = record['s3']['object']['size']
        
        # Tiempo UTC-6
        timestamp_utc = datetime.utcnow()
        timestamp_local = timestamp_utc - timedelta(hours=6)  
        timestamp_str = timestamp_local.isoformat()

        try:
            # Guardar en DynamoDB
            table.put_item(
                Item={
                    'fileName': key,
                    'bucket': bucket,
                    'size': size,
                    'uploadedAt': timestamp_str
                }
            )

            # Log de confirmación
            print(f"[CONFIRMACIÓN] Archivo '{key}' registrado correctamente a las {timestamp_str}")

            # Enviar alerta a SNS
            sns.publish(
                TopicArn=topic_arn,
                Subject="Nuevo archivo subido",
                Message=f"Se subió el archivo '{key}' al bucket '{bucket}' a las {timestamp_str}."
            )

        except Exception as e:
            # Log de error
            print(f"[ERROR] No se pudo registrar '{key}': {str(e)}")

    return {
        'statusCode': 200,
        'body': json.dumps('Proceso terminado, revisa CloudWatch Logs y tu correo')
    }

