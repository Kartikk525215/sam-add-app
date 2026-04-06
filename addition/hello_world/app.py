import json

def lambda_handler(event, context):
    # Get query parameters from URL
    params = event.get("queryStringParameters") or {}

    num1 = int(params.get("a", 0))
    num2 = int(params.get("b", 0))

    result = num1 + num2

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Sum is {result}"
        })
    }