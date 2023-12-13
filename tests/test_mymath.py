# pylint: disable=missing-docstring
from urllib.parse import quote_plus
import pytest
import requests_mock

from my_pdm_project_cwprogram_test.mymath import (
    add_numbers,
    average_numbers,
    subtract_numbers,
    multiply_numbers,
    divide_numbers,
    make_mathjs_request,
    BASE_URI
)


def test_makemathjs_request():
    with requests_mock.Mocker() as m:
        m.get(f'{BASE_URI}{quote_plus("2+3")}', text='5')
        m.get(f'{BASE_URI}{quote_plus("7/3")}', text='5')
        result = make_mathjs_request(2, 3, '+')
        result2 = make_mathjs_request(7, 3, '/')
    assert result == 5
    assert isinstance(result, int)
    assert isinstance(result2, float)


def test_makemathjs_unsupported_operation():
    with pytest.raises(ValueError):
        make_mathjs_request(2, 3, '~')


def test_add():
    with requests_mock.Mocker() as m:
        m.get(f'{BASE_URI}{quote_plus("2+3")}', text='5')
        assert add_numbers(2, 3) == 5


@pytest.mark.parametrize('x,y,expected', [(0, 3, -3), (5, 3, 2)])
def test_subtract(x, y, expected):
    with requests_mock.Mocker() as m:
        m.get(f"{BASE_URI}{quote_plus(f'{x}-{y}')}", text=f'{expected}')
        assert subtract_numbers(x, y) == expected


@pytest.mark.parametrize('x,y,expected', [(3, 0, 0), (2, 3, 6)])
def test_multiply(x, y, expected):
    with requests_mock.Mocker() as m:
        m.get(f"{BASE_URI}{quote_plus(f'{x}*{y}')}", text=f'{expected}')
        assert multiply_numbers(x, y) == expected


def test_divide():
    with requests_mock.Mocker() as m:
        m.get(f"{BASE_URI}{quote_plus(f'{6}/{3}')}", text='2')
        m.get(f"{BASE_URI}{quote_plus(f'{7}/{3}')}", text='2.3333333333333335')
        assert divide_numbers(6, 3) == 2
        assert divide_numbers(7, 3) == 2.3333333333333335
        with pytest.raises(ZeroDivisionError):
            divide_numbers(3, 0)


def test_average():
    assert average_numbers([90, 88, 99, 100]) == 94.25
