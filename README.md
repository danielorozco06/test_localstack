# Localstack

## Requirements

- WSL
- Docker environment
- Python 3.X
- Pip

## Installation

```sh
# Install localstack
python3 -m pip install localstack 
```

## Process

```sh
# Go to path
cd local_jobs/localstack

# Start docker and install/start localstack
./start.sh

# Set environment variables
export AWS_ACCESS_KEY_ID="test"
export AWS_SECRET_ACCESS_KEY="test"
export AWS_DEFAULT_REGION="us-east-1"

# Create secret
python3 create_secret.py

# Get secret
python3 get_secret_value.py

# Stop localstack and docker
./stop.sh
```
