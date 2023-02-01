from test_helper import run_common_tests, failed, passed, import_task_file, get_answer_placeholders


def test_task_window():
    window = get_answer_placeholders()[0]
    if 'aendern Sie diesen Wert' == window:
        failed('Sie sollten die Variablen \'hello\' neu definieren.')
    else:
        passed()


def test_value():
    file = import_task_file()

    if file.greetings == 'hallo':
        failed('Sie sollten der Variablen einen anderen Wert zuweisen')
    else:
        passed()


if __name__ == '__main__':
    test_task_window()
    run_common_tests('Sie sollten die Variablen \'hello\' neu definieren.')
    test_value()
