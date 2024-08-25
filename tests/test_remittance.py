import unittest
from unittest.mock import patch

from src.remittance import remittance


class TestRemittance(unittest.TestCase):

    @patch("builtins.input", side_effect=["1", 500, "1234567890", "4"])
    def test_number_check_phone(self, mock_input):
        result = remittance(10000)
        self.assertEqual(result, 9500.0)

    @patch("builtins.input", side_effect=["2", 500, "1234567890123456", "4"])
    def test_number_check_card(self, mock_input):
        result = remittance(10000)
        self.assertEqual(result, 9500.0)

    @patch("builtins.input", side_effect=["3", 500, "12345678901234567890", "4"])
    def test_number_check_account(self, mock_input):
        result = remittance(10000)
        self.assertEqual(result, 9500.0)

    @patch("builtins.print")
    def test_number_check_account_invalid_input_word(self, mock_print):
        with patch("builtins.input", side_effect=["1", "sfwgr", "4"]):
            result = remittance(10000)
        self.assertTrue(result)
        mock_print.assert_called_with("Введенная сумма должна быть числом\n")

    @patch("builtins.print")
    def test_number_check_account_invalid_input(self, mock_print):
        with patch("builtins.input", side_effect=["1", 15000, "4"]):
            result = remittance(10000)
        self.assertTrue(result)
        mock_print.assert_called_with("Недостаточно средств введите другую сумму.")
