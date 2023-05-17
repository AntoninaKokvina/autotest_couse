# Игра "Эрудит"
# Нужно написать программу scrabble, которая помогает считать кол-во очков (points), полученное за слово (word)
# По одному очку вы получите за буквы а, в, е=ё, и, н, о, р, с, т.
# Два очка стоит д, к, л, м, п, у.
# Три балла получают за б, г, ь, а также я.
# Четыре балла стоят буквы й, ы.
# 5 очков засчитывается за ж, з, х, ц, ч.
# 6 и 7 очков не предусмотрено.
# Восемь можно получить за букву ф, ш, э, ю.
# 10 баллов стоит буква щ,
# а 15 - ъ
# Например (Ввод --> Вывод):
# курс --> 6 (к=2, у=2, р=1, с=1)


def scrabble(word):
    """
    функция считает количество очков, полученное за слово в игре Эрудит
    :param word: слово, для которого требуется подсчитать очки
    :return: количество отков за исходное слово
    """

    # словарь с количеством очков для букв
    points_dict = {'а': 1, 'б': 3, 'в': 1, 'г': 3, 'д': 2, 'е': 1, 'ё': 1, 'ж': 5, 'з': 5, 'и': 1, 'й': 4, 'к': 2,
                   'л': 2, 'м': 2, 'н': 1, 'о': 1, 'п': 2, 'р': 1, 'с': 1, 'т': 1, 'у': 2, 'ф': 8, 'х': 5, 'ц': 5,
                   'ч': 5, 'ш': 8, 'щ': 10, 'ъ': 15, 'ы': 4, 'ь': 3, 'э': 8, 'ю': 8, 'я': 3,}

    points = 0 # общее кол-во очков для слова    
    # для каждой буквы ищем кол-во очков в словаре и добавляем к общему кол-ву очков
    for i in range(len(word)):
        points += points_dict[word[i]]

    return points

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = ["курс", 'авеинорстё', 'дклмпеу', 'бгья', 'йы', 'жзхцч', 'фшэю', 'щъ', "карабасбарабас", "околоводопроводного",
        "еженедельное", 'эхоэнцефалограф', 'человеконенавистничество', 'делопроизводительница']

test_data = [6, 10, 13, 12, 8, 25, 32, 25, 21, 26, 20, 54, 34, 36]

for i, d in enumerate(data):
    assert scrabble(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
