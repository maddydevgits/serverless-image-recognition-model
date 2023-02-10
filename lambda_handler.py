import boto3
import base64

def lambda_handler(event, context):
    # Get the image data from the event
    base64_message = event['image']
    
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)

    # Connect to AWS Rekognition
    rekognition = boto3.client('rekognition')

    # Call the detect_labels function
    response = rekognition.detect_labels(Image={'Bytes': message_bytes})

    # Return the response
    return response
