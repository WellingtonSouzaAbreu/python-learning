import os
import spacy
import nltk

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Carregue o modelo de linguagem do spaCy em português
nlp = spacy.load('pt_core_news_sm')

# Texto de exemplo


def main():
    clearTerminal()

    text1 = 'Estou vendendo um sofá usado verde, aceito algo em troca, ele vai ser perfeito para a sua casa'
    text2 = 'Cuido do seu pet!. \nSou apaixonado por pets e me coloco a disposição \npara oferecer serviço de banhos e passeios para o seu! '
    text3 = 'Como comunidade nós focamos em inserir essas pessoas o mais rápido no mercado de trabalho, pois temos a vivência de pessoas que vieram da periferia e confirmamos que depois que entramos nesta área a nossa vida mudou 100%.Nós estamos aqui para levar a informação para a periferia e servir de grupo de apoio para que essas pessoas tenham as oportunidades que não tiveram ainda para chegar nesse universo.. Nossa missão é inserir pessoas de origem periférica na área de tecnologia.Sabemos que a área de desenvolvimento de software e tecnologia é grande e continua crescendo. É uma área de acesso democrático, pois o conteúdo necessário para trabalhar com isso está (quase sempre) livre e aberto na internet, mas para pessoas periféricas, com menos acesso a informação, ainda falta um certo apoio. '
    tags, originalText = extractTags(text2)

    print(originalText)
    print('\n')
    print(tags)


def clearTerminal():
    os.system('clear')


def extractTags(text):
    doc = nlp(text)

    tags = []
    for token in doc:
        word = token.text
        # Verifique se a palavra é um substantivo ou adjetivo
        if token.pos_ not in ['ADJ', 'VERB', 'ADV', 'ADP', 'PRON', 'DET', 'NUM', 'CCONJ', 'SCONJ', 'INTJ']:
            if token.pos_ in ['NPROP', 'NOUN']:
                if word not in stopwords.words('portuguese'):
                    tags.append(word)

    return tags, text


main()
