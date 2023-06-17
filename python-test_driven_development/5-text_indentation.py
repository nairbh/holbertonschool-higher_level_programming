#!/usr/bin/python3
""" print a text """


def text_indentation(text):
    """ print a text whitout punctionation """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    punctuation = [".", "?", ":"]

    new_text = ""
    line = ""
    for i in text:
        line += i
        if i in punctuation:
            new_text += line.strip() + "\n\n"
            line = ""

    if line:
        new_text += line.strip()

    print(new_text)
