from unittest.mock import patch

from src.card_for_test import CardTest


def test_card_test(card_test):
    assert card_test.number == "1234 5678 9012 3456"
    assert card_test.balance == 100
    assert card_test.pin == 1234


@patch("random.randint")
def test_card_test_random(mock_rand):
    mock_rand.return_value = 1234
    card_test = CardTest()
    assert card_test.number == "1234 1234 1234 1234"
    assert card_test.balance == 1234
    assert card_test.pin == 1234