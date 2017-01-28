import os
import sys

examples_dir = os.path.abspath(os.path.dirname(__file__))
root_dir = os.path.join(examples_dir, '..')
lib_dir = os.path.join(root_dir, 'lib')

sys.path.insert(0, examples_dir)
sys.path.insert(1, lib_dir)
