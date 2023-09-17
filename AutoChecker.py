import re


def replace_spam_words(text, spam_words):
    for word in spam_words:
        pattern = re.compile(r'\b' + re.escape(word) + r'\b', flags=re.IGNORECASE)

        result = pattern.sub('***', text)
    return result
