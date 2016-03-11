from collections import deque
from workabilly.base.workers import BaseTask

class TaskQueue:

    def __init__(self):
        self.queue = []
        self.done = deque()

    def add(self, task):
        self.queue.append(task)

    def __lshift__(self, task):
        if isinstance(BaseTask, task):
            self.add(task)

    def execute(self, current, **kwargs):

        current.beforeExecute()

        res = {}
        if kwargs:
            current.prepare(**kwargs)
            current.describe()
            res = current.execute(**kwargs)
        else:
            current.describe()
            res = current.execute()

        self.done.append(current)
        return res

    def start(self, **kwargs):
        if not self.queue:
            print("Queue is empty!")

        data = {}
        while len(self.queue) > 0:
            current = self.queue.pop(0)
            if current is None:
                continue
            ret = self.execute(current, **data)
            if ret:
                data.update(ret)

        while len(self.done) > 0:
            current = self.done.pop()
            current.afterExecute()
