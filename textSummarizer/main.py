import src.files as files
import src.text as text 
# download('stopwords') - text.py
# download('punkt') - text.py

# INPUT dirtText.txt
# OUTPUT summarizedText.txt

def main():
    try:
        # Read dirt text from file
        fileText = files.readFile('./src/docs/dirtText.txt') 

        # Remove symbols
        textWithoutSymbols = text.removeTextSymbols(fileText)

        # Remove stopwords
        textWithoutStopwords = text.removeStopwords(textWithoutSymbols)

        # Calculate word frequency
        wordFrequency = text.agroupWordFrequency(textWithoutStopwords)

        # Get the maximum word frequency
        maxWordFrequency = text.getMaximumWordFrequencyValue(wordFrequency)

        # Normalize word frequency
        normalizedWordFrequency = text.normalizeWordFrequency(wordFrequency, maxWordFrequency)

        # Tokenize text in phrases
        tokenizedPhrases = text.tokenizePhrases(fileText)

        # Calculate phrases score
        phrasesScore = text.setPhrasesScore(tokenizedPhrases, normalizedWordFrequency)

        # Calculate summarized text size
        summarizedTextSize = text.estimateSummarizedTextSize(fileText) 

        # Get the largest element
        largestPhrasesScore = text.getLargestElements(summarizedTextSize, phrasesScore)

        # Join the largest phrases score
        summarizedText = " ".join(largestPhrasesScore)

        # Write summarized text to file
        files.writeFile('./src/docs/summarizedText.txt', summarizedText)
    except Exception as err: 
        print(err)

main()