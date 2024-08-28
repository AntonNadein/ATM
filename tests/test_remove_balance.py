import unittest
from unittest.mock import patch

import pytest

from src.remove_balance import money_change, not_money_change, remove_balance


@pytest.fixture
def money_change_test1():
    return 18900


@pytest.fixture
def money_change_test2():
    return 4500


@pytest.fixture
def money_change_test3():
    return 1500


def test_money_change_0():
    assert money_change(6000) == {"money2000": 3}


def test_money_change_1(money_change_test1):
    assert money_change(money_change_test1) == {"money100": 4, "money500": 7, "money5000": 3}


def test_money_change_2(money_change_test2):
    assert money_change(money_change_test2) == {"money100": 5, "money1000": 4}


def test_money_change_3(money_change_test3):
    assert money_change(money_change_test3) == {"money500": 3}


def test_not_money_change_1(money_change_test1):
    assert not_money_change(money_change_test1) == {
        "money100": 4,
        "money1000": 1,
        "money2000": 1,
        "money500": 1,
        "money5000": 3,
    }


def test_not_money_change_2(money_change_test2):
    assert not_money_change(money_change_test2) == {"money2000": 2, "money500": 1}


def test_not_money_change_3(money_change_test3):
    assert not_money_change(money_change_test3) == {"money1000": 1, "money500": 1}


class TestRemoveBalance(unittest.TestCase):

    @patch("builtins.input", side_effect=["0"])
    def test_remove_balance_exit(self, mock_input):
        result = remove_balance(10000)
        self.assertEqual(result, 10000.0)

    @patch("builtins.print")
    def test_remove_balance_money_is_tight(self, mock_print):
        with patch("builtins.input", side_effect=["100000", "0"]):
            result = remove_balance(10000)
        self.assertTrue(result)
        mock_print.assert_called_with("У вас не достаточно средств\n")

    @patch("builtins.print")
    def test_remove_balance_money_not_100(self, mock_print):
        with patch("builtins.input", side_effect=["1020", "0"]):
            result = remove_balance(10000)
        self.assertTrue(result)
        mock_print.assert_called_with("Введите другую сумму\n")

    @patch("builtins.print")
    def test_remove_balance_yes(self, mock_print):
        with patch("builtins.input", side_effect=["1900", "да"]):
            result = remove_balance(10000)
        self.assertTrue(result)
        mock_print.assert_called_with(
            "Выданы наличные:\n5000: --- шт\n2000: --- шт\n1000: --- шт\n500: 3 шт\n100: 4 шт\n"
        )
        self.assertEqual(result, 8100)

    @patch("builtins.print")
    def test_remove_balance_no(self, mock_print):
        with patch("builtins.input", side_effect=["18900", "нет"]):
            result = remove_balance(20000)
        self.assertTrue(result)
        mock_print.assert_called_with("Выданы наличные:\n5000: 3 шт\n2000: 1 шт\n1000: 1 шт\n500: 1 шт\n100: 4 шт\n")
        self.assertEqual(result, 1100)

    @patch("builtins.print")
    def test_remove_balance_error(self, mock_print):
        with patch("builtins.input", side_effect=["inf", "0"]):
            result = remove_balance(10000)
        self.assertTrue(result)
        mock_print.assert_called_with("Сумма должна быть числом")
