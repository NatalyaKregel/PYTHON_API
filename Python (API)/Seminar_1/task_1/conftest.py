import pytest


@pytest.fixture()
def valid_word():
    return 'молоко'     #если ввести здесь с ошибкой тест провалится


@pytest.fixture()
def invalid_word():
    return 'малоко'
