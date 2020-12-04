
# выбрать действие от 1 до 3.
action = int(input('Please choose action:\n '))
if action == 3:                                         # выход из программы при выборе 3
    print('Have a nice day.')
    exit()

elif action == 1:                                       # подсчёт ко-ва слов втексте, ко-ва уникальных слов в тексте
    f_name = str(input('enter file name:\n '))
    with open(f_name, 'rt', encoding='UTF8') as file:
        file_content = file.read().lower()              # содержимое файла
        words_count = file_content.split(' ')           # ко-во слов в файле
#        print(len(words_count))




elif action == 2:
    print()



