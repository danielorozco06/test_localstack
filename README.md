# Process

```sh
./start.sh

export AWS_ACCESS_KEY_ID="test"
export AWS_SECRET_ACCESS_KEY="test"
export AWS_DEFAULT_REGION="us-east-1"

python3 create_secret.py

python3 get_secret_value.py

./stop.sh
```
