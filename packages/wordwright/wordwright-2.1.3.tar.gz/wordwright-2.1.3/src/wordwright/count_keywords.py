from wordwright.preprocessing import clean_text
from collections import Counter

def count_keywords(text, keywords):
    """Count the occurrences of each keyword in the given text. White-space or
    punctuations-only strings are treated as empty. Characters entangled in punctuations
    would be together treated as a single word (ex: w?o!'r_d --> word).
    
    Parameters
    ----------
    text : str
        The text in which to count keywords.
    keywords : list[str]
        A list of string of keywords to count in the text.

    Returns
    -------
    dict
        A dictionary where keys are keywords and values are the counts of those keywords in the text.

    Examples
    --------
    >>> from wordwright.count_keywords import count_keywords
    >>> test = count_keywords("I like cheese.", ["cheese"])
    {'cheese': 1}
    """
    if not isinstance(text, str):
        raise TypeError('Input text must be a string!')

    if not isinstance(keywords, list):
        raise TypeError('Keywords must be provided in a list!')

    for keyword in keywords:
        if not isinstance(keyword, str):
            raise TypeError('All keywords must be presented in a string format!')

    clean = clean_text(text)
    words = clean.split()
    word_counts = Counter(words)

    keyword_counts = {clean_text(keyword):(word_counts[clean_text(keyword)] 
                                           if clean_text(keyword) in word_counts 
                                           else 0) for keyword in keywords}
    
    return keyword_counts