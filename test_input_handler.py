import pytest
from input_handler import get_valid_guess


@pytest.fixture
def mock_input(monkeypatch):
    def change_input(values: list[str]):
        inputs = iter(values)
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    return change_input


def test_get_valid_guess(mock_input, capsys):
    mock_input(["abc", "50"])
    result = get_valid_guess()
    assert "You must enter a number!" in capsys.readouterr().out
    assert result == 50


def test_get_valid_guess_out_of_range(mock_input):
    mock_input(["150", "50"])
    result = get_valid_guess()
    assert result == 50


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("1", 1),
        ("100", 100),
        ("50", 50),
    ],
)
def test_get_valid_guess_valid_values(mock_input, user_input, expected):
    mock_input([user_input])
    result = get_valid_guess()
    assert result == expected


def test_get_valid_guess_invalid_boundaries(mock_input):
    mock_input(["0", "101", "50"])
    result = get_valid_guess()
    assert result == 50
