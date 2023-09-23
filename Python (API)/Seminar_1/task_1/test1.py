'''
Задание 1
С использованием фреймворка pytest написать тест операции checkText
SOAP API https://speller.yandex.net/services/spellservice?WSDL
Тест должен использовать DDT и проверять наличие определенного
верного слова в списке предложенных исправлений к определенному
неверному слову.
Слова должны быть заданы через фикстуры в conftest.py,
адрес wsdl должен быть вынесен в config.yaml.
Методы работы с SOAP должны быть вынесены в отдельную библиотеку.
'''


from api import check_text


def test_step1(valid_word, invalid_word) -> None:
    assert valid_word in check_text(invalid_word), 'test_step1 FAIL'

