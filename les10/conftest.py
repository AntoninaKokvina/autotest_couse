import pytest
import datetime

@pytest.fixture(scope='class')
def print_time():
    print(f'\nвремя старта: {datetime.datetime.now().strftime("%d.%m %H:%M:%S")}')
    yield
    print(f'\nвремя окончания: {datetime.datetime.now().strftime("%d.%m %H:%M:%S")}')

@pytest.fixture()
def print_work_time():
    start = datetime.datetime.now()
    yield
    end = datetime.datetime.now()
    print(f'\nвремя выполнения: {end - start}')