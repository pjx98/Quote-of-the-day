import json
import boto3



def lambda_handler(event, context):
    
    daily_quote = get_quotes(1)
    
    quote = daily_quote['Quote']
    author = daily_quote['Author']
    
    client = boto3.client('sns')

    
    response = client.publish(
        TopicArn= 'arn:aws:sns:ap-southeast-1:996122235934:lambda_email_topic',
        Message= quote + " by " + author,
        Subject='Your Quote for the day!',
        )
    
    

def get_quotes(id, dynamodb=None):
        if not dynamodb:
            dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
    
        table = dynamodb.Table('Quote-of-the-day')
    
        try:
            response = table.get_item(Key={'id': id})
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response['Item']