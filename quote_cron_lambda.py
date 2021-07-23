import json
import random
import boto3


def lambda_handler(event, context):
    
    # Get a quote from Quotes' table
    def get_quotes(id, dynamodb=None):
        if not dynamodb:
            dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
    
        table = dynamodb.Table('Quotes')
    
        try:
            response = table.get_item(Key={'id': id})
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response['Item']
        
    # Get item counts in table
    # Need to wait for 6 hrs for function to sync with database
    def get_number_of_items(dynamodb=None):
        dynamodb_client = boto3.client('dynamodb')
        
        response = dynamodb_client.describe_table(
        TableName='Quotes'
        )  
        return response['Table']['ItemCount']
    
    
    # insert quote into Quote-of-the-day table
    # overwrite quote everyday using same id
    def insert_quotes(id, context, Table_name, dynamodb=None):
        if not dynamodb:
            dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
    
        table = dynamodb.Table(Table_name)
        response = table.put_item(
        Item={
                'id' : id,
                'Author': context['Author'],
                'Quote': context['Quote']
            }
        )
        return response


    def random_quote():
        context = {}
        
        # Get random quote from Quotes' table
        quote_id = random.randint(1, get_number_of_items())
        quotes = get_quotes(quote_id)
    
        context['Author'] = quotes['Author']
        context['Quote'] = quotes['Quote']
        
            
        # insert quote into Quote-of-the-day table
        insert_quotes(1, context, 'Quote-of-the-day')

        

    random_quote()