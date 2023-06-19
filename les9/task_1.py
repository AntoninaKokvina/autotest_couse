# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

from pathlib import Path

try:
    # открываем файл и записываем его содержимое в строку:
    f = open('test_file/task1_data.txt', encoding='utf-8')
    f_str = f.read()
    # открываем и очищаем второй файл
    f2 = open('test_file/task1_answer.txt', mode='w+', encoding='utf-8')
    f2.seek(0)
    f2.close()
    # во второй файл записываем все символы кроме чисел
    f2 = open('test_file/task1_answer.txt', mode='a+', encoding='utf-8')
    for i in f_str:
        if not i.isdigit():
            f2.write(i)
finally:
    f.close()
    f2.close()


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
