# Solution of;
# Project Euler Problem 258: A lagged Fibonacci sequence
# https://projecteuler.net/problem=258
# 
# A sequence is defined as:gk = 1, for 0 ≤ k ≤ 1999gk = gk-2000 + gk-1999, for 
# k ≥ 2000. Find gk mod 20092010 for k = 1018.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
