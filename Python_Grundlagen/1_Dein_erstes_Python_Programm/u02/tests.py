from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_initial():
    window = get_answer_placeholders()[0]
    if window == 'fügen Sie hier einen Kommentar ein':
        failed('Sie sollten die Datei bearbeiten')
    else:
        passed()


if __name__ == '__main__':
    run_common_tests('Gib deinen Namen ein')
    test_initial()
