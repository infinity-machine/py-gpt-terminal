import os
import sys
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

messages = [{
        "role": "system",
        "content": "Just do your best you helpful boy you!"
}]

def main():
    while True:
        user_input = input('USER: ')
        if user_input.lower() in ('exit', 'quit'):
            print('SAYONARA!')
            sys.exit()
        if user_input:
            messages.append({
                    "role": "user",
                    "content": user_input
                })
            chat_completion = openai.ChatCompletion.create(
                model='gpt-3.5-turbo', messages=messages
            )
        gpt_response = chat_completion.choices[0].message.content
        print(f"GPT: {gpt_response}")
        messages.append({
            'role': 'assistant',
            'content': gpt_response
        })
        
main()