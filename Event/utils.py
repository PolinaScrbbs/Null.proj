import sys
import io

def execute_code(code, input_data):
    stdout = io.StringIO()
    sys.stdout = stdout

    try:
        for data in input_data:
            input_index = code.find('input()')
            if input_index != -1:
                code = code[:input_index] + data + code[input_index+7:]
        exec(code)
        result = stdout.getvalue()
        stdout.truncate(0)
        stdout.seek(0)
        return result, True
    except Exception as e:
        return str(e), False
    finally:
        sys.stdout = sys.__stdout__

def test_task(code, input_data_list, output_data_list):
    correct_tests = 0

    for j in range(len(input_data_list)):
        input_data = [x.strip() for x in input_data_list[j].split(", ")]
        test_result, success = execute_code(code, input_data)
        if success:
            print(test_result, output_data_list[j])
            if str(test_result).strip() == str(output_data_list[j]).strip():
                correct_tests += 1
                continue
            else:
                return f'Test {j} error >> result {test_result}', False
        return f'Test {j} error >> {test_result}', False

    if correct_tests == len(input_data_list):
        return 'Успешно', True