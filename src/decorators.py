import datetime
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для  логирования функции
    Если имя файла указано, логи пишутся в файл, иначе - логи выводятся в консоль
    """

    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Сщздаем сообщение для лога
            """
            func_name = func.__name__
            time_start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = None
            success = False
            message = ""
            try:
                result = func(*args, **kwargs)
                success = True
                message = f"{time_start} - {func_name} ok: Result = {result}"
            except Exception as e:
                message = (f"{time_start} - {func_name} error: {type(e).__name__}."
                           f"Inputs: {args}, {kwargs}\n")
                raise e
            finally:
                """
                Записываем лог в файл или выводим в консоль
                """
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message)
                else:
                    print(message, end="")
            return result if "result" in locals() else None

        return wrapper

    return decorator
