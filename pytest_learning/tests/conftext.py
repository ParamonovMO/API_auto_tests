import pytest

@pytest.fixture() #действие до
def auth():
    print('Вход в систему выполнен')

@pytest.fixture(scope='module')
def some():
    print('Начало')
    yield
    print('Конец')
