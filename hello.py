# Import required libraries
from dotenv import load_dotenv
import os
from anthropic import Anthropic

# Load API key from .env file
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

# Create Claude client with API key (SDK will use ANTHROPIC_API_KEY env var if not specified)
client = Anthropic(api_key=api_key)

# Simple example: Ask Claude to tell a joke
response = client.messages.create(
     model="claude-3-haiku-20240307",  # Choose Claude model version (https://github.com/anthropics/courses/blob/master/anthropic_api_fundamentals/03_models.ipynb)
     max_tokens=100,                       # Limit response length
     messages=[
         {
             "role": "user",
             "content":"tell me a joke"
         }
     ]
)

# Commented out print statement for joke response
# print("Response: ", response.content[0].text)

# Translation function that takes a word and target language
def translate(text, target_language):
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=100,
        messages=[
            # Attempt to translate
            {
                "role": "user",
                "content": f"Translate the following word to {target_language} and make sure to return the word only: {text}"
            }
        ]
    )
    # Return translated text
    return response.content[0].text

# Test the translation function
print(translate("hello", "French"))
