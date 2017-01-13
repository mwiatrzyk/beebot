#!/usr/bin/env python3

import os
import sys
import unittest

root_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
testing_dir = os.path.join(root_dir, 'testing')
lib_dir = os.path.join(root_dir, 'lib')

sys.path.insert(0, root_dir)
sys.path.insert(1, lib_dir)

from beebot.config import config

config.update({
    'root_dir': root_dir
})


def load_tests():
    path = os.path.join(testing_dir, 'unit')
    loader = unittest.TestLoader()
    return loader.discover(path)


def run_tests(suite):
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


def main():
    suite = load_tests()
    status = run_tests(suite)
    if status.wasSuccessful():
        return 0
    else:
        return 1


sys.exit(main())
