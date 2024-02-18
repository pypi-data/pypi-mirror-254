from string import punctuation
import os
import re

def load_text(file_path):
    """ Load and return the content of a text file. 

    This function reads a text file from the specified file path, but 
    does not modify the content of the file.

    Parameters
    ----------    
    file_path: str 
        The path to the text file to be read.
    
    Returns
    ---------- 
    str
        The content of the file as a string.
    
    Raises
    ------
    FileNotFoundError
        If the file specified by file_path does not exist.
    OSError
        If there is an error opening or reading the file.

    Examples
    --------
    >>> load_text("text.txt")
    """
    if not isinstance(file_path, str):
        raise TypeError("The input must be a string.")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    
    with open(file_path, "r") as file:
        txt = file.read()
    return txt


def clean_text(text):
    """
    Clean a text string by removing punctuation (except apostrophes 
    that directly follow a character), converting to lowercase, and 
    removing excessive spaces and tabs. Standalone apostrophes or 
    those not directly following a character are removed.

    Parameters
    ----------
    text : str
        The text to be cleaned.

    Returns
    ---------- 
    str
        The cleaned text.
    
    Examples
    --------
    >>> clean_text("It's a sunny day. ,Let's GO!")
    "it's a sunny day let's go"
    """
    if not isinstance(text, str):
        raise TypeError("The input must be a string.")

    # Remove standalone apostrophes and those not following a character
    txt = re.sub(r"(?<!\w)'|'(?!\w)", '', text)

    # Remove punctuation except apostrophes and convert to lowercase
    modified_punctuation = punctuation.replace("'", "")
    txt = txt.lower()
    for p in modified_punctuation:
        txt = txt.replace(p, "")

    # Remove excessive whitespace
    txt = ' '.join(txt.split())
    
    return txt