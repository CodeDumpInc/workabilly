from nose.tools import *
from workabilly.base.task import BaseTask

def test_task_necessary():
    task = BaseTask()
    assert(task.run_necessary())

def test_task_return_dict():
    task = BaseTask()
    assert(task.execute() is not None)