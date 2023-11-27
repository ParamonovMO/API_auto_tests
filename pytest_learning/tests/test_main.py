import pytest

def test_sending_mail_1(auth):
    print('Первое письмо отправлено')


def test_sending_mail_2(auth):
    print('Второе письмо отправлено')


def test_sending_mail_3(auth):
    print('Третье письмо отправлено')

#Запуск pytest -s -v
#-s - Отображение результата работы функций
#-v - Отображение файла, функций и результата теста
