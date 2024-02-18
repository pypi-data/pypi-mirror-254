def print_prog():
    print(
        """
import spacy 
nlp=spacy.load("en_core_web_sm")

from textblob import TextBlob

blob=TextBlob("i am sad")
sent=blob.sentiment

if sent.polarity>0:
    print("positive")

elif sent.polarity<0:
    print("negative")

else:
    print("neutral")

"""
    )
