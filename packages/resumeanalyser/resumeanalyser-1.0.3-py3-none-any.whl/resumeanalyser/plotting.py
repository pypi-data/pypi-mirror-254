from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

def plot_wordcloud(text):
    """Plot the wordcloud of the input resume text.
    
    Parameters
    ----------
    text : str
        Text to plot wordcloud on.

    Returns
    -------
    matplotlib.image.AxesImage
        wordcloud plot of important words.

    Examples
    --------
    >>> from resumeanalyser.plotting import plot_wordcloud
    >>> txt = 'a b c d e f g a a a a a'
    >>> plot_wordcloud(txt)
    """
    if not text:
        raise ValueError("Input text should not be None.")
    
    if not isinstance(text, str):
        raise TypeError("Input text should be String.")
    
    wc = WordCloud(width = 800, height = 500, random_state=123).generate(text)
    fig = plt.imshow(wc)
    plt.axis("off")
    return fig

def plot_topwords(text, n=10):
    """Plot a bar chart of word counts in the input resume text.
    
    Parameters
    ----------
    text : str
        Text to plot top frequency barchart on.
    n : int, optional
        Plot the top n words. By default, 10.

    Returns
    -------
    matplotlib.container.BarContainer
        Bar chart of word counts.

    Examples
    --------
    >>> from resumeanalyser.plotting import plot_topword
    >>> txt = 'a b c d e f g a a a a a'
    >>> plot_topwords(txt,n=5)
    """
    if not text:
        raise ValueError("Input text should not be None.")
    
    if not isinstance(text, str):
        raise TypeError("Input text should be String.")
    
    if not isinstance(n, int) or n < 2:
        raise ValueError("Input n should be an integer bigger than 1")
    
    word_counts = Counter(text.split())
    top_n_words = word_counts.most_common(n)
    word, count = zip(*top_n_words)
    fig = plt.bar(range(n), count)
    plt.xticks(range(n), labels=word, rotation=45)
    plt.xlabel("Word")
    plt.ylabel("Count")
    return fig

def plot_suite(text, n=10):
    """Plot the comprehensive plot suite for the input resume text.
    
    Parameters
    ----------
    text : str
        Text to plot suite on.
    n : int, optional
        Plot the top n words. By default, 10.

    Returns
    -------
    matplotlib.figure.Figure
        A comprehensive visualization of the resume text keywords.

    Examples
    --------
    >>> from resumeanalyser.plotting import plot_suite
    >>> txt = 'a b c d e f g a a a a a'
    >>> plot_suite(txt,n=10)
    """
    if not text:
        raise ValueError("Input text should not be None.")
    
    if not isinstance(text, str):
        raise TypeError("Input text should be String.")

    if not isinstance(n, int) or n < 2:
        raise ValueError("Input n should be an integer bigger than 1")
    
    # Create a new figure with two subplots side by side
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    # plot the wordcloud plot
    wc = WordCloud(width = 800, height = 500, random_state=123).generate(text) # default built-in stopwords are used, change it if needed
    axes[0].imshow(wc)  # Adjust the colormap as needed
    axes[0].set_title('WordCloud')
    axes[0].axis("off")

    # plot the topword barchart
    word_counts = Counter(text.split())
    top_n_words = word_counts.most_common(10)
    word, count = zip(*top_n_words)
    axes[1].bar(range(10), count)
    axes[1].set_xticks(range(10), labels=word, rotation=45)
    axes[1].set_xlabel("Word")
    axes[1].set_ylabel("Count")
    axes[1].set_title('Top Frequency Words')
    
    plt.tight_layout()

    return fig