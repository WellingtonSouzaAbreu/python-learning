import json 
import numpy as np 
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
import pickle

def main():
    with open('./docs/intents.json') as file:
        fileData = json.load(file)
        intents = fileData['intents']
    
    trainingSentences = [] 
    trainingLabels = [] 
    labels = []
    responses = []

    for intent in intents:
        for pattern in intent['patterns']:
           trainingSentences.append(pattern)
           trainingLabels.append(intent['tag'])
        responses.append(intent['responses'])

        if intent['tag'] not in labels:
            labels.append(intent['tag'])

    # print(trainingSentences)
    # print(trainingLabels)
    # print(responses)
    # print(labels)

    numberOfLabels = len(labels)

    labelEncoder = LabelEncoder()
    labelEncoder.fit(trainingLabels)  # Analisa os rótulos e cria um mapeamento entre cada rótulo único e um valor numérico exclusivo
    trainingLabels = labelEncoder.transform(trainingLabels)  # Transforma os rótulos originaisem valores numéricos
    
    # Cada valor nesse vetor captura algum aspecto do significado da palavra "cachorro".
    # Por exemplo, o valor 0.8 pode representar o tamanho, indicando que "cachorro" é maior em relação a outras palavras. O valor -0.5 pode representar a agressividade, indicando que "cachorro" tem um significado negativo nesse aspecto.
    # Tamanho da dimensão do vetor de embedding para representar palavras A palavra "cachorro" pode ser representada como um vetor 16D, por exemplo: [0.2, 0.8, -0.4, 0.6, -0.3, 0.5, 0.1, -0.2, 0.9, -0.1, -0.5, 0.3, 0.7, -0.6, 0.4, -0.8].
    embeddingDim = 16 
    vocabularySize = 1000
    oovToken = "<OOV>"              # Token para palavras não encontradas ou fora do vocabulário(vocabularySize)
    maxLenght = 20                  # Comprimendo máximo dos tokens

    tokenizer = Tokenizer(num_words=vocabularySize, oov_token=oovToken) # Intancia o tokenizador
    tokenizer.fit_on_texts(trainingSentences)  # Alimentando tokenizador com as mensagens de treinamento
    # ['hi', 'hey'] = {'hi': 1, 'hey': 2}

    wordIndex = tokenizer.word_index   # Obtem o index de todas as palavras tokenizadas

    # Converte texto em sequencias de números inteiros. Cada palavra nas mensagens é substituída pelo seu índice numérico correspondente no vocabulário
    sequences = tokenizer.texts_to_sequences(trainingSentences) 
    # ['hi', 'hey'] = [[1,2], [3,4]]
    
    paddedSequences = pad_sequences(sequences, maxlen=maxLenght, truncating='post') # Deixa todos os tokens no mesmo tamanho
    
    # REDE NEURAL

    # Modelo de rede neural onde as camadas são empilhadas uma após a outra
    model = Sequential() 

    # Converte os índices numéricos das palavras em vetores de incorporação (word embeddings) de acordo com o vocabulário que você construiu.
    model.add(Embedding(vocabularySize, embeddingDim, input_length=maxLenght)) 

    # Operação de média global nas saídas da camada de incorporação, reduzindo a dimensionalidade. É útil para reduzir o número de parâmetros na rede neural e simplificar o modelo.
    model.add(GlobalAveragePooling1D()) 

    # Você está adicionando duas camadas densas (fully connected layers) com 16 unidades (neurônios) cada e função de ativação ReLU. 
    # Isso significa que cada camada tem 16 neurônios e usa a função de ativação ReLU para introduzir não linearidade na rede.
    model.add(Dense(16, activation='relu'))   
    model.add(Dense(16, activation='relu'))   

    # Adiciona a camada de saída com um número de unidades igual ao número de classes (intenções) que seu chatbot deve prever
    model.add(Dense(numberOfLabels, activation='softmax'))

    # Compilando modelo
    # Define a função de perda como 'sparse_categorical_crossentropy' para problemas de classificação multiclasse.
    # O otimizador 'adam' é usado para ajustar os pesos da rede durante o treinamento.
    # A métrica de avaliação é 'accuracy', que mede a precisão das previsões do modelo.
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Esta linha exibe um resumo do modelo, mostrando as camadas, o número de parâmetros e outras informações relevantes
    # model.summary()

    # Quantidades de treinamento, ajustando seus pesos para fazer previsões mais precisas.
    epocs = 700


    # print(paddedSequences) # [[ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 10 31 18]]
    # print(trainingLabels) # [1 2 3]
    history = model.fit(paddedSequences, np.array(trainingLabels), epochs=epocs)

    # Salva modelo treinado para usos futuros
    model.save('chat_model')

    # Salva o tokenizador para usos futuros como fluxo de bytes(pickling)
    # Digamos que você tenha treinado o modelo com um Tokenizer que converteu a palavra "hello" em [1] e "goodbye" em [2]. 
    # Quando você carrega o modelo mais tarde, você também deve carregar o mesmo Tokenizer 
    # para que ele saiba como converter palavras da mesma maneira.
    with open('tokenizer.pickle', 'wb') as handle:
        pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    # salva labelEncoder é salvo no arquivo "label_encoder.pickle". 
    # O LabelEncoder é usado para converter intenções (etiquetas) em números para treinamento e previsões.
    with open('label_encoder.pickle', 'wb') as ecn_file:   
        pickle.dump(labelEncoder, ecn_file, protocol=pickle.HIGHEST_PROTOCOL)
    
    
    print('running...')

main()

