from src.selection_cycles import while_true_question


def check_pin(number: int) -> bool:
    """Функция проверки пин кода карты"""
    i = 3
    while i != 0:
        input_word = while_true_question("Вернуть карту?\nВведите: да/нет\n", "да", "нет")
        if input_word == "да":
            return False
        elif input_word == "нет":
            input_number = int(input("Введите пин код ****:\n "))
            if input_number != number:
                i -= 1
                if i == 2:
                    word = "попытки"
                elif i == 1:
                    word = "попытка"
                else:
                    print("Ваша карта заблокирована\n")
                    return False
                print(f"Вы ввели неверный пин у вас осталость {i} {word} до блокировки карты\n")
            else:
                print("Вы ввели верный пин код\n")
                return True
