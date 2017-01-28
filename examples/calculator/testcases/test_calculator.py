import os
import unittest

from beebot.context import Context

from calculator.components import Calculator

root_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')


class TestExecutable(unittest.TestCase):

    def setUp(self):
        self.ctx = Context(root_dir=root_dir)
        self.sut = Calculator(self.ctx)

    def test_check_calculator(self):
        self.sut.start()
        self.sut.stdin.send({'operator': 'sub', 'args': [1, 2]})
        self.sut.stdout.receive({'result': -1})
        self.sut.done()

    def test_check_calculator_using_synchronous_task(self):

        def task(sut):
            sut.stdin.send({'operator': 'add', 'args': [1, 2, 3]})
            sut.stdout.receive({'result': 6})

        self.sut.start()
        self.sut.run(task)
        self.sut.done()

    def test_check_calculator_using_asynchronous_task(self):

        def task(sut):
            sut.stdin.send({'operator': 'add', 'args': [1, 2, 3]})
            sut.stdout.receive({'result': 6})

        self.sut.start()
        self.sut.run_async(task)
        self.sut.done()
