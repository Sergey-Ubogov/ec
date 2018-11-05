from src.parse_test import parse_test


def get_tests(input_file):
    with open(input_file, encoding='utf-8') as f:
        tests = f.read().split('\n\n')

    return list(map(parse_test, tests))


