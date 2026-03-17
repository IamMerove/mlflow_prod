import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def prepare_minio():
    # On récupère les variables
    endpoint = os.getenv('MLFLOW_S3_ENDPOINT_URL', 'http://localhost:9000')
    key_id = os.getenv('AWS_ACCESS_KEY_ID')
    access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

    print(f"DEBUG: Tentative de connexion à {endpoint} avec l'ID {key_id}")

    s3 = boto3.client(
        's3',
        endpoint_url=endpoint,
        aws_access_key_id=key_id,
        aws_secret_access_key=access_key,
        region_name='us-east-1' 
    )

    try:
        response = s3.list_buckets()
        buckets = [b['Name'] for b in response['Buckets']]
        if 'mlflow' not in buckets:
            s3.create_bucket(Bucket='mlflow')
            print("✅ Bucket 'mlflow' créé avec succès.")
        else:
            print("ℹ️ Le bucket 'mlflow' existe déjà.")
    except Exception as e:
        print(f"❌ Erreur détaillée : {type(e).__name__} - {e}")

if __name__ == "__main__":
    prepare_minio()