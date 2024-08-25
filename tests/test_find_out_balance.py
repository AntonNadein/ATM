from src.find_out_balance import find_out_balance


def test_find_out_balance(capsys):
    find_out_balance(1000)
    captured = capsys.readouterr()
    assert captured.out == "Баланс вашей карты: 1000\n\n"
