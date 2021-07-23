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
