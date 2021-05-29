# Solution of;
# Project Euler Problem 104: Pandigital Fibonacci ends
# https://projecteuler.net/problem=104
# 
# The Fibonacci sequence is defined by the recurrence relation:Fn = Fn−1 + 
# Fn−2, where F1 = 1 and F2 = 1. It turns out that F541, which contains 113 
# digits, is the first Fibonacci number for which the last nine digits are 1-9 
# pandigital (contain all the digits 1 to 9, but not necessarily in order). 
# And F2749, which contains 575 digits, is the first Fibonacci number for 
# which the first nine digits are 1-9 pandigital. Given that Fk is the first 
# Fibonacci number for which the first nine digits AND the last nine digits 
# are 1-9 pandigital, find k.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 104
    timed.caller(dummy, n, i, prob_id)
