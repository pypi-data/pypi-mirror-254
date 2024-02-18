import nltk
import re
import os


# Download NLTK WordNet and stopwords datasets
try:
    nltk.download("wordnet", quiet=True)
    nltk.download("stopwords", quiet=True)
    nltk.download("punkt", quiet=True)

    from nltk.corpus import wordnet
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
    from nltk.tokenize import word_tokenize

except Exception as e:
    print(f"An error occurred: {e}")


def remove_punctuation(text):
    """
    Remove punctuation and special characters from the input text.

    Parameters:
    text (str): A string containing the text to be processed.

    Returns:
    str: The text with all punctuation and special characters removed.

    Example:
    >>> remove_punctuation("Hello, world!")
    'Hello world'
    """
    cleaned_text = re.sub('[^A-Za-z]', ' ', text)
    cleaned_text = re.sub(' +', ' ', cleaned_text)

    return cleaned_text


def tokenize(text):
    """
    Tokenize the input text into individual words.

    Parameters:
    text (str): A string containing the text to be tokenized.

    Returns:
    list: A list of words (tokens) extracted from the input text.

    Example:
    >>> tokenize("Hello, world!")
    ['Hello', ',', 'world', '!']
    """
    return word_tokenize(text)


def to_lower(tokens):
    """
    Convert all tokens in the input list to lowercase.

    Parameters:
    tokens (list): A list of tokens (words).

    Returns:
    list: A list of tokens in lowercase.

    Example:
    >>> to_lower(['Hello', 'WORLD'])
    ['hello', 'world']
    """
    return [token.lower() for token in tokens]


def remove_stop_words(tokens):
    """
    Remove stop words from the list of tokens.

    Parameters:
    tokens (list): A list of tokens (words).

    Returns:
    list: A list of tokens with stop words removed.

    Example:
    >>> remove_stop_words(['this', 'is', 'a', 'sample'])
    ['sample']
    """
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token not in stop_words]


def lemmatize(tokens):
    """
    Apply lemmatization to each token in the list.

    Parameters:
    tokens (list): A list of tokens (words).

    Returns:
    list: A list of lemmatized tokens.

    Example:
    >>> lemmatize(['running', 'jumps'])
    ['running', 'jump']
    """
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]


def clean_text(text):
    """
    Clean text by applying a series of processing steps: tokenization, converting to lower case,
    removing stop words, and applying lemmatization.

    Parameters:
    text (str): A string containing the text to be cleaned.

    Returns:
    str: The cleaned text as a single string.

    Example:
    >>> clean_text("This is a sample sentence, showing off the stop words filtration.")
    'sample sentence showing stop word filtration'
    """

    text = remove_punctuation(text)
    tokens = tokenize(text)
    tokens = to_lower(tokens)
    tokens = remove_stop_words(tokens)
    tokens = lemmatize(tokens)
    return ' '.join(tokens)
