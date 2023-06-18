# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


def generate_random_name():
    letters = string.ascii_lowercase
    # name = ' '.join(''.join(random.choice(letters) for i in range(random.randint(1,15))) for j in range(2))
    while True:
        name = ' '.join(''.join(random.choices(letters, k=random.randint(1,15))) for i in range(2))
        yield name

gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
