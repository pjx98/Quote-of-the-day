import json
import boto3 
import count_file

def lambda_handler(event, context):

    # Get the service resource
    sqs = boto3.resource('sqs')
    
    # Get the queue
    queue = sqs.get_queue_by_name(QueueName='quotes_queue')
    
    # get author and quote value from message attributes
    message_attributes = event['Records'][0]
    author = message_attributes["messageAttributes"]["Author"]["stringValue"]
    quote = message_attributes["messageAttributes"]["Quote"]["stringValue"]

    context = {}
    context['Author'] = author
    context['Quote'] = quote
    insert_quotes(count_file.count, context, 'Quotes')
    count_file.count += 1
    
    client = boto3.client('sqs')
    response = client.delete_message(
        QueueUrl='https://sqs.ap-southeast-1.amazonaws.com/996122235934/quotes_queue',
        ReceiptHandle= message_attributes["receiptHandle"]
    )
    

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

