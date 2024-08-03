import json
import boto3
import my_module

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('drink-drinks')

def myfunc(event):
    body = json.loads(event["body"])


    if event.get("httpMethod") == "PUT":
        msg,data = my_module.insert(table,"ID",body)

    elif event.get("httpMethod") == "PATCH":
        msg,data = my_module.update(table,"ID",body)

    elif event.get("httpMethod") == "DELETE":
        msg,data = my_module.delete(table,"ID",body)
    
    return msg,data

def lambda_handler(event, context):
    return my_module.trycatch(lambda : myfunc(event))