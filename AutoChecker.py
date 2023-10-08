def to_indexed(source_file, output_file):
    counter = 0

    with open(source_file, 'r') as content, open(output_file, 'w') as outcontent:
        lines = content.readlines()

        for line in lines:
            new_line = f'{counter}: {line}'
            outcontent.write(new_line)
            counter += 1
