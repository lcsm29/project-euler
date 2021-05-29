# Solution of;
# Project Euler Problem 179: Consecutive positive divisors
# https://projecteuler.net/problem=179
# 
# Find the number of integers 1 < n < 107, for which n and n + 1 have the same 
# number of positive divisors. For example, 14 has the positive divisors 1, 2, 
# 7, 14 while 15 has 1, 3, 5, 15.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 179
    timed.caller(dummy, n, i, prob_id)
