import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def summarize(text):

    # create prompt
    prompt = "Write a concise summary of the following content: \n"
    prompt += text

    # ping model and generate a response
    client = OpenAI()

    response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
)

    # clean up response to just the actual String value and return
    answer = response["choices"][0]["text"].strip()
    return answer
