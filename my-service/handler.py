import json


def hello(event, context):
    body = {
        "message": "Ola Mundo! - Python 3.8 - AWS Lambda - AWS SAM - teste de deploy"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
