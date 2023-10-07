import os
import re
import sys
import shutil


def directory_creation(path, list):
    created_dirs_path_list = []
    for name in list[1:]:
        new_directory = os.path.join(path, name)
        if not os.path.exists(new_directory):
            os.mkdir(new_directory)
            print(f'Directory {name} created\n'
                  f'{"+" * 32}')
            created_dirs_path_list.append(new_directory)
        else:
            print(f'Directory {name} already exists')
    return created_dirs_path_list


def scan_and_sort(content, extension):
    print(f'Scanning...\n'
          f'{"=" * 100}')

    dict_of_lists = {
        'folders': [],
        'images': [],
        'videos': [],
        'documents': [],
        'musics': [],
        'archives': [],
        'unknowns': [],
    }

    list_of_dirs_to_create = []

    for element in content:
        if os.path.isdir(element):
            dict_of_lists['folders'].append(element)
        elif element.endswith(extension['image']):
            dict_of_lists['images'].append(element)
        elif element.endswith(extension['vidio']):
            dict_of_lists['videos'].append(element)
        elif element.endswith(extension['documents']):
            dict_of_lists['documents'].append(element)
        elif element.endswith(extension['music']):
            dict_of_lists['musics'].append(element)
        elif element.endswith(extension['archives']):
            dict_of_lists['archives'].append(element)
        else:
            dict_of_lists['unknowns'].append(element)

    for key1, value1 in dict_of_lists.items():
        print(f'{key1} files found: {len(value1)}\nList of {key1} is:{value1}\n'
              f'{"=" * 100}')

    for key2, value2 in dict_of_lists.items():
        if value2:
            list_of_dirs_to_create.append(key2)

    return list_of_dirs_to_create, dict_of_lists


def normalize(characters, input_list, symbols):
    result_list = []
    for element in input_list:
        filename, file_extension = os.path.splitext(element)

        for slavik, latina in zip(symbols['slavik'], symbols['latina']):
            filename = re.sub(re.escape(slavik), latina, filename, flags=re.IGNORECASE)

        for chars in characters:
            filename = filename.replace(chars, '_')

        normalized_element = filename + file_extension
        try:
            os.rename(element, normalized_element)
            result_list.append(normalized_element)
            continue
        except PermissionError:
            print(f'{"*" * 32}\n'
                  f'Something is wrong. Close all directories and try again.\n'
                  f'{"*" * 32}\n')
    return result_list


def relocate(current_directory, dict_of_lists):
    for key, file_list in dict_of_lists.items():
        if key == 'folders':
            continue
        if len(file_list) == 0:
            continue
        for file_name in file_list:
            source_file = os.path.join(current_directory, file_name)
            target_directory = os.path.join(current_directory, key)
            target_file = os.path.join(target_directory, file_name)

            try:
                shutil.move(source_file, target_file)
                print((f'Moved {file_name} to {target_directory}'))
            except Exception as j:
                print(f'Failed to move {file_name}: {str(j)}')


def enter_subdirectories_and_make_magic(current_directory):
    try:
        os.chdir(current_directory)
        print(f'{"->" * 32}\n'
              f'Enter the directory: {current_directory}\n'
              f'{"->" * 32}\n')
    except FileNotFoundError:
        print(f'Directory not found: {current_directory}')
        return
    except Exception as error:
        print(f'An error occurred: {error}')
        return

    content = os.listdir()
    normalized_content = normalize(characters, content, symbols)
    list_of_dirs_to_create, dict_of_lists = scan_and_sort(normalized_content, extension)

    if dict_of_lists['folders']:
        for folder in dict_of_lists['folders']:
            subdir_path = os.path.join(current_directory, folder)
            enter_subdirectories_and_make_magic(subdir_path)

    if not list_of_dirs_to_create:
        print(f'\n{"<-" * 32}\n'
              f'{current_directory} Is empty.\n'
              f'Moving up and deleting empty directory: {current_directory}\n'
              f'{"<-" * 32}\n')
        os.chdir('..')
        os.rmdir(current_directory)

    else:
        created_dirs_path_list = directory_creation(current_directory, list_of_dirs_to_create)
        relocate(current_directory, dict_of_lists)


characters = ('~', '!', '#', '$', '%', '&', "'", '(', ')', '-', '{',
              '}', '.', '_', '^', '@', "'", ',', ';', '=', '[', ']',
              ' ',)

symbols = {
    'slavik': ('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
               'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
               'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
               'э', 'ю', 'я', 'є', 'і', 'ї', 'ґ', "ą", "ć", "ę",
               "ł", "ń", "ó", "ś", "ź", "ż"),
    'latina': ('a', 'b', 'v', 'g', 'd', 'e', 'e', 'j', 'z', 'i',
               'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't',
               'u', 'f', 'h', 'ts', 'ch', 'sh', 'sch', '', 'y', '',
               'e', 'yu', 'ya', 'je', 'i', 'ji', 'g', "a", "c", "e",
               "l", "n", "o", "s", "z", "z")
}

extension = {
    'image': ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff',
              '.tif', '.webp', '.svg', '.heif', '.heic', '.raw',),
    'vidio': ('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm',
              '.3gp', '.mpeg', '.mpg', '.ogg', '.h264', '.h265', '.hevc',),
    'documents': ('.doc', '.docx', '.pdf', '.odt', '.rtf', '.txt',
                  '.html', '.tex', '.xls', '.xlsx', '.ppt', '.pptx',),
    'music': ('.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma',
              '.m4a', '.aiff', '.ape', '.midi', '.mp4', '.amr'),
    'archives': ('.zip', '.rar', '.7z', '.tar', '.gz',),
    'unknown': (),
}

# if len(sys.argv) != 2:
#     print('Please pass only one argument - the path to the directory.')
#     sys.exit(1)
# directory_path = sys.argv[1]
# if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
#     print('Directory does not exist.')
#     sys.exit(1)

directory_path = r'C:\Users\Alex\Downloads\TestDir'
enter_subdirectories_and_make_magic(directory_path)
