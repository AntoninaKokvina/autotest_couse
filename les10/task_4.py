# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.usefixtures('print_time')
class Test:

    def test_1(self):
        assert all_division(10000000, 100000) == 100

    @pytest.mark.usefixtures('print_work_time')
    def test_2(self):
        assert all_division(1, 8) == 0.125

    def test_3(self):
        assert all_division(100, -10, 2) == -5

    def test_4(self):
        with pytest.raises(IndexError):
            all_division()

    def test_5(self):
        with pytest.raises(ZeroDivisionError):
            all_division(5, 0)

