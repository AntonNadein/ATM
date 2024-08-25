def selection_condition(
    question: str, answer_one: str, answer_two: str, answer_three: str, answer_four: str
) -> str:
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



# result = selection_condition("Выбор из меню:", "Узнать баланс", "Снять деньги", "Внести деньги", "Перевод по номеру телефона")
# print(result)