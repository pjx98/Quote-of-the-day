import json
import boto3 
import count_file
def lambda_handler(event, context):
    
    
    # Get the service resource
    sqs = boto3.resource('sqs')
    
    # Get the queue
    queue = sqs.get_queue_by_name(QueueName='quotes_queue')
    
    
    for message in queue.receive_messages(MessageAttributeNames=['Author', 'Quote'], MaxNumberOfMessages=10):
        # Get the custom author message attribute if it was set
        if message.message_attributes is not None:
            author_name = message.message_attributes.get('Author').get('StringValue')
            quote_name = message.message_attributes.get('Quote').get('StringValue')
        

        author =  author_name
        quote = quote_name
        
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
        
        context = {}
        context['Author'] = author
        context['Quote'] = quote
        insert_quotes(count_file.count, context, 'Quotes')
        message.delete()
        count_file.count += 1
    

