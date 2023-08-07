def real_len(text):
    special_characters = ['\n', '\f', '\r', '\t', '\v']

    for char in special_characters:
        text = text.replace(char, '')

    return len(text)


text = 'Alex\nKdfe23\t\f\v.\r'
print(real_len(text))