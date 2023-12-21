# import openai
# import pandas as pd
import requests
from hugchat import hugchat

def main():

    # start a new huggingchat connection
    chatbot = hugchat.ChatBot()

    # start a new conversation
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)

    # enter your message here
    msg = 'Why should I learn Python'

    # print the response
    print(chatbot.chat(msg))


# def main():
#     """ openai.organization = 'org-84XXMSdppS6DlmdhjWtcgKiJ'
#     openai.api_key = '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'
#     openai.Model.list() """
#     print('running...')
#     url = "https://api.openai.com/v1/chat/completions"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": "Bearer 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"
#     }

#     data = {
#         "model": "gpt-3.5-turbo",
#         "messages": [{"role": "user", "content": "Say this is a test!"}],
#         "temperature": 0.7
#     }

#     response = requests.post(url, headers=headers, json=data)

#     print(response.json())



main()
