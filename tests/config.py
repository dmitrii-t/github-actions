import os
import boto3


dynamodb = boto3.client(service_name='dynamodb',
                        endpoint_url=os.getenv('DYNAMODB_ENDPOINT', 'http://localhost:4566'))
