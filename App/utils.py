import sys
import io

def execute_code(code, input_data):
    # Создаем объект для перехвата вывода
    stdout = io.StringIO()
    sys.stdout = stdout  # Перенаправляем стандартный вывод в объект

    try:
        for data in input_data:
            input_index = code.find('input()')
            if input_index != -1:
                code = code[:input_index] + data + code[input_index+7:]
        # Выполняем код пользователя с использованием входных данных
        exec(code)
        # Получаем результат выполнения
        result = stdout.getvalue()
        # Очищаем буфер вывода
        stdout.truncate(0)
        stdout.seek(0)
        # Возвращаем результат
        return result, True
    except Exception as e:
        # Обрабатываем ошибки выполнения кода
        return str(e), False
    finally:
        # Возвращаем стандартный поток вывода в исходное состояние
        sys.stdout = sys.__stdout__