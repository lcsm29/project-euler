# Solution of;
# Project Euler Problem 20: Factorial digit sum
# https://projecteuler.net/problem=20
# 
# n! means n × (n − 1) × . . . × 3 × 2 × 1For example, 10! = 10 × 9 × . . . × 
# 3 × 2 × 1 = 3628800,and the sum of the digits in the number 10! is 3 + 6 + 2 
# + 8 + 8 + 0 + 0 = 27. Find the sum of the digits in the number 100!
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 20
    timed.caller(dummy, n, i, prob_id)
