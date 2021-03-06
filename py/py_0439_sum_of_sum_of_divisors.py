# Solution of;
# Project Euler Problem 439: Sum of sum of divisors
# https://projecteuler.net/problem=439
# 
# Let d(k) be the sum of all divisors of k. We define the function S(N) = 
# $\sum_{i=1}^N \sum_{j=1}^Nd(i \cdot j)$. For example, S(3) = d(1) + d(2) + 
# d(3) + d(2) + d(4) + d(6) + d(3) + d(6) + d(9) = 59. You are given that 
# S(103) = 563576517282 and S(105) mod 109 = 215766508. Find S(1011) mod 109.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 439
    timed.caller(dummy, n, i, prob_id)
