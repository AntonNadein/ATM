def top_up_balance(balance):
    while True:
        new_balance = input("Внесите деньги для пополнения счета:\n")
        try:
            if not new_balance == "inf":
                new_balance = float(new_balance)
                balance += new_balance
                return balance
        except ValueError:
            print("Сумма должна быть числом")
        if new_balance == "exit":
            return balance


# print(top_up_balance(500))
