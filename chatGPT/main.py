from openai import OpenAI

client = OpenAI(api_key='')

import requests

def main():
    # TODO: The 'openai.organization' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'openai(organization='org-84XXMSdppS6DlmdhjWtcgKiJ')'
    # openai.organization = 'org-84XXMSdppS6DlmdhjWtcgKiJ'

    textInput = input("Enter your message: ")

    system_message = f"""The maximum characters in the response must be 15"""
    user_message = f"""{textInput}"""
    messages = [  
        {'role':'system', 'content': system_message},    
        {'role':'user', 'content': user_message},  
    ] 
    
    response = client.chat.completions.create(model='gpt-3.5-turbo',
        messages=messages,
        temperature=0,
        max_tokens=15
    )

    print(response.usage.total_tokens)
    print(response.choices[0].message.content)
    

main()