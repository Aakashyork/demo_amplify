import json

def handler(event, context):
  print('received event:')
  print(event)
  a = 5
  b = 6
  c = a +b
  console.log(c)
  return {
      'statusCode': 200,
      'headers': {
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
      },
      'body': json.dumps()
  }