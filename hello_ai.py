from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))

#send a question to the AI model
response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
        {"role": "user",
         "content": "What is Artificial Intelligence?"
         }
    ])

# Display the response
print(response.choices[0].message.content)
                                          