# Solution of;
# Project Euler Problem 25: 1000-digit Fibonacci number
# https://projecteuler.net/problem=25
# 
# The Fibonacci sequence is defined by the recurrence relation:
#   Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1. 
#
# Hence the first 12 terms will be:
#   F1 = 1
#   F2 = 1
#   F3 = 2
#   F4 = 3
#   F5 = 5
#   F6 = 8
#   F7 = 13
#   F8 = 21
#   F9 = 34
#   F10 = 55
#   F11 = 89
#   F12 = 144
#
# The 12th term, F12, is the first term to contain three digits. What is the
# index of the first term in the Fibonacci sequence to contain 1000 digits?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def fn_fib_next(n):
    a, b, i = 1, 1, 2
    while len(str(b)) < n:
        a, b, i = b, a + b, i + 1
    return i


if __name__ == '__main__':
    n = 1_000
    i = 40
    prob_id = 25
    timed.caller(fn_fib_next, n, i, prob_id)
