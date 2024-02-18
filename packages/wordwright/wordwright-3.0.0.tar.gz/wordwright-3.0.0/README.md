# Wordwright

A package for text processing

![](docs/logo.jpg)

[![ci-cd](https://github.com/UBC-MDS/wordwright/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/wordwright/actions/workflows/ci-cd.yml)
[![codecov](https://codecov.io/gh/UBC-MDS/wordwright/graph/badge.svg?token=0cuB4J7YN9)](https://codecov.io/gh/UBC-MDS/wordwright)
[![Documentation Status](https://readthedocs.org/projects/text-processing-util-mds24/badge/?version=latest)](https://text-processing-util-mds24.readthedocs.io/en/latest/?badge=latest)
[![PyPI - Version](https://img.shields.io/pypi/v/text-processing-util-mds24)](https://pypi.org/project/text-processing-util-mds24/)
[![Python 3.9.0](https://img.shields.io/badge/python-3.9.0-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![version](https://img.shields.io/github/v/release/UBC-MDS/wordwright)](https://github.com/UBC-MDS/wordwright/releases)
[![release](https://img.shields.io/github/release-date/UBC-MDS/wordwright)](https://github.com/UBC-MDS/wordwright/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Project Status: Active -- The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)


In today's world, text is omnipresent and serves as more than just a form of communication. From the briefest tweets to in-depth blog posts, from academic papers to business emails, our digital world is full of textual content. The ability to read, analyze, and derive meaning from the written content is crucial. This is where our text analysis package `wordwright` enters the picture.

## Package Summary

This Python package [`wordwright`](https://wordwright.readthedocs.io/en/latest/index.html) focuses on text analysis and processing. It offers a range of functions, from basic text cleaning to more complex analyses such as language detection, word and sentence counting, word frequency summarizing, and keyword searching. This functionality is particularly useful in fields like data analysis, natural language processing, and anywhere textual data needs to be understood or transformed. Functions are designed to be self-explanatory, which is especially beneficial for those new to programming or text processing. Quickstart guide could be found [here](https://wordwright.readthedocs.io/en/latest/example.html).

## Contributors

Yi Han ([\@yhan178](https://github.com/yhan178)), Yingzi Jin ([\@jinyz8888](https://github.com/jinyz8888)), Yi Yan ([\@carrieyanyi](https://github.com/carrieyanyi)), Hongyang Zhang ([\@alexzhang0825](https://github.com/alexzhang0825))

## Installation

### Install from PyPI
Run this command to install the package

``` bash
$ pip install wordwright
```
### Install from GitHub
If the installation is unsuccessful, please consider the following process. Before proceeding with the installation, ensure you have Miniconda/Anaconda installed on your system. These tools provide support for creating and managing Conda environments.

#### Step 1: Clone the Repository

Start by cloning the repository to your local machine. Open your terminal and run the following command:

``` bash
$ git clone git@github.com:UBC-MDS/wordwright.git
```

Navigate to the directory of the cloned repository.

#### Step 2: Create and Activate the Conda Environment

Create a new Conda environment using the `environment.yaml` file provided in this repository. This file contains all the necessary dependencies, including both Python and Poetry versions.

To create the environment, open your terminal and navigate to the directory where the `environment.yaml` file is located. Then, run the following command:

``` bash
$ conda env create -f environment.yaml

$ conda activate wordwright
```

#### Step 3: Install the Package Using Poetry

With the Conda environment activated, you can now use Poetry to install the package. Run the following command to install the package using Poetry:

``` bash
$ poetry install
```

This command reads the pyproject.toml file in your project (if present) and installs the dependencies listed there.

### Running the tests

Navigate to the project root directory and use the following command in terminal to test the functions defined in the projects. Tests are stored in [here](#0).

``` bash
$ pytest tests/*
```

### Troubleshooting

**Environment Creation Issues**: If you encounter problems while creating the Conda environment, ensure that the environment.yaml file is in the correct directory and that you have the correct version of Conda installed.

## Example Usage

To use the `wordwright` package, you can import and call its functions in your Python environment. Here is an example:

``` bash

>>> from wordwright.preprocessing import clean_text
>>> from wordwright.word_frequency import frequent_words
>>> from wordwright.count_keywords import count_keywords

>>> clean_text("It's a sunny day. ,Let's GO!")
"it's a sunny day let's go"

>>> text = "The quick brown fox jumps over the lazy dog. The fox was very quick."
>>> stopwords = ["the", "over", "was", "very"]
>>> frequent_words(text, stopwords)
Counter({'quick': 2, 'fox': 2, 'brown': 1, 'jumps': 1, 'lazy': 1, 'dog': 1})

>>> count_keywords("I like cheese.", ["cheese"])
{'cheese': 1}
```

## Functions

-   `load_text(file_path)`: Loads and returns the content of a text file. Required input is `file_path`, which specifies the path to the file.

-   `clean_text(text)`: Cleans a text string by removing punctuation, converting to lowercase, and removing common stopwords. Required input is `text`, which is the string to be cleaned.

-   `count_keywords(text, keywords)`: Counts the occurrences of specified keywords in the text. Required inputs are `text` and `keywords`. After giving a list of keywords, this function return the occurrence of each selected word.

-   `count_sentences(text, punctuation)`: Count the number of sentences in the text. The number of sentences is counted based on specified delimiters. Required inputs are `text` and `punctuation`.

-   `language_detection(text)`: Detects if the text is in English or not. Required input is `text`, which is the text to be checked for language.

-   `frequent_words(text, number, stopwards)`: Analyzes a given text to find and return the most frequent words, excluding specified stopwords. Required inputs are `text`, `number`, and `stopwards`, which are the cleaned text to be analyzed, the number of most frequent words to return, and a list of words to be excluded from the analysis.

## `wordwright` Use in Python Ecosystem

While there are other packages that offer similar functions, such as [Natural Language Toolkit](https://www.nltk.org/) (Loper & Bird, 2002) and [TextBlob](https://textblob.readthedocs.io/en/dev/) (Loria, 2018). `wordwright` distinguishes itself by its simplicity and focus on the most essential text processing features. It is designed for ease of use, making it an excellent choice for those who have basic programming knowledge.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`wordwright` was created by Yi Han, Yingzi Jin, Yi Yan, Hongyang Zhang. It is licensed under the terms of the MIT license.

## Credits

`wordwright` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

## Reference

Loper, E., & Bird, S. (2002). Nltk: The natural language toolkit. arXiv preprint cs/0205028.

Loria, S. (2018). textblob Documentation. Release 0.15, 2(8), 269.
