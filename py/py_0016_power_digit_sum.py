# Solution of;
# Project Euler Problem 16: Power digit sum
# https://projecteuler.net/problem=16
# 
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def fn_short(n):
    return sum([int(c) for c in str(2 ** n)])


if __name__ == '__main__':
    n = 1_000
    i = 40_000
    prob_id = 16
    timed.caller(fn_short, n, i, prob_id)
