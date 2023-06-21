import time

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функція {func.__name__} виконалася за {execution_time} секунд")
        return result
    return wrapper

# Приклад функції, для якої буде вимірюватися час виконання
def some_function():
    time.sleep(2)  # Затримка на 2 секунди
    return "Результат"

# Тест для перевірки працездатності функції measure_execution_time
@measure_execution_time
def test_measure_execution_time():
    result = some_function()
    assert result == "Результат"

test_measure_execution_time()
