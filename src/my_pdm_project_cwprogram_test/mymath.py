"""
A module containing simple math operations.
"""
from urllib.parse import quote_plus
import numpy as np
import requests

BASE_URI = "http://api.mathjs.org/v4/?expr="
SUPPORTED_OPERATIONS = ['+', '-', '*', '/']


def make_mathjs_request(a: int, b: int, operation: str):
    """Make a expression call against the MathJS API

    :param a: Base integer for the operation
    :type a: int
    :param b: Integer to use with a in the operation
    :type b: int
    :param operation: Operation to run against a and b
    :type operation: str

    :raises ZeroDivisionError: Raised if division by 0
    :raises ValueError: Raised if not a supported operation

    :returns:
        - int for non division operations
        - float for division operations
    """
    if operation == '/' and b == 0:
        raise ZeroDivisionError
    if operation not in SUPPORTED_OPERATIONS:
        raise ValueError

    operation_expression = quote_plus(f'{a}{operation}{b}')
    res = requests.get(
        f'{BASE_URI}{operation_expression}', timeout=20
    )

    if operation == '/':
        return float(res.text)
    return int(res.text)


def add_numbers(a: int, b: int):
    """Add two numbers together

    :param a: The base integer to use in the add operation
    :type a: int
    :param b: The integer to add to the base integer
    :type b: int

    :return: The sum of both integers
    :rtype: int
    """
    return make_mathjs_request(a, b, '+')


def subtract_numbers(a: int, b: int):
    """Subtract two numbers

    :param a: The base integer to use in the subtract operation
    :type a: int
    :param b: The integer to subtract the base integer from
    :type b: int

    :return: The subtraction of both numbers
    :rtype: int
    """
    return make_mathjs_request(a, b, '-')


def multiply_numbers(a: int, b: int):
    """Multiple two numbers together

    :param a: The base integer to use in the multiply operation
    :type a: int
    :param b: The integer to multiply against the base number
    :type b: int

    :return: The result of multiplying both numbers
    :rtype: int
    """
    return make_mathjs_request(a, b, '*')


def divide_numbers(a: int, b: int):
    """Divide two numbers

    :param a: The base integer to use in the add operation
    :type a: int
    :param b: The integer divide a by
    :type b: int

    :return: The quotient of the division operation
    :rtype: float
    """
    return make_mathjs_request(a, b, '/')


def average_numbers(numbers: list[int]):
    """Average a list of numbers

    :param numbers: The list of numbers to average
    :type numbers: list[int]

    :return: The average of the numbers
    :rtype: float
    """
    return np.average(numbers)
