articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    global articles_dict
    result = []

    for dict in articles_dict:
        for value in dict.values():
            if not isinstance(value, int):
                if not letter_case:
                    value = str(value).lower()
                    key = str(key).lower()
                if key in value:
                    result.append(dict)

    return result

