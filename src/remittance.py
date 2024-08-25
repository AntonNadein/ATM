from src.selection_condition import number_check, selection_condition


def remittance(balance: float) -> float:
    """
    Функция перевода средств
    :param balance: Начальный баланс
    :return: Баланс после операций
    """
    while True:
        # выбор условия
        result = selection_condition(
            "Выберете: \nПеревод по номеру телефона введите '1'"
            "\nПеревод на карту введите '2'"
            "\nПеревод а счет введите '3'"
            "\nВернуться назад введите '4'",
            "1",
            "2",
            "3",
            "4",
        )
        if result == "four":
            return balance
        # проверка достаточности средств
        try:
            input_amount = float(input("\nВведите сумму для перевода: \n"))
            if input_amount >= balance:
                print("Недостаточно средств введите другую сумму.")
                return balance
            # логика проверки выбранного условия
            if result == "one":
                answer = number_check("Введите номер телефона", 10)
                if answer:
                    balance -= input_amount
                    print(f"Операция выполнена текущий баланс: {balance}\n")
            elif result == "two":
                answer = number_check("Введите номер карты", 16)
                if answer:
                    balance -= input_amount
                    print("Операция выполнена\n")
                    print(f"Операция выполнена текущий баланс: {balance}\n")
            elif result == "three":
                answer = number_check("Введите номер карты", 20)
                if answer:
                    balance -= input_amount
                    print("Операция выполнена\n")
                    print(f"Операция выполнена текущий баланс: {balance}\n")
        except ValueError:
            print("Введенная сумма должна быть числом\n")


# print(remittance(10000))
