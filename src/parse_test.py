from src.static.curve_types import CurveTypes
from src.classes.curves.simple_curve import SimpleCurve
from src.classes.curves.supersingular_curve import SupersingularCurve
from src.classes.curves.non_supersingular_curve import NonSupersingularCurve
from src.static.task_types import TaskTypes
from src.classes.point import Point


def parse_task(task):
    type_task, arg1, arg2 = task.split()
    if type_task == TaskTypes.Add:
        return type_task, Point(*arg1[1:-1].split(',')), Point(*arg2[1:-1].split(','))
    elif type_task == TaskTypes.Mull:
        return type_task, Point(*arg1[1:-1].split(',')), int(arg2)


def parse_test(test):
    line_with_type, n, params, *tasks = test.split('\n')
    n = int(n)
    tasks = list(map(parse_task, filter(lambda task: task, tasks)))

    type = CurveTypes.Simple if line_with_type != CurveTypes.Supersingular and line_with_type != CurveTypes.NonSupersingular else line_with_type

    if type == CurveTypes.Simple:
        p = int(line_with_type)
        a, b = [int(parameter) for parameter in params.split()]

        return SimpleCurve(n, tasks, a, b, p)
    else:
        a, b, c = [int(parameter) for parameter in params.split()]
        if type == CurveTypes.NonSupersingular:
            return NonSupersingularCurve(n, tasks, a, b, c)
        elif type == CurveTypes.Supersingular:
            return SupersingularCurve(n, tasks, a, b, c)