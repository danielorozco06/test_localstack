"""
This script creates a new secret in AWS Secrets Manager using the LocalStack
"""

import boto3
from botocore.exceptions import NoCredentialsError


def create_secret(
    secret_name: str, secret_value: str, region_name: str, endpoint_url: str
) -> str:
    """
    Create a new secret in AWS Secrets Manager
    """
    try:
        # Create a Secrets Manager client with the LocalStack endpoint URL
        client = boto3.client(
            "secretsmanager", region_name=region_name, endpoint_url=endpoint_url
        )

        # Create a new secret
        response = client.create_secret(Name=secret_name, SecretString=secret_value)

        # Return the ARN of the created secret
        return response["ARN"]

    except NoCredentialsError:
        return "Error: AWS credentials not found."


secret_name = "secret1"
secret_value = "daniel"
region_name = "us-east-1"
localstack_endpoint_url = "http://localhost:4566"

created_secret_arn = create_secret(
    secret_name, secret_value, region_name, localstack_endpoint_url
)
if created_secret_arn:
    print("Secret created with ARN:", created_secret_arn)
else:
    print("Failed to create the secret.")
