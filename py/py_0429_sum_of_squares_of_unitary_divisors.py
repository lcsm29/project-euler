# Solution of;
# Project Euler Problem 429: Sum of squares of unitary divisors
# https://projecteuler.net/problem=429
# 
# A unitary divisor d of a number n is a divisor of n that has the property 
# gcd(d, n/d) = 1. The unitary divisors of 4! = 24 are 1, 3, 8 and 24. The sum 
# of their squares is 12 + 32 + 82 + 242 = 650. Let S(n) represent the sum of 
# the squares of the unitary divisors of n. Thus S(4!)=650. Find S(100 000 
# 000!) modulo 1 000 000 009.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 429
    timed.caller(dummy, n, i, prob_id)
