import pytest

def test_sending_mail_1(auth, some):
    print('Первое письмо отправлено')


def test_sending_mail_2(auth, some):
    print('Второе письмо отправлено')


def test_sending_mail_3(auth, some):
    print('Третье письмо отправлено')

#Запуск pytest -s -v test_main.py
#-s - Отображение результата работы функций
#-v - Отображение файла, функций и результата теста
