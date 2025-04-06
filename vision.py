import base64
from dotenv import load_dotenv
import os
from anthropic import Anthropic
import httpx

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

# For more details on vison prompting, see: https://github.com/anthropics/courses/blob/master/anthropic_api_fundamentals/06_vision.ipynb

# Local Image Processing
# 1. Open image file in binary mode
# 2. Read binary contents
# 3. Convert to base64
# 4. Convert to string

with open("./images/wolfgang-hasselmann-_EG_Th77EmQ-unsplash.jpg", "rb") as image_file:
    binary_data = image_file.read() 
    base_64_encoded_data = base64.b64encode(binary_data) 
    base64_string = base_64_encoded_data.decode('utf-8')

# Remote Image Processing
# 1. Fetch image from URL
# 2. Convert to base64 string
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Church_of_light.jpg/1599px-Church_of_light.jpg"
image_media_type = "image/jpeg"
image_data = base64.b64encode(httpx.get(image_url).content).decode("utf-8")

client = Anthropic(api_key=api_key)

# Create message with image and text
# Multiple images can be added as separate blocks in the content array
messages = [
    {
        "role": "user",
        "content": [
            {
                "type":"image",
                "source":{
                   "type":"base64",  # Supported types: base64 only currently
                   "media_type":"image/jpeg", # Supported formats: JPEG, PNG, WEBP, GIF
                   "data":base64_string #actual image data
                }
            },
            {
                "type":"text",
                "text": "Describe this image."
            }
        ]
    }
]
response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=2048,
    messages=messages,
)

print(response.content[0].text)


    