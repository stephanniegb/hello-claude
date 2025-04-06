import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic(api_key=api_key)

def generate_questions(topic,num_questions):
    response = client.messages.create(
         model="claude-3-haiku-20240307",
         # Maximum number of tokens (words/characters) in the response
         max_tokens=500,
         # Instructions that define Claude's role and behavior (like a character prompt)
         system=f"You are an expert on {topic}, generate thought provoking questions that are fun and engaging. You should generate {num_questions} questions.",
         messages=[{
             "role":"user",
             "content":f"Generate {num_questions} questions about {topic} as a numbered list."
         }],
         # Tells Claude when to stop generating (here, after the last question number)
         stop_sequences=[f"{num_questions+1}"]
         # For more details on these parameters, see: https://github.com/anthropics/courses/blob/master/anthropic_api_fundamentals/04_parameters.ipynb
    )
    return response.content[0].text

def main():
    topic = input("Enter a topic: ")
    num_questions = int(input("Enter the number of questions: "))
    questions = generate_questions(topic,num_questions)
    print("\nGenerated Questions:")
    print(questions)

if __name__ == "__main__":
    main()
    
    