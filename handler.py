import json
import boto3
import uuid

table_name = 'users'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def hello(event, context):
   
    result = None

    people = [
            { 'id' : '1', 'name' : 'Martha', 'lastname' : 'Rivera'},
            { 'id' : '2', 'name' : 'Nikki', 'lastname' : 'Wolf'},
            { 'id' : '3', 'name' : 'John', 'lastname' : 'Doe'},
        ]
    
    with table.batch_writer() as batch_writer:
        for person in people:
            item = {
                'id' : person['id'],
                'name'  : person['name'],
                'lastname': person['lastname']
            }
            print("> batch writing: {}".format(person['name']) )
            batch_writer.put_item(Item=item)
            
        result = f"Success. Added {len(people)} people to {table_name}."

    return {'message': result}


def find_all(event, context):
  data = table.scan()
  return data['Items']