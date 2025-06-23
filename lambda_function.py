import json
from another import another_func



def lambda_handler(event, context):
    # Extract numbers from the event
    num1 = event.get('num1', 0)
    num2 = event.get('num2', 0)
    print("third ")

    # Calculate the sum
    result = num1 + num2
    return another_func(num1,num2,result)

    return {
        'statusCode': 200,
        'body': f'The sum of {num1} and {num2} is {result}.'
    }
