from anthropic import Anthropic
import random
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

class ChefBot:
    def __init__(self):
        self.client = Anthropic(api_key=api_key)
        self.conversation_history = []
        self.system_prompt = """You are ChefBot, an expert culinary assistant. You specialize in:
            - Providing detailed recipes and cooking instructions
            - Offering cooking tips and techniques
            - Suggesting ingredient substitutions
            - Answering questions about cooking methods
            - Providing nutritional advice
            Always maintain a friendly, chef-like personality and focus on culinary topics."""

        self.greetings = [
            "Hello! I'm Chef Bot, ready to cook up something delicious!",
            "Welcome to my virtual kitchen! What shall we make today?",
            "Hi there, food lover! Let's create something tasty!"
        ]

    def greet(self):
        return random.choice(self.greetings)

    def get_response(self, user_input):
        # Add user input to conversation history
        self.conversation_history.append({"role": "user", "content": user_input})

        response = self.client.messages.create(
            model="claude-3-haiku-20240307",
            system=self.system_prompt,  
            messages=self.conversation_history,
            max_tokens=500
        )

        assistant_response = response.content[0].text
        
        # Add assistant response to conversation history
        self.conversation_history.append({"role": "assistant", "content": assistant_response})
        
        return assistant_response

def main():
    chef = ChefBot()
    print(chef.greet())
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            print("Chef Bot: Goodbye! Happy cooking!")
            break
        
        response = chef.get_response(user_input)
        print("Chef Bot:", response)

if __name__ == "__main__":
    main()
