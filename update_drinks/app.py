import json
import boto3
import my_module

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('drink-drinks')


def custom_update(table,data):
    try:
        table.update_item(
            Key={
                'userID' :  data.get("userID"),
                'eventID' :  data.get("eventID"),
            },
            AttributeUpdates={ 
                key:{"Value":data.get(key)} for key in data if key not in ["userID","eventID"]
            }
        )
    except:
        table.put_item(
            Item=data
        )

    return "L'élément a bien été mis à jour",{}

def myfunc(event):
    body = json.loads(event["body"])


    if event.get("httpMethod") == "PUT":
        msg,data = custom_update(table,body)
    elif event.get("httpMethod") == "PATCH":
        msg,data = custom_update(table,body)
    
    return msg,data

def lambda_handler(event, context):
    return my_module.trycatch(lambda : myfunc(event))