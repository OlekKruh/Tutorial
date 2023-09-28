def save_applicant_data(source, output):
    with open(output, 'w') as data_list:
        for dictionary in source:
            information = list(dictionary.values())
            form_lins = ','.join(map(str, information))
            data_list.write(form_lins + '\n')



student_list = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

save_applicant_data(student_list, 'list.txt')
