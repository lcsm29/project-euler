# Solution of;
# Project Euler Problem 443: GCD sequence
# https://projecteuler.net/problem=443
# 
# Let g(n) be a sequence defined as follows:g(4) = 13,g(n) = g(n-1) + gcd(n, 
# g(n-1)) for n > 4. The first few values are: n4567891011121314151617181920. 
# . . g(n)1314161718272829303132333451545560. . . You are given that g(1 000) 
# = 2524 and g(1 000 000) = 2624152. Find g(1015).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 443
    timed.caller(dummy, n, i, prob_id)
