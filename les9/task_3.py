# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

from pathlib import Path

buy_list = open('test_file/task_3.txt', encoding='utf-8')
buy_sum = []
i = 0
buy_sum.append(0)
# в список buy_sum записываем суммы покупок:
while 1:
    k = buy_list.readline()[:-1]
    if k.isdigit():
        buy_sum[i] += int(k)
    else:
        if buy_sum[i] != 0:
            i += 1
            buy_sum.append(0)
        else:
            break
# сортируем список с суммами и считаем сумму трех самых дорогих:
buy_sum.sort()
three_most_expensive_purchases = sum(buy_sum[-3::])


assert three_most_expensive_purchases == 202346
