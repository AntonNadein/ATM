from src.selection_cycles import while_true_question


def remove_balance(balance: float) -> float:
    """
    Функция выдачи наличных
    :param balance: Тетущий баланс
    :return: Баланс после выдачи
    """
    while True:
        withdraw_money = input("Введите сумму для снятия:\n" "или 0 для возырата в предыдущее меню\n")
        if withdraw_money == "0":
            return balance
        try:
            withdraw_money = int(withdraw_money)
            if withdraw_money > balance:
                print("У вас не достаточно средств\n")
            elif withdraw_money % 100 != 0:
                print("Введите другую сумму\n")
            else:
                answer = while_true_question("Желаете снять с разменом", "да", "нет")
                if answer == "да":
                    issuance = money_change(withdraw_money)
                elif answer == "нет":
                    issuance = not_money_change(withdraw_money)
                print(
                    f"Выданы наличные:\n"
                    f"5000: {issuance.get("money5000", "---")} шт\n"
                    f"2000: {issuance.get("money2000", "---")} шт\n"
                    f"1000: {issuance.get("money1000", "---")} шт\n"
                    f"500: {issuance.get("money500", "---")} шт\n"
                    f"100: {issuance.get("money100", "---")} шт\n"
                )
                return balance - withdraw_money
        except ValueError:
            print("Сумма должна быть числом")


def not_money_change(withdraw_money):
    """Выдача денег без размена"""
    money_dict = {}
    while True:
        if withdraw_money // 5000 > 0:
            money5000 = withdraw_money // 5000
            money_dict["money5000"] = money5000
            withdraw_money -= money5000 * 5000
        elif withdraw_money // 2000 > 0:
            money2000 = withdraw_money // 2000
            money_dict["money2000"] = money2000
            withdraw_money -= money2000 * 2000
        elif withdraw_money // 1000 > 0:
            money1000 = withdraw_money // 1000
            money_dict["money1000"] = money1000
            withdraw_money -= money1000 * 1000
        elif withdraw_money // 500 > 0:
            money500 = withdraw_money // 500
            money_dict["money500"] = money500
            withdraw_money -= money500 * 500
        elif withdraw_money // 100 > 0:
            money100 = withdraw_money // 100
            money_dict["money100"] = money100
            withdraw_money -= money100 * 100
        elif withdraw_money == 0:
            break
    return money_dict


def money_change(withdraw_money):
    """Выдача денег с разменом"""
    money_dict = {}
    while True:
        if withdraw_money // 5000 > 1:
            money5000 = withdraw_money // 5000
            money_dict["money5000"] = money5000
            withdraw_money -= money5000 * 5000
        elif withdraw_money // 2000 > 2:
            money2000 = withdraw_money // 2000
            money_dict["money2000"] = money2000
            withdraw_money -= money2000 * 2000
        elif withdraw_money // 1000 > 3:
            money1000 = withdraw_money // 1000
            money_dict["money1000"] = money1000
            withdraw_money -= money1000 * 1000
        elif withdraw_money // 500 > 2:
            money500 = withdraw_money // 500
            money_dict["money500"] = money500
            withdraw_money -= money500 * 500
        elif withdraw_money // 100 > 0:
            money100 = withdraw_money // 100
            money_dict["money100"] = money100
            withdraw_money -= money100 * 100
        elif withdraw_money == 0:
            break
    return money_dict
