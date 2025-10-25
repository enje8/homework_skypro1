import pytest
from string_utils import StringUtils


string_utils = StringUtils()

#Позитивные тесты
def test_trim_positive():
    res = string_utils.trim(" skypro")
    assert res == "skypro"


def test_contains_positive():
    res = string_utils.contains("skypro", "k")
    assert res is True


def test_delete_symbol_positive():
    res = string_utils.delete_symbol("sky-pro", "-")
    assert res == "skypro"


#Негативные тесты
def test_trim_negative():
    res = string_utils.trim("skypro")
    assert res == "skypro"


def test_contains_negative():
    res = string_utils.contains("skypro", "a")
    assert res is False


def test_delete_symbol_negative():
    res = string_utils.delete_symbol("skypro", "z")
    assert res == "skypro"
