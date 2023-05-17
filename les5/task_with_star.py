# Напишите функцию to_roman, которая преобразуют арабское число (val) в римское (roman_str).
#
# Современные римские цифры записываются, выражая каждую цифру отдельно,
# начиная с самой левой цифры и пропуская цифру со значением нуля.
# Римскими цифрами 1990 отображается: 1000=М, 900=СМ, 90=ХС; в результате MCMXC.
# 2023 записывается как 2000=MM, 20=XX, 3=III; или MMXXIII.
# В 1666 используется каждый римский символ в порядке убывания: MDCLXVI.
#
# Например (Ввод --> Вывод) :
# 2008 --> MMVIII


def to_roman(val):
    """
    преобразуют арабское число в римское
    :param val: исходное арабское число
    :return: полученное римское число
    """

    # соответствие арабских чисел и римских
    # {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
    # 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

    # находим максимальное значение, которое можно заменить на римское число,
    # заменяем и вызываем to_roman для числа уменьшенного на уже замененное
    roman_str = ''
    if val >= 1000:
        roman_str = 'M' + to_roman(val - 1000)
    elif val >= 900:
        roman_str = 'CM' + to_roman(val - 900)
    elif val >= 500:
        roman_str = 'D' + to_roman(val - 500)
    elif val >= 400:
        roman_str = 'CD' + to_roman(val - 400)
    elif val >= 100:
        roman_str = 'C' + to_roman(val - 100)
    elif val >= 90:
        roman_str = 'XC' + to_roman(val - 90)
    elif val >= 50:
        roman_str = 'L' + to_roman(val - 50)
    elif val >= 40:
        roman_str = 'XL' + to_roman(val - 40)
    elif val >= 10:
        roman_str = 'X' + to_roman(val - 10)
    elif val >= 9:
        roman_str = 'IX' + to_roman(val - 9)
    elif val >= 5:
        roman_str = 'V' + to_roman(val - 5)
    elif val >= 4:
        roman_str = 'IV' + to_roman(val - 4)
    elif val >= 1:
        roman_str = 'I' + to_roman(val - 1)

    return roman_str

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [1133, 2224, 1938, 1817, 2505, 391, 3743, 1634, 699, 1666, 1494, 1444]

test_data = [
    "MCXXXIII", "MMCCXXIV", "MCMXXXVIII", "MDCCCXVII", "MMDV", "CCCXCI", 'MMMDCCXLIII', 'MDCXXXIV', 'DCXCIX', 'MDCLXVI',
    'MCDXCIV', 'MCDXLIV']


for i, d in enumerate(data):
    assert to_roman(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
