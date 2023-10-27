import re
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer


def get_unique_words(texts):
    # Join a list of strings to one long string
    words = " ".join(texts)
    # Remove certain characters and make everything lower case
    pattern = '[' + "().,;:!?'’`´“”" + '"' + ']'
    words = re.sub(pattern, '', words)
    words = words.lower().split()
    # Lemmatize each word
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(w) for w in words]
    # Return list of unique words
    unique_words = list(set(words))
    return unique_words
