# ATM

## Описание:

ATM - это прототип работы банкомата.

## Использование:
* Клонируем репозитроий *git@github.com:AntonNadein/ATM.git*
* Устанавливаем зависимоти **pyproject.toml**
* Запускаем функционал при помощи файлов **main.py,**


## Документация:
1. Модуль *[card_for_test.py](src%2Fcard_for_test.py)* класс для генерации данных карты.
2. Модуль *[pin_check.py](src%2Fpin_check.py)* для проверки пин кода карты.
3. Модуль *[find_out_balance.py](src%2Ffind_out_balance.py)* выводит баланс карты.
4. Модуль *[remittance.py](src%2Fremittance.py)* имитирует:
- перевод по номеру телефона
- перевод на карту(по номеру)
- перевод на счет(по номеру)
5. Модуль *[top_up_balance.py](src%2Ftop_up_balance.py)* пополняет баланс карты.
6. Модуль *[remove_balance.py](src%2Fremove_balance.py)* имитирует снятие денег:
- с разменом
- без размена
7. Вспомогательный модуль *[selection_condition.py](src%2Fselection_condition.py)* функция выбора пунктов меню.
8. Вспомогательный модуль *[selection_cycles.py](src%2Fselection_cycles.py)* функция выбора да/нет.

## Тестирование:
Для тестироваия используйте файлы 
**[test_card_for_test.py](tests%2Ftest_card_for_test.py)
[test_find_out_balance.py](tests%2Ftest_find_out_balance.py)
[test_pin_check.py](tests%2Ftest_pin_check.py)
[test_remittance.py](tests%2Ftest_remittance.py)
[test_remove_balance.py](tests%2Ftest_remove_balance.py)
[test_selection_condition.py](tests%2Ftest_selection_condition.py)
[test_selection_cycles.py](tests%2Ftest_selection_cycles.py)
[test_top_up_balance.py](tests%2Ftest_top_up_balance.py)**

test coverage 99%

## Лицензия:

Этот проект не имеет лицензий.