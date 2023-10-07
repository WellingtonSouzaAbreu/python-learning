import string
from nltk import corpus, download, sent_tokenize, word_tokenize
from heapq import nlargest
# download('stopwords')
# download('punkt')

def estimateSummarizedTextSize(text):
    if text.count('. ') > 20:
        return int(round(text.count('. ')/10, 0))
    else:
        return 5
    
# textWithoutSymbols = [char for char in fileText if char not in string.punctuation] // Alternative
def removeTextSymbols(text): 
    textWithoutSymbols = text.translate(str.maketrans('', '', string.punctuation))
    textWithoutSymbols = ''.join(textWithoutSymbols)
    return textWithoutSymbols

def removeStopwords(text):
    processedText = []
    words = text.split()
    for word in words:
        if word.lower() not in corpus.stopwords.words('portuguese'):
            processedText.append(word)
    return processedText

def agroupWordFrequency(text):
    wordFrequency = {}
    for word in text:
        if word not in wordFrequency:
            wordFrequency[word] = 1
        else:
            wordFrequency[word] = wordFrequency[word] + 1
    return wordFrequency

def getMaximumWordFrequencyValue(wordFrequency):
    maximumWordFrequency = max(wordFrequency.values())
    return maximumWordFrequency

def tokenizePhrases(text):
    tokenizedPhrases = sent_tokenize(text, 'portuguese')
    return tokenizedPhrases

def normalizeWordFrequency(wordFrequency, maxWordFrequency):
    normalizedWordFrequency = wordFrequency
    for word in wordFrequency.keys(): 
        wordFrequency[word] = (wordFrequency[word]/maxWordFrequency)
    return normalizedWordFrequency

def setPhrasesScore(tokenizedPhrases, normalizedWordFrequency):
    phrasesScore = {}
    for phrase in tokenizedPhrases:
        for word in word_tokenize(phrase.lower()):
            if word in normalizedWordFrequency.keys():
                if phrase not in phrasesScore.keys():
                    phrasesScore[phrase] = normalizedWordFrequency[word]
                else:
                    phrasesScore[phrase] = phrasesScore[phrase] + normalizedWordFrequency[word]
    return phrasesScore

def getLargestElements(summarizedTextSize, phrasesScore):
    largestElements = nlargest(summarizedTextSize, phrasesScore, key=phrasesScore.get)
    return largestElements
