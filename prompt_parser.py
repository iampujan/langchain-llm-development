from openai import OpenAI
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# Set OpenAI API key

MODEL_NAME = os.getenv("MODEL_NAME")
MODEL_API_URL = os.getenv("MODEL_API_URL")
client = OpenAI(api_key=os.getenv("MODEL_API_KEY"), base_url=MODEL_API_URL)

# ChatApi OpenAI

def get_completion(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages = messages,
    )
    return response.choices[0].message.content

print(get_completion("What is 1+1?"))


customer_email = """
Arrr, I be fuming that me blender lid flew off and splattered me kitchen walls with smoothie! And to make matters worse,
the warranty don't cover the cost of cleaning up me kitchen. I need yer help right now, matey!
"""

style = """American English in a calm and respectful tone"""

prompt = f"""Translate the text \
that is delimited by triple backticks 
into a style that is {style}.
text: ```{customer_email}```
"""

print("prompt: ",prompt)
response = get_completion(prompt)
print("response: ",response)


