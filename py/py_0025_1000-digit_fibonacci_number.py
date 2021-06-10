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
import sys
sys.setrecursionlimit(10000)


def fn_recursive_bisect(n):
    def fib(num, computed = {0: 0, 1: 1}):
        if num not in computed:
            computed[num] = fib(num - 1, computed) + fib(num - 2, computed)
        return computed[num]
    
    def get_high():
        high = 100
        while len(str(fib(high))) < n:
            high *= 2
        return high
    
    def bsct(n, l=0, h=get_high()):
        m = (l + h) // 2
        while 1:
            tmp = len(str(fib(m)))
            if tmp < n:
                l, m = m, (m + h) // 2
            if tmp > n:
                h, m = m, (m + l) // 2
            if tmp == n:
                break
        return l, m

    low, mid = bsct(n)
    for i in range(low, mid + 1):
        if len(str(fib(i))) >= n:
            return i


def fn_fib_next(n):
    a, b, i = 1, 1, 2
    while len(str(b)) < n:
        a, b, i = b, a + b, i + 1
    return i


if __name__ == '__main__':
    n = 1_000
    i = 40
    prob_id = 25
    timed.caller(fn_recursive_bisect, n, i, prob_id)
    timed.caller(fn_fib_next, n, i, prob_id)
