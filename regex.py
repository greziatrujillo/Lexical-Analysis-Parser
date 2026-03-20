"""
Author: Grezia Trujillo
Date: 24 March 2026
Project: Test if the regular expression is correct.
Purpose of the project: Validate the regular expression which takes in strings with the roots chosen and accepts them into the language.
"""

import re


def parse(userInput):

    """
    establish the regular expression for the language. User will input a word and it will be matched with the regular expression.
    """

    stringRegex = re.compile(r'\w*mater\w*|\w*domin\w*')

    
    return bool(stringRegex.search(userInput))


def accept(match):

    """
    if matched, the word is accepted into the language. 
    print confirming message.
    """

    if match:
        return "The word is part of the language."
    else:
        return "The word is not in the language. Try again."


"""
keep asking for input until the user types "exit". Corresponding message for each result is printed.
"""

while True:
    word = input("Enter a word (or 'exit' to quit): ")
    if word == "exit":
        break
    
    res = parse(word)

    status = accept(res)

    print(status)