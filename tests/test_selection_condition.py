import unittest
from unittest.mock import patch

from src.selection_condition import number_check, selection_condition


class TestSelectionCondition(unittest.TestCase):

    @patch("builtins.input", side_effect=["one", "two", "three", "four", "exit"])
    def test_selection_condition(self, mock_input):
        result = selection_condition("question", "one", "two", "three", "four")
        self.assertEqual(result, "one")

        result = selection_condition("question", "one", "two", "three", "four")
        self.assertEqual(result, "two")

        result = selection_condition("question", "one", "two", "three", "four")
        self.assertEqual(result, "three")

        result = selection_condition("question", "one", "two", "three", "four")
        self.assertEqual(result, "four")

        result = selection_condition("question", "one", "two", "three", "four")
        self.assertEqual(result, "exit")


class TestNumberCheck(unittest.TestCase):

    @patch("builtins.input", side_effect=["123", "exit"])
    def test_number_check(self, mock_input):
        result = number_check("question", 3)
        self.assertTrue(result)

        result = number_check("question", 3)
        self.assertFalse(result)

    @patch("builtins.print")
    def test_number_check_invalid_input(self, mock_print):
        with patch("builtins.input", side_effect=["1234", "12345"]):
            result = number_check("question", 5)
        self.assertTrue(result)
        mock_print.assert_called_with("Введенное значения не является числом или длинна числа не равна 5\n")


# второй работающий тест на отловлю принта
# def test_number_check_invalid_input_part2(capsys):
#     with patch('builtins.input', side_effect=['1234', '12345']):
#         number_check("question", 5)
#     captured = capsys.readouterr()
#     assert captured.out == "Введенное значения не является числом или длинна числа не равна 5\n\n"
