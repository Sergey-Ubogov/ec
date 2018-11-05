from src.static.task_types import TaskTypes


class Curve:
    def __init__(self, n, tasks, a, b):
        self.n = n
        self.a = a
        self.b = b
        self.tasks = tasks
        self.answers = []

    def solve_tasks(self):
        return list(map(self.solve_task, self.tasks))

    def solve_task(self, task):
        type_task, arg1, arg2 = task
        if type_task == TaskTypes.Add:
            return TaskTypes.Add, arg1, arg2, self.add(arg1, arg2)
        elif type_task == TaskTypes.Mull:
            return TaskTypes.Mull, arg1, arg2, self.mull(arg1, arg2)

