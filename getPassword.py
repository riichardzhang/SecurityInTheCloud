
import boto3
from botocore.exceptions import ClientError

def get_secret():

    secret_name = "rds!db-1621541f-6617-4099-8a4a-667023a11808"
    region_name = "ap-southeast-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name,
        aws_access_key_id='AKIA3ASL2ZNEEW4DG2WN',
        aws_secret_access_key= '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'
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']

    return secret[35:-2]

get_secret()
