import unittest
from unittest.mock import patch

from src.top_up_balance import top_up_balance


class TestTopUpBalance(unittest.TestCase):

    @patch("builtins.input", side_effect=["exit"])
    def test_top_up_balance_exit(self, mock_input):
        result = top_up_balance(10000)
        self.assertEqual(result, 10000.0)

    @patch("builtins.print")
    def test_top_up_balance(self, mock_print):
        with patch("builtins.input", side_effect=["inf", "aavd", "400"]):
            result = top_up_balance(10000)
        self.assertTrue(result)
        mock_print.assert_called_with("Сумма должна быть числом")
        self.assertTrue(result)
        mock_print.assert_called_with("Сумма должна быть числом")
        self.assertEqual(result, 10400)
