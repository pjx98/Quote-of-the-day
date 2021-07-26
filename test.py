DynamoDB Stream Output:

{'Records': [
    {'eventID': '767498e3587e4959b18ae88f5606b372', 
     'eventName': 'INSERT', 
     'eventVersion': '1.1', 
     'eventSource': 'aws:dynamodb', 
     'awsRegion': 'ap-southeast-1', 
     'dynamodb': {
         'ApproximateCreationDateTime': 1627040387.0, 'Keys': 
             {'id': {'S': '31abf5113d0148fe9046d1c6051a6b03'}}, 
             'NewImage': {'Email': 
                 {'S': 'pjingxiang@gmail.com'}, 
                 'id': {'S': '31abf5113d0148fe9046d1c6051a6b03'}}, 
             'SequenceNumber': '412600000000020983975388', 
             'SizeBytes': 93, 'StreamViewType': 'NEW_IMAGE'}, 'eventSourceARN': 'arn:aws:dynamodb:ap-southeast-1:996122235934:table/user-email/stream/2021-07-23T11:21:09.733'}]}


{'ApproximateCreationDateTime': 1627041286.0, 
 'Keys': {
    'id': {'S': 'bab7d7598f2a47b6ba91b1f46e58787f'}
    }, 
 'NewImage': {
     'Email': {'S': 'pjingxiang@gmail.com'}, 
              'id': {'S': 'bab7d7598f2a47b6ba91b1f46e58787f'}
              }, 
 'SequenceNumber': '414400000000020984432489', 'SizeBytes': 93, 'StreamViewType': 'NEW_IMAGE'}


SQS output:
    
{
   "Records":[
      {
         "messageId":"64dd96f8-79d8-49d3-a8f7-933a3c92fb3a",
         "receiptHandle":"AQEBEfDIpKG0gVCZJecqRnvy8Ukbg0DK3QOjZKiLvKQSXXeM60bhGC3zNznohEccYcA7+dWCYQBf4VWHRwjF8N80uCzTPFuq6PrPitg+cLM06Uf+PW1qIFWSa1FCSEV+nlUjB2xTaS883XRkTPHsdC/FgwDEXABUpo4nPeWyP/yIqlSebFqUb/dD3l1K6Ap6q8tIUqlKEp89woL7uH5HDWdLyCu3LDD1trtYaPXOpKQgEg6V1rRtg7XOSwsykLobsqJTbKZfh9cuhj0d7XaEkU7GXEIiua5kvTWqx+vHScgm1noDCkSWHudOZbr+IiFGh7bEYI0bpZXPY0+YU2NyNQX9ugiboTgbPtgP9fm2p5fthSEUnkXNOhcnRs39QhSaczSYFRrKyqfcCrpLey9w8rioVw==",
         "body":"new quote",
         "attributes":{
            "ApproximateReceiveCount":"10",
            "SentTimestamp":"1627134001394",
            "SenderId":"AIDA6P3MDCQPDRLYZWZ6Z",
            "ApproximateFirstReceiveTimestamp":"1627134001394"
         },
         "messageAttributes":{
            "Quote":{
               "stringValue":"e5ue5u",
               "stringListValues":[
                  
               ],
               "binaryListValues":[
                  
               ],
               "dataType":"String"
            },
            "Author":{
               "stringValue":"e5ye5y",
               "stringListValues":[
                  
               ],
               "binaryListValues":[
                  
               ],
               "dataType":"String"
            }
         },
         "md5OfBody":"cf915fe1915a522edea1e8ee4c144b2e",
         "md5OfMessageAttributes":"4513b5d732f6a001659c757ee03a959f",
         "eventSource":"aws:sqs",
         "eventSourceARN":"arn:aws:sqs:ap-southeast-1:996122235934:quotes_queue",
         "awsRegion":"ap-southeast-1"
      }
   ]
}