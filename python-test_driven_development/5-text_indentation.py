#!/usr/bin/python3
"""Module to print text with indentation"""


def text_indentation(text):
    """Function to print text"""
    if type(text) != str:
        raise TypeError("text must be a string")
    text2 = text.strip()
    new_text = text2[0]
    for i in text2[1:]:
        if i in '.?:':
            new_text += i + "\n\n"
        else:
            if i == " " and new_text[-1] == "\n":
                continue
            new_text += i
    print(new_text, end="")
