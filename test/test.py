import json

def handler(event, context):

    print 'Error Test!'

    return {
        'statusCode': 200,
        'body': json.dumps('Error Test!')
    }