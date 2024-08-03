import json
import boto3
import my_module

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('drink-drinks')

def myfunc():
    response = table.scan()
    return "ok",events

def lambda_handler(event, context):
    return my_module.trycatch(myfunc)