from src.card_for_test import CardTest
from src.pin_check import check_pin

if __name__ == "__main__":
    # тестовая карта
    test_card = CardTest()
    test_number_card = test_card.number
    test_balance_card = test_card.balance
    test_pin_card = test_card.pin
    print(test_pin_card)

    # тело проекта
    answer = check_pin(test_pin_card)
    if not answer:
        print("Хорошего дня!")