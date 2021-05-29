# Solution of;
# Project Euler Problem 320: Factorials divisible by a huge integer
# https://projecteuler.net/problem=320
# 
# Let N(i) be the smallest integer n such that n! is divisible by 
# (i!)1234567890Let S(u)=∑ N(i) for 10 ≤ i ≤ u. S(1000)=614538266565663. Find 
# S(1 000 000) mod 1018.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 320
    timed.caller(dummy, n, i, prob_id)
