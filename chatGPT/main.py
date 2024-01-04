from openai import OpenAI

client = OpenAI(api_key='apiKey')

import requests

def main():
    # TODO: The 'openai.organization' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'openai(organization='org-84XXMSdppS6DlmdhjWtcgKiJ')'
    # openai.organization = 'org-84XXMSdppS6DlmdhjWtcgKiJ'

    system_message = f"""answer in capital letters"""
    user_message = f"""say hello word in upper case"""
    messages = [  
        {'role':'system', 'content': system_message},    
        {'role':'user', 'content': user_message},  
    ] 
    
    response = client.chat.completions.create(model='gpt-3.5-turbo',
        messages=messages,
        temperature=0,
        max_tokens=15
    )

    print(response.choices[0].message.content)
    



main()

""" def main():
    # : The 'openai.organization' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'openai(organization='org-84XXMSdppS6DlmdhjWtcgKiJ')'
    # openai.organization = 'org-84XXMSdppS6DlmdhjWtcgKiJ'
    client.models.list()
    print('running...')
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Say hello world!"}],
        "temperature": 0.7,
        "max_tokens":10
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.json()) """
