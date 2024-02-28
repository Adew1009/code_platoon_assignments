import subprocess
import pytest
import calculator


def test_add():
    assert calculator.calculate(2, 3, "add") == 5

# Add more functional tests for subtract, multiply, and divide


def test_terminal_output(capsys):
    str_output = calculator.calculate(10, 2, "multiply")
    print("Result:", str_output)
    captured = capsys.readouterr()
    assert captured.out == "Result: 20\n"


def test_argument_passing(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
    assert calculator.calculate(6, 2, "divide") == 3.0


# Add more tests to cover edge cases and negative scenarios
# import subprocess


def test_divide_by_zero():
    assert calculator.calculate(2, 0, "divide") == "Cannot divide by zero"


def test_add():
    assert calculator.calculate(2, 3, "add") == 5


def test_divide():
    assert calculator.calculate(2, 2, "divide") == 1


def test_divide_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.calculate(2, 0, 'divide')


def test_add_float():
    assert calculator.calculate(2, 1.5, "add") == 3.5

   # Add more functional tests for subtract, multiply, and divide


def test_too_few_args():
    result = subprocess.run(
        ["python3", "calculator.py", '10', "divide"], text=True, capture_output=True)
    assert result.stdout == "Usage: calculator.py <num1> <num2> <operation>\n"


def test_too_many_args():
    result = subprocess.run(["python3", "calculator.py", '6',
                            '2', "10", "divide"], text=True, capture_output=True)
    assert result.stdout == "Usage: calculator.py <num1> <num2> <operation>\n"


def test_argument_passing():
    result = subprocess.run(
        ["python3", "calculator.py", '6', '2', "divide"], text=True, capture_output=True)
    assert result.stdout == "Result: 3.0\n"

   # Add more tests to cover edge cases and negative scenarios
