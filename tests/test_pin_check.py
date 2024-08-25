import unittest
from unittest.mock import patch

from src.pin_check import check_pin


class TestCheckPin(unittest.TestCase):
    @patch("builtins.input", side_effect=["нет", 12, "нет", 12, "нет", 12])
    def test_check_pin(self, mock_input):
        result = check_pin(1)
        self.assertEqual(result, False)

    @patch("builtins.input", side_effect=["нет", 12, "нет", 12, "нет", 1])
    def test_check_pin_true(self, mock_input):
        result = check_pin(1)
        self.assertEqual(result, True)

    @patch("builtins.input", side_effect=["нет", 1])
    def test_check_pin_first_true(self, mock_input):
        result = check_pin(1)
        self.assertEqual(result, True)

    @patch("builtins.input", side_effect=["да"])
    def test_check_pin_first_false(self, mock_input):
        result = check_pin(1)
        self.assertEqual(result, False)
