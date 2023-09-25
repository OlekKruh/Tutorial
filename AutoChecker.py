def get_cats_info(path):
    list_of_cats = []
    with open(path, 'r') as content:
        while True:
            data = content.readline().strip()
            if not data:
                break
            line = data.split(',')
            client = {
                'id': line[0],
                'name': line[1],
                'age': line[2]
            }
            list_of_cats.append(client)
    return list_of_cats

print(get_cats_info('list.txt'))
