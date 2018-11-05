from src.arguments_parser import ArgParser
from src.get_tests import get_tests
from src.write_answers import  write_answers


if __name__ == '__main__':
    args = ArgParser().get_arguments()

    tests = get_tests(args.input_file)
    answers = map(lambda test: test.solve_tasks(), tests)

    write_answers(answers, args.output_file)
