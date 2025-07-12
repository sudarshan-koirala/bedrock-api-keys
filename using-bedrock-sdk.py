import boto3
from dotenv import load_dotenv
load_dotenv()

# Create an Amazon Bedrock client
client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"     # If you've configured a default region, you can omit this line
) 

# Define the model and message
model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"
messages = [{"role": "user", "content": [{"text": "Hello"}]}]
   
response = client.converse(
    modelId=model_id,
    messages=messages,
)

# Print the response
print(response['output']['message']['content'][0]['text'])