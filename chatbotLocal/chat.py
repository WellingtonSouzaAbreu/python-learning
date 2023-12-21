import os
import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import random
import pickle
from datetime import datetime
import re

import colorama 
from colorama import Fore, Style, Back
colorama.init()

with open('./docs/intents.json') as file:
    fileData = json.load(file)
    intents = fileData['intents']

scheduleData = {
    'day': '',
    'hour': '',
    'procedure': '',
}

numeros_por_extenso = {
    'um': 1, 'dois': 2, 'três': 3, 'quatro': 4, 'cinco': 5,
    'seis': 6, 'sete': 7, 'oito': 8, 'nove': 9, 'dez': 10,
    'onze': 11, 'doze': 12, 'treze': 13, 'catorze': 14, 'quinze': 15,
    'dezesseis': 16, 'dezessete': 17, 'dezoito': 18, 'dezenove': 19, 'vinte': 20,
    'vinte e um': 21, 'vinte e dois': 22, 'vinte e três': 23, 'vinte e quatro': 24, 'vinte e cinco': 25,
    'vinte e seis': 26, 'vinte e sete': 27, 'vinte e oito': 28, 'vinte e nove': 29, 'trinta': 30,
    'trinta e um': 31,
}

def chatInit():
    # Nesta parte, o código carrega o modelo de chatbot treinado (chat_model) 
    # e os objetos de pré-processamento, ou seja, o Tokenizer e o LabelEncoder
    model = getTrainedModel()
    labelEncoder = getTreinedLabelEncoder()
    tokenizer = getTrainedTokenizer()

    # Define sequência máxima de entrada
    maxInputLenght = 20

    clearTerminal()
    print(Fore.YELLOW + 'Bot iniciado... Digite "x" para sair' + Style.RESET_ALL)
           
    while True:              
        print(Fore.LIGHTBLUE_EX + 'User: ' + Style.RESET_ALL, end='')
        textInput = input()

        if textInput.lower() == 'x': break

        result = model.predict(
            keras.preprocessing.sequence.pad_sequences(
                tokenizer.texts_to_sequences([textInput]),
                truncating='post', maxlen=maxInputLenght
            )
        )

        # Decodifica o maior resultado
        tag = labelEncoder.inverse_transform([np.argmax(result)])

        print(tag)
        # Imprime resposta

        if tag == 'setDay':
            print('settingDay...')
            scheduleData['day'] = textInput
            """ regex_hoje = re.compile(r'\baa\b', re.IGNORECASE)
            res = regex_hoje.search(textInput) """

        if tag == 'setHour':
            print('settingHour...')
            formatterHour = convertDateText(textInput)
            print(formatterHour)
            scheduleData['hour'] = formatterHour

        if tag == 'setProcedure':
            print('settingProcedure...')
            scheduleData['hour'] = textInput

        if 'questions-cutMale' == tag:
            print('hasAQuestion')
            print('O corte masculino custa 30')

        if not isGreetingIntent(tag): 
            makeNewQuestions(tag)

        print(scheduleData)

        """ for intent in intents:
            if intent['tag'] == tag:
                # Escolhe uma resposta aleatória
                textResponse = []
                textResponse = random.choice(intent['responses'])

                print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, textResponse)
                break """

def makeNewQuestions(intentTag):
    if scheduleData['procedure'] == '':
        print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, 'O que você gostaria de agendar?')
        return

    if scheduleData['day'] == '':
        print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, 'Que dia gostaria de agendar?')
        return

    if scheduleData['hour'] == '':
        print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, 'Que horário?')
        return


def isGreetingIntent(tag):
    if tag == 'setDay' or tag == 'setHour' or tag == 'setProcedure': return False
    else: return True

def getTrainedModel():
    model = keras.models.load_model('./src/chat_model')
    return model

def getTreinedLabelEncoder():
    with open('./src/label_encoder.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
        return tokenizer

def getTrainedTokenizer():
    with open('./src/tokenizer.pickle', 'rb') as enc:
        tokenizer = pickle.load(enc)
        return tokenizer

def clearTerminal():
    os.system('clear')

def convertDateText(texto):
    padrao_horarios = re.compile(r'(\b\d{1,2}(?:(?:h(?:oras)?)?|\b)|\b(?:um|dois|três|quatro|cinco|seis|sete|oito|nove|dez|onze|doze|treze|catorze|quinze|dezesseis|dezessete|dezoito|dezenove|vinte|vinte e um|vinte e dois|vinte e três|vinte e quatro|vinte e cinco|vinte e seis|vinte e sete|vinte e oito|vinte e nove|trinta|trinta e um))(\s*(?:h(?:oras)?)?)?\b', re.IGNORECASE)

    match = padrao_horarios.search(texto)
    if match:
        horario_capturado = match.group(1)
        if horario_capturado.isdigit():
            # Se o horário capturado é um número, formata como "00:00"
            return f"{int(horario_capturado):02d}:00"
        else:
            # Se o horário capturado é por extenso, mapeie para números e formate como "00:00"
            numeros_por_extenso = {
                'um': 1, 'dois': 2, 'três': 3, 'quatro': 4, 'cinco': 5,
                'seis': 6, 'sete': 7, 'oito': 8, 'nove': 9, 'dez': 10,
                'onze': 11, 'doze': 12, 'treze': 13, 'catorze': 14, 'quinze': 15,
                'dezesseis': 16, 'dezessete': 17, 'dezoito': 18, 'dezenove': 19, 'vinte': 20,
                'vinte e um': 21, 'vinte e dois': 22, 'vinte e três': 23, 'vinte e quatro': 24, 'vinte e cinco': 25,
                'vinte e seis': 26, 'vinte e sete': 27, 'vinte e oito': 28, 'vinte e nove': 29, 'trinta': 30,
                'trinta e um': 31,
            }
            numero = numeros_por_extenso[horario_capturado.lower()]
            return f"{numero:02d}:00"
    return None

chatInit()
