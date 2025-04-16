from src.decorators import log


def test_log_to_console_success(capsys):
    """Тест успешного выполнения с выводом в консоль"""

    @log()
    def add(a: int, b: int) -> int:
        return a + b

    result = add(2, 3)

    captured = capsys.readouterr()
    output = captured.out

    assert "add ok" in output
    assert "Result = 5" in output
    assert str(result) in output


def test_log_to_file_success(tmp_path):
    """Тест успешного выполнения с записью в файл"""
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def multiply(a: int, b: int) -> int:
        return a * b

    multiply(3, 4)

    assert log_file.exists()

    content = log_file.read_text(encoding="utf-8")
    assert "multiply ok" in content
    assert "Result = 12" in content


def test_log_to_console_error(capsys):
    """Тест ошибки с выводом в консоль"""

    @log()
    def divide(a: int, b: int) -> float:
        return a / b

    try:
        divide(1, 0)
    except ZeroDivisionError:
        pass

    captured = capsys.readouterr()
    assert "divide error" in captured.out
    assert "ZeroDivisionError" in captured.out


def test_log_returns_correct_value():
    """Тест что декоратор возвращает правильное значение"""

    @log()
    def greet(name: str) -> str:
        return f"Hello, {name}!"

    assert greet("Alice") == "Hello, Alice!"
