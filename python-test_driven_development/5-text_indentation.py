#!/usr/bin/python3
"""Module to print text with indentation"""

def text_indentation(text):
    """Function to print text"""
    if type(text) != str:
        raise TypeError("text must be a string")
    text2 = text.strip()
    new_text = text2[0]
    ignore_space = False
    for i in text2[1:]:
        if i in '.?:':
            new_text += i + "\n\n"
            ignore_space = True
        else:
            if i == " " and ignore_space is True:
                ignore_space = False
                continue
            new_text += i
            ignore_space = False
    print(new_text, end="")
