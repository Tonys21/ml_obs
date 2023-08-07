# test_user_password_function.py
import pytest
import io
from src.user_password_function import get_password_from_input


## Must test if "at least 8 characters", "at least 1 special character", "at least 1 letter" and "at least one letter"

def test_password_with_8_char(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO(',com'))
    assert get_password_from_input() is None


def test_password_with_1_special_char(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Testing2023'))
    assert get_password_from_input() is None


def test_password_with_1_letter_char(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('2023@2023'))
    assert get_password_from_input() is None


def test_password_with_1_numeric_char(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Testing@deuxmillevingttrois'))
    assert get_password_from_input() is None


def test_password_no_error(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Testing@2023'))
    assert get_password_from_input() == 'Testing@2023'
