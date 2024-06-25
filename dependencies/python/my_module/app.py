import json
import uuid

def trycatch(function):
    try :
        msg,data = function()

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin' : '*',
                'Access-Control-Allow-Methods': '*'
            },
            'body': json.dumps({"success" : 1,"message":msg,"data":data}, default=int)
        }
    except Exception as e:
        msg = f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}"
        
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin' : '*',
                'Access-Control-Allow-Methods': '*'
            },
            'body': json.dumps({"success" : 0,"erreur":f'{msg}',"data":{}}, default=int)
        }
    
def insert(table,pkey,data):
    retour = {}

    pkey_val = str(uuid.uuid4())
    
    data[pkey] = pkey_val
    retour[pkey] = pkey_val

    table.put_item(
        Item=data
    )

    return "L'élément a bien été inséré",retour

# def to_aws_type(val):
#     to_aws_type(data.get(key))
#     if isinstance(val, str):
#         return {"S": val}
#     if isinstance(val, int) or isinstance(val, float):
#         return {"N": str(val)}
#     if isinstance(val, None):
#         return {"NULL": True}
#     if isinstance(val, bool):
#         return {"BOOL": val}



def update(table,pkey,data):
    table.update_item(
        Key={
            'ID' :  data.get(pkey)
        },
        AttributeUpdates={ 
            key:{"Value":data.get(key)} for key in data if key != pkey
        }
    )

    return "L'élément a bien été mis à jour",{}

def delete(table,pkey,data):
    table.delete_item(
        Key={
            'ID' : str(data.get(pkey))
        }
    )
    return "L'élément a bien été supprimé",{}
