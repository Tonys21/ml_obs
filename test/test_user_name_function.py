# test_user_name_function.py
import pytest
import io
from src.user_name_function import get_user_name_from_input

## Must test if "not empty" and if "no space"

def test_username_with_no_space(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra adaltas.com'))
    assert get_user_name_from_input() is None

#def test_username_not_empty(monkeypatch):
#    monkeypatch.setattr('sys.stdin', io.StringIO(''))
#    assert get_user_name_from_input() is None

def test_username_no_error(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_user_name_from_input() == 'petra@adaltas.com'
