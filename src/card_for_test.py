import random


class CardTest:
    """Класс для генерации тестовых карт"""
    number: str
    balance: float
    pin: int

    def __init__(self, number="", balance=None, pin=None):
        """Инициализация характеристик карты:
        number: 16-ти значный номер карты если не задан сгенерируется вавтоматически.
        balance: баланс карты если не задан сгенерируется вавтоматически.
        pin: 4-х значный номер если не задан сгенерируется вавтоматически.
        """
        if number == "" or len(number) != 16 or not number.isdigit():
            list1 = []
            for i in range(4):
                list1.append(str(random.randint(1000, 9999)))
            self.number = f"{list1[0]} {list1[1]} {list1[2]} {list1[3]}"
        else:
            self.number = f"{number[0:4]} {number[4:8]} {number[8:12]} {number[12:]}"

        if type(balance) is float or type(balance) is int:
            self.balance = balance
        else:
            self.balance = random.randint(10, 999)

        if type(pin) is int:
            self.pin = pin
        else:
            self.pin = random.randint(1000, 9999)
