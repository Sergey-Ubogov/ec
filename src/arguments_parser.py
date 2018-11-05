from argparse import ArgumentParser


class ArgParser:
    def __init__(self):
        self.parser = ArgumentParser(description='Operations on elliptic curve curves (c) Sergey Ubogov')
        self.parser.add_argument('-i', '--input_file', help='file with tests', default='input.txt')
        self.parser.add_argument('-o', '--output_file', help='file for answers')

    def get_arguments(self):
        return self.parser.parse_args()
