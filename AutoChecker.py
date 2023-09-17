import re


def find_word(text, word):
    res_dict = {}
    pattern = re.compile(word, flags=re.IGNORECASE)
    result = re.findall(pattern, text)
    return result


print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))
