from src.card_for_test import CardTest
from src.find_out_balance import find_out_balance
from src.pin_check import check_pin
from src.remittance import remittance
from src.remove_balance import remove_balance
from src.selection_condition import selection_condition
from src.top_up_balance import top_up_balance

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
        exit()
    while True:
        print("Выберете один из пунктов меню:\n")
        answer = selection_condition("Введитте:\n 1 УЗНАТЬ БАЛАНС\n 2 ПЕРЕВОД"
                                     "\n 3 ВНЕСТИ НА КАРТУ\n 4 СНЯТЬ\n 0 ВЫХОД",
                                     "1", "2", "3", "4")
        if answer == "one":
            # баланс
            find_out_balance(test_balance_card)
        elif answer == "two":
            # перевод
            test_balance_card = remittance(test_balance_card)
        elif answer == "three":
            # внести на карту
            test_balance_card = top_up_balance(test_balance_card)
        elif answer == "four":
            # снять
            test_balance_card = remove_balance(test_balance_card)
        elif answer == "exit":
            print("Спасибо что воспользовались нашими услугами. Хорошего дня!")
            break
