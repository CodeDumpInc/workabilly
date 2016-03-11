from collections import deque
from workabilly.base.task import BaseTask

class TaskQueue:

    def __init__(self):
        self.queue = deque()
        self.done = deque()

    def add(self, task):
        self.queue.append(task)

    def __lshift__(self, task):
        if isinstance(BaseTask, task):
            self.add(task)

    def execute(self, current, **kwargs):
        current.beforeExecute()

        args = {}
        args = kwargs

        current.describe(**args)
        result = current.execute(**args)

        self.done.append(current)
        return result

    def run(self, **kwargs):
        if not self.queue:
            print("Queue is empty!")

        data = {}
        data.update(kwargs)
        while len(self.queue) > 0:
            task = self.queue.popleft()
            if task:
                ret = self.execute(task, **data)
                data.update(ret)

        while len(self.done) > 0:
            task = self.done.pop()
            task.afterExecute()
