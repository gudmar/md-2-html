from rich import print
import traceback

def get_fail_message(description, expected, result):
    return '''
    [red]Failed test[/] [[bold red]{}[/]].
    [green]Expected [{}][/],
    [red]received [{}][/]
    '''.format(description, expected, result)

def get_exception_message(description, expected, result):
    return '''
    [bold red]:warning:[/][black on red]Exception during test[/] [[bold red]{}[/]].
    [green]Expected [{}][/],
    [red]received [{}][/]
    '''.format(description, expected, result)


def get_fail_report(*args):
    description, expected, result = args
    message = get_fail_message(*args)
    return {
        "description": description,
        "expected": expected,
        "result": result,
        "message": message,
    }

def get_error_report(*args):
    description, expected, result, error = args
    error_name = type(error).__name__
    return {
        'description':description, 
        'expected':expected, 
        'result':result, 
        'message': error_name
    }

def run_tests(test_cases, tested_function):
    passed = []
    failed = []
    for test_case in test_cases:
        try:
            result = tested_function(test_case['input'])
            is_passed = result == test_case['expected']
            # is_passed = test_case["comparition"](result, test_case['expected'])
            print(result)
            print(test_case['expected'])
            if is_passed:
                passed.append(test_case['description'])
            else:
                failed.append(get_fail_report(test_case['description'], test_case['expected'], result))
        except Exception as error:
            # failed.append(get_fail_message(test_case['description'], test_case['expected'], result))
            failed.append(get_exception_message(test_case['description'], test_case['expected'], error))
            # failed.append(traceback.format_exc())
            print(traceback.format_exc())
    print('[blue]Executed: {}[/], [green]passed: {}[/], [red]failed: {}[/]'.format(len(test_cases), len(passed), len(failed)))
    # print('Failed:')
    for fail in failed:
        # print(fail)
        # print(fail['message'])
        print(fail["message"])
