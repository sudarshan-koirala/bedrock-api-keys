import requests
import os
from dotenv import load_dotenv
load_dotenv()

url = "https://bedrock-runtime.us-east-1.amazonaws.com/model/anthropic.claude-3-5-sonnet-20240620-v1:0/converse"

payload = {
    "messages": [
        {
            "role": "user",
            "content": [{"text": "Hello"}]
        }
    ]
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ['AWS_BEARER_TOKEN_BEDROCK']}"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)