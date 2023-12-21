import os
import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import random
import pickle

import colorama 
from colorama import Fore, Style, Back
colorama.init()

with open('./docs/intents.json') as file:
    fileData = json.load(file)
    intents = fileData['intents']

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

        if textInput.lower() == 'x':
            break

        result = model.predict(
            keras.preprocessing.sequence.pad_sequences(
                tokenizer.texts_to_sequences([textInput]),
                truncating='post', maxlen=maxInputLenght
            )
        )

        # Decodifica o maior resultado
        tag = labelEncoder.inverse_transform([np.argmax(result)])

        # Imprime resposta
        for intent in intents:
            if intent['tag'] == tag:
                # Escolhe uma resposta aleatória
                textResponse = []
                textResponse = random.choice(intent['responses'])

                print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, textResponse)
                break


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

chatInit()
