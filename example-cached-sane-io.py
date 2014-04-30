#!/usr/bin/env python

# Simple program to demonstrate profiling; this version has no big bugs

import sys

usage = """
  example.py FILENAME
  Reads the file FILENAME, which must contain a list of integers, one per line.
  For each integer i, outputs the i'th member of the fibonacci sequence.
"""

_fib_cache=dict()

def nth_fib(n):
    if n not in _fib_cache:
        _fib_cache[n] = compute_nth_fib(n)
    return _fib_cache[n]

def compute_nth_fib(n):
    if n <= 0: return 0
    elif n == 1: return 1
    else: return nth_fib(n-1) + nth_fib(n-2)

def main(command, filename):
    with open(filename) as f:
        for line in f.readlines():
            n = int(line.rstrip())
            print nth_fib(n)

if __name__ == "__main__":
    try:
        main(*sys.argv)
    except Exception as e:
        print >> sys.stderr, e, usage

