import re


def find_all_emails(text):
    pattern = re.compile(r'\b[A-Za-z\d_.]{2,}@[A-Za-z]+\.[A-Za-z]{2,}\b')
    match = pattern.findall(text)

    mail_list = []

    for i in match:
        mail_list.append(i)
    print(mail_list)
    return mail_list
