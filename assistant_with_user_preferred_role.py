from openai import OpenAI
from dotenv import load_dotenv
import os

# Load configuration
load_dotenv()

# Create AI client
client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))

print("=" * 40)
print("      My AI Assistant")
print("=" * 40)

roles = {
    "1": "You are a friendly school teacher. Explain every concept using simple language and real-life examples.",

    "2": "You are a senior Python developer. Explain programming concepts clearly and always include Python examples.",

    "3": "You are an experienced travel guide. Recommend places, food, transportation and travel tips.",

    "4": "You are a motivational coach. Encourage the user and give practical advice with a positive attitude.",

    "5": "You are a professional interviewer. Ask one interview question at a time and provide feedback after each answer."
}

print("\nChoose your assistant role from the following options:")
print("1. Friendly School Teacher")
print("2. Senior Python Developer")
print("3. Experienced Travel Guide")
print("4. Motivational Coach")
print("5. Professional Interviewer")

choice = input("\nEnter your choice : ")

messages = [
    {"role": "system",
     "content": roles.get(
         choice,
         "You are a helpful AI assistant. Provide assistance based on user queries."
         )
     }
    ]

while True:
    user_question= input("\nYou: ")
    messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )
    if user_question.lower() == "quit":
        print("\nAI: Goodbye! Have a great day.")
        break
      
       
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages)
    
    ai_response = response.choices[0].message.content
    
     # Save the AI's reply   
    messages.append(
        {
            "role": "assistant",
            "content": ai_response
        }
    )
    print("\nAI:", ai_response)
    