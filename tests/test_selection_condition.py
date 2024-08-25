import unittest
from unittest.mock import patch

from src.selection_condition import selection_condition


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
