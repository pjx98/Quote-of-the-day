import json
import random
import boto3


def get_number_of_items(dynamodb=None):
        dynamodb_client = boto3.client('dynamodb')
        
        response = dynamodb_client.describe_table(
        TableName='Quotes'
        )  
        return response['Table']['ItemCount']



count = get_number_of_items()
