from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy

def SimilarityCV(text1, text2):
    """
    To calculate cosine-similarity score using CountVectorizer between two strings of text

    Parameters:
    text1 (str): First string containing the text be compared. eg. Job Description
    text2 (str): Second string containing the text be compared. eg. Resume text

    Returns:
    float: Cosine-Similarity score which shows how similar the two strings are.

    Example:
    >>> SimilarityCV("I am studying Data Science at UBC", "There are many good sources to study Data Science online")
    21.8
    """
    if not text1 or not text2:
        raise ValueError("Both input strings must not be empty.")
    
    if not isinstance(text1, str) or not isinstance(text2, str):
        raise ValueError("Both inputs must be strings.")

    cv = CountVectorizer()
    text = [text1, text2]
    count_matrix = cv.fit_transform(text)

    similarityScore = round(cosine_similarity(count_matrix)[0][1] * 100, 2)

    return similarityScore

#print(SimilarityCV("I am studying Data Science at UBC", "There are many good sources to study Data Science online"))

def SimilaritySpacy(text1, text2):
    """
    To calculate cosine-similarity score using Spacy embeddings between two strings of text

    Parameters:
    text1 (str): First string containing the text be compared. eg. Job Description
    text2 (str): Second string containing the text be compared. eg. Resume text
    model: Spacy model object eg. en_core_web_md, en_core_web_lg

    Returns:
    float: Cosine-Similarity score which shows how semantically similar the two strings are.

    Example:
    >>> SimilaritySpacy("I am studying Data Science at UBC", "There are many good sources to study Data Science online")
    45.3
    """
    if not text1 or not text2:
        raise ValueError("Both input strings must not be empty.")
        
    if not isinstance(text1, str) or not isinstance(text2, str):
        raise ValueError("Both inputs must be strings.")

    # Specify the model name you want to check or download
    model_name = "en_core_web_md"

    # Check if the spaCy model is installed
    try:
        nlp = spacy.load(model_name)
        print(f"{model_name} is already installed.")
    except OSError:
        print(f"{model_name} is not installed. Downloading...")
        # Download the spaCy model
        spacy.cli.download(model_name)
        print(f"{model_name} has been downloaded and installed.")
    # Load the NLP model
    nlp = spacy.load(model_name)

    text1 = nlp(text1)
    text2 = nlp(text2)

    # Calculating the similarity between the two texts
    similarity_score = text1.similarity(text2)

    return similarity_score

#print(SimilaritySpacy("I am studying Data Science at UBC", "There are many good sources to study Data Science online"))
