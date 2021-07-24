import json
import boto3


def handle_insert(record):
    
    newImage = record['dynamodb']['NewImage']
    email = newImage['Email']['S']
    return email


def lambda_handler(event, context):

    client = boto3.client('sns')
    
    # record = event['Records'][0]
    # type = record['eventName']
    # print(event['Records'][0]['eventName'])
    
    
    if event['Records'][0]['eventName'] == 'INSERT':
    #email = event['Records'][0]['dynamodb']['NewImage']['Email']['S']
    
        email = event['Records'][0]['dynamodb']['NewImage']['Email']['S']
        
        client.subscribe(TopicArn='arn:aws:sns:ap-southeast-1:996122235934:lambda_email_topic',
                      Protocol='email',
                      Endpoint= email,
                      )