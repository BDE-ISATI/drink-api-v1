import json
import boto3
import my_module

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('drink-users')

def myfunc():
    response = table.scan()
    events = response['Items']
    events.sort(key=lambda x: x.get('ordre',99999))
    return "ok",events

def lambda_handler(event, context):
    return my_module.trycatch(myfunc)