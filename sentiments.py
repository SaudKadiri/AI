# Using NLTK VADER to get sentiment score from text.
# Best suited for language used in social media, like short sentences with some slang and abbreviations. 
# Less accurate for long, structured text.

from nltk.sentiment import SentimentIntensityAnalyzer

def calculate_sentiment(text):
    # create an object of the SentimentIntensityAnalyzer class.
    sia = SentimentIntensityAnalyzer()

    # dictionary which contains positive, negative, neutral, and compound scores of the text
    score = sia.polarity_scores(text)
    return score

text = 'Difficult road often lead to beautiful destinations.'

print(calculate_sentiment(text))
# {'neg': 0.219, 'neu': 0.439, 'pos': 0.342, 'compound': 0.34}
