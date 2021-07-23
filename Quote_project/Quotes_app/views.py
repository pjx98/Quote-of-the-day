from django.shortcuts import render
import boto3
from botocore.exceptions import ClientError
import random
import uuid

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
     