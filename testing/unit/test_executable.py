import unittest

from testing.component.calculate import Calculate


class TestExecutable(unittest.TestCase):

    def setUp(self):
        self.sut = Calculate()

    def test_foo(self):

        def task(sut):
            sut.stdin.send({'operator': 'add', 'args': [1, 2, 3]})
            sut.stdout.receive({'result': 6})

        self.sut.start()
        self.sut.run(task)
        self.sut.done()
