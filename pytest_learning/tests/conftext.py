import pytest

@pytest.fixture() #действие до
def auth():
    print('Вход в систему выполнен')
