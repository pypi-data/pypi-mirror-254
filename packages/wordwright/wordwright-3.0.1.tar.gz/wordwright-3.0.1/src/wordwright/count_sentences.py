def count_sentences(text, punctuation):
    """
    Count the number of sentences in the text, which is based on specified delimiters.
   
    Parameters
    ----------
    text (str)
        The text to be analyzed.
    punctuation (list)
        List of punctuation marks
    
    Returns
    ----------
    int
        An int describing the number of sentences in text.
    
    Examples
    --------
    >>> from wordwright.count_sentences import count_sentences
    >>> count_sentences("I like cheese! I like cat. I hate fruit", ["!", "."])
    2
    
    """
    sentence_count = 0
    
    if type(punctuation) != list:
        raise TypeError("Please enter a list of punctuation")
        
    if text:
        for i in range(len(text)):
            for punc in punctuation:
                if text[i] == punc:
                    sentence_count += 1
    print(f"There are {sentence_count} sentence(s), which is splited by {punctuation}.")
    return sentence_count        
