def selection_condition(question: str, answer_one: str, answer_two: str, answer_three: str, answer_four: str) -> str:
    """
    Функция логики выбора
    :param question: Условие
    :param answer_true: Первый ответ
    :param answer_false: Второй ответ
    :param answer_false: Третий ответ
    :param answer_false: Четвертый ответ
    :return: Один из ответов
    """
    while True:
        string = (input(f"{question}:\n{answer_one}\n{answer_two}\n{answer_three}\n{answer_four}\n ")).lower()
        if string in [answer_one.lower()]:
            return "one"
        elif string in [answer_two.lower()]:
            return "two"
        elif string in [answer_three.lower()]:
            return "three"
        elif string in [answer_four.lower()]:
            return "four"
        elif string in ["exit"]:
            return "exit"


def number_check(input_question: str, number_of_digits: int) -> bool:
    """Функция проверки номера
    :param input_question: Условие для проверки номера
    :param number_of_digits: Длинна номера
    :return: Bool
    """
    while True:
        input_number = input(f"{input_question}:\n")
        if input_number.isdigit() and len(input_number) == number_of_digits:
            return True
        elif input_number in ["exit"]:
            return False
        else:
            print(f"Введенное значения не является числом или длинна числа не равна {number_of_digits}\n")
