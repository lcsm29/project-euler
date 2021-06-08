# Solution of;
# Project Euler Problem 20: Factorial digit sum
# https://projecteuler.net/problem=20
# 
# n! means n × (n − 1) × . . . × 3 × 2 × 1
# 
# For example, 10! = 10 × 9 × . . . × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! 
# is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. 
# 
# Find the sum of the digits in the number 100!
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed
import math


def fn_brute(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return sum([int(c) for c in str(fact)])


def fn_math_fact_based(n):
    return sum([int(c) for c in str(math.factorial(n))])


if __name__ == '__main__':
    n = 100
    i = 95_000
    prob_id = 20
    timed.caller(fn_brute, n, i, prob_id)
    timed.caller(fn_math_fact_based, n, i, prob_id)
