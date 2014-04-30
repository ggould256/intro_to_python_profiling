#!/usr/bin/env python

# Simple program to demonstrate profiling; has two major performance bugs.

import sys

usage = """
  example.py FILENAME
  Reads the file FILENAME, which must contain a list of integers, one per line.
  For each integer i, outputs the i'th member of the fibonacci sequence.
"""

def nth_fib(n):
    if n <= 0: return 0
    elif n == 1: return 1
    else: return nth_fib(n-1) + nth_fib(n-2)

def count_lines(filename):
    with open(filename) as f:
        return len(f.readlines())

def nth_line(filename, n):
    with open(filename) as f:
        return int(f.readlines()[n].rstrip())

def main(command, filename):
    for line_number in xrange(count_lines(filename)):
        print nth_fib(nth_line(filename, line_number))

if __name__ == "__main__":
    try:
        main(*sys.argv)
    except Exception as e:
        print >> sys.stderr, e, usage

