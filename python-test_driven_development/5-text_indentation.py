#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    ponctuation = [".", "?", ":"]

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
