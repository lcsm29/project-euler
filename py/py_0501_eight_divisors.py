# Solution of;
# Project Euler Problem 501: Eight Divisors
# https://projecteuler.net/problem=501
# 
# The eight divisors of 24 are 1, 2, 3, 4, 6, 8, 12 and 24. The ten numbers 
# not exceeding 100 having exactly eight divisors are 24, 30, 40, 42, 54, 56, 
# 66, 70, 78 and 88. Let f(n) be the count of numbers not exceeding n with 
# exactly eight divisors. You are given f(100) = 10, f(1000) = 180 and f(106) 
# = 224427. Find f(1012).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 501
    timed.caller(dummy, n, i, prob_id)
