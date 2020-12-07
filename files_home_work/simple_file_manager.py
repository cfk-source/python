import glob
# выбрать действие от 1 до 3.
from typing import TextIO

action = int(input('Please choose action:\n '))
if action == 3:                                         # выход из программы при выборе 3
    print('Have a nice day.')
    exit()

elif action == 1:                                       # подсчёт ко-ва слов втексте, ко-ва уникальных слов в тексте
    f_name = str(input('enter file name:\n '))
    with open(f_name, 'r', encoding='UTF8') as r_file:
        file_content = r_file.read().lower()            # содержимое файла в нижнем регистре
        words = file_content.split(' ')                 # слова разделённые пробелом
        words_count = len(words)                        # ко-во слов в файле
        unique_words = set(words)                       # уникальные слова
        unique_words_count = len(unique_words)          # ко-во уникальных слов
        print(unique_words)
        print(unique_words_count)

        with open('text_Copy.txt', 'w+', encoding='UTF8') as n_file:

            n_file.write(str(list(unique_words)))
            n_file.write('\n' + str(unique_words_count))
        n_file.close()
    r_file.close()
    print('Results in file: ' + n_file.name)
    exit()

elif action == 2:
    path = 'files_home_work'
    files = glob.glob(path)
    for file in files:
        f = open(file, 'r', encoding='UTF8')
        f.readlines()
        f.content = f.read().lower()
        f.words = f.content.split(' ')

        print(f.words)


        f.close()
    print()



