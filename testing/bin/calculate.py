#!/usr/bin/env python3

import sys


def subtract(args):
    result = args[0]
    for a in args[1:]:
        result -= a
    return result


def multiply(args):
    result = args[0]
    for a in args[1:]:
        result *= a
    return result


def read():

    def convert(data):
        for x in data:
            if '.' in x:
                yield float(x)
            else:
                yield int(x)

    line = sys.stdin.readline()
    if line != 'done':
        line = line.split()
        return line[0], [x for x in convert(line[1:])]


def write(value):
    if isinstance(value, int):
        sys.stdout.write('%d\n' % value)
    else:
        sys.stdout.write('%f\n' % value)
    sys.stdout.flush()


def main():
    while True:
        cmd = read()
        if not cmd:
            return 0
        op, args = cmd
        if op == 'add':
            write(sum(args))
        elif op == 'sub':
            write(subtract(args))
        elif op == 'mul':
            write(multiply(args))
        else:
            sys.stderr.write('Invalid operator: %s\n' % op)


sys.exit(main())
