from django.shortcuts import render
import boto3
from botocore.exceptions import ClientError
import random
import uuid


# read quote from table and display on web
def today_quote(request):
    context = {}
    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')

    table = dynamodb.Table('Quote-of-the-day')
    response = table.get_item(Key={'id': 1})
    
    context['Author'] = response['Item']['Author']
    context['Quote'] = response['Item']['Quote']
    
    return render(request, 'present-quote.html', context)

    
    

def show_all_items(request):
    
    dynamodb_client = boto3.client('dynamodb')
    response = dynamodb_client.scan(
        TableName='Quotes',
        ProjectionExpression='Author,Quote',
        )
    
    # print(response['Items'])
    
    author_lst = []
    for i in response['Items']:
        author = i['Author']['S']
        author_lst.append(author)
    # print(author_lst)
    
    quote_lst = []
    for j in response['Items']:
        quote = j['Quote']['S']
        quote_lst.append(quote)
    # print(quote_lst)
    
    context = {}
    context = {'Items' : zip(author_lst,quote_lst) }
    
    return render(request, 'all_items.html',context)

# send user-submitted quotes into SQS
def user_add_quote(request):
    
    if request.method == "POST":
        context = {}
        Author = request.POST.get('Author')
        Quote = request.POST.get('Quote')
        
        # Get the service resource
        sqs = boto3.resource('sqs')

        # Get the queue
        queue = sqs.get_queue_by_name(QueueName='quotes_queue')

        response = queue.send_message(
                    MessageBody='new quote', 
                    MessageAttributes={
                        'Author': {
                                'StringValue': Author,
                                'DataType': 'String'
                            },
                        'Quote': {
                                'StringValue': Quote,
                                'DataType': 'String'
                            }
                
                })

    
    return render(request, 'submit_quote.html')


def insert_user_email(request):
    
    if request.method == "POST":
        email = request.POST.get('Email')
        
        my_id = uuid.uuid4().hex
        dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
        
        table = dynamodb.Table('user-email')
        response = table.put_item(
        Item={
                'id' : my_id,
                'Email': email
            }
        )

    return render(request, 'email.html')