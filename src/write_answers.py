from src.static.task_types import TaskTypes


def format_answer(type_task, arg1, arg2, result):
    return f'{arg1} {"+" if type_task == TaskTypes.Add else "*"} {arg2} = {result}\n'


def write_tasks(answers, write):
    for answer in answers:
        for task in answer:
            write(format_answer(*task))


def print_without_line_break(*arguments):
    print(*arguments, end='')


def write_answers(answers, output_file):
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            write_tasks(answers, f.write)
    else:
        write_tasks(answers, print_without_line_break)
