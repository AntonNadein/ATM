import pytest

from src.card_for_test import CardTest


@pytest.fixture
def card_test():
    return CardTest("1234567890123456", 100, 1234)