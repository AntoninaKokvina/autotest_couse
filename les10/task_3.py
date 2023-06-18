# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division



@pytest.mark.parametrize('arg, res', [pytest.param((10000000, 100000), 100, marks=pytest.mark.smoke()),
                                      pytest.param((1, 8), 0.125, marks=pytest.mark.skip('Пропускаем')),
                                      pytest.param((100, -10, 2), -5)])
def test_all(arg, res):
    assert all_division(*arg) == res

