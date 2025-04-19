from openai import OpenAI
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# Set OpenAI API key

MODEL_NAME = os.getenv("MODEL_NAME")
MODEL_API_URL = os.getenv("MODEL_API_URL")
client = OpenAI(api_key=os.getenv("MODEL_API_KEY"), base_url=MODEL_API_URL)


def get_completion(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages = messages,
    )
    return response.choices[0].message.content

print(get_completion("What is 1+1?"))