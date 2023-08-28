"""
Retrieve the value of a secret from AWS Secrets Manager using the LocalStack endpoint URL
"""

import boto3
from botocore.exceptions import NoCredentialsError


def get_secret_value(secret_name: str, region_name: str, endpoint_url: str) -> str:
    """
    Retrieve the value of a secret from AWS Secrets Manager
    """
    try:
        # Create a Secrets Manager client with the LocalStack endpoint URL
        client = boto3.client(
            "secretsmanager", region_name=region_name, endpoint_url=endpoint_url
        )

        # Retrieve the secret value
        response = client.get_secret_value(SecretId=secret_name)

        # Return the secret value
        if "SecretString" in response:
            return response["SecretString"]
        else:
            # If the secret is stored as binary, you can access it using response['SecretBinary']
            return ""

    except NoCredentialsError:
        return "Error: AWS credentials not found."


secret_names = ["secret1", "secret2", "secret3"]
region_name = "us-east-1"
localstack_url = "http://localhost:4566"

secret_values = []
for secret_name in secret_names:
    secret_value = get_secret_value(secret_name, region_name, localstack_url)

    if secret_value:
        secret_values.append(secret_value)
        print("Secret name:", secret_name, "Secret Value:", secret_value)
    else:
        secret_values.append("")
        print("Failed to retrieve the secret value.")

print(secret_values)
