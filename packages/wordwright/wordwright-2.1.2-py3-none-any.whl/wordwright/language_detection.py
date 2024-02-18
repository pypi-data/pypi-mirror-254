from langdetect import detect, LangDetectException

def language_detection(text):
    """
    Detect if the text is in English or not.
    
    Parameters
    ----------
    text : str
        The text to be checked.
    
    Returns
    -------
    str: "English" if the text is detected to be in English, "Not English" otherwise,
         or "Language detection error" in case of an error.
    
    Examples
    --------
    >>> language_detection("This is a sample English text.")
    'English'
    >>> language_detection("Este es un texto en español.")
    'Not English'
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    if not text.strip():  # Check if the string is empty or whitespace
        raise ValueError("Input string is empty or whitespace.")
    try:
        return "English" if detect(text) == 'en' else "Not English"
    except LangDetectException:
        return "Language detection error"

