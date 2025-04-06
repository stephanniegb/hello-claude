import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic(api_key=api_key)

# ANSI color codes
BLUE = "\033[94m"
GREEN = "\033[92m"
RESET = "\033[0m"


class ChatBot:
    def __init__(self):
        self.client = Anthropic(api_key=api_key)
        self.conversation_history = []
        self.system_prompt = """You are a helpful assistant that can answer questions and help with tasks."""
        self.greeting = f"{GREEN}Hello I am Lulu, your personal assistant; type 'quit' to end the conversation{RESET}"
        self.conclusion = f"{GREEN}Thank you for using Lulu, have a great day!{RESET}"
    
    def greet(self):
        return self.greeting
    
    def get_response(self,user_input):
        self.conversation_history.append({"role":"user","content":user_input})

        # Using basic streaming parameter approach
        # Creates a stream of message chunks that we can iterate through
        stream = self.client.messages.create(
            model="claude-3-haiku-20240307",
            system=self.system_prompt,
            messages=self.conversation_history,
            max_tokens=1000,
            stream=True
        )

        assistant_response = ""
        # Process each chunk as it arrives and print it immediately
        for chunck in stream:
            if(chunck.type == "content_block_delta"):
                content = chunck.delta.text
                print(f"{GREEN}{content}{RESET}", end="", flush=True)
                assistant_response += content

        print()

        self.conversation_history.append({"role":"assistant","content":assistant_response})

def main():
    chatbot = ChatBot()
    print(chatbot.greet())

    while True:
        user_input = input(f"{BLUE}You: {RESET}")
        if user_input.lower() in ['quit', 'exit']:
            print(f"{chatbot.conclusion}{RESET}")
            break
        chatbot.get_response(user_input)


if __name__ == "__main__":
    main()
                

# from anthropic import AsyncAnthropic
# import asyncio

# client = AsyncAnthropic(api_key=api_key)

# # Alternative approach using AsyncAnthropic and streaming helpers
# # This commented section shows how to use the SDK's built-in streaming utilities
# async def streaming_with_helpers():
#     async with client.messages.stream(
#         max_tokens=1024,
#         model="claude-3-haiku-20240307",
#         messages=[
#             {
#                 "role": "user",
#                 "content": "Write me sonnet about orchids",
#             }
#         ],
#     ) as stream:
#         # text_stream helper makes it easy to process text chunks
#         async for text in stream.text_stream:
#             print(text, end="", flush=True)

# async def main():
#     await streaming_with_helpers()

# asyncio.run(main())

# # For more details on streaming, see: https://github.com/anthropics/courses/blob/master/anthropic_api_fundamentals/05_Streaming.ipynb
        
    

        
        
        