from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic(api_key=api_key)

conversation_history = []

while True:
    user_input = input("You: ")

    if(user_input.lower() in ["quit", "exit"]):
        print("Bye!")
        break
    conversation_history.append({"role":"user","content":user_input})
    response = client.messages.create(
          model="claude-3-7-sonnet-20250219",
          messages=conversation_history,
          max_tokens=500,
    )
    assistant_response = response.content[0].text
    print("Assistant: ", assistant_response)
    conversation_history.append({"role":"assistant","content":assistant_response})



