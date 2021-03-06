# Solution of;
# Project Euler Problem 528: Constrained Sums
# https://projecteuler.net/problem=528
# 
# Let S(n,k,b) represent the number of valid solutions to x1 + x2 + . . . + xk 
# ≤ n, where 0 ≤ xm ≤ bm for all 1 ≤ m ≤ k. For example, S(14,3,2) = 135, 
# S(200,5,3) = 12949440, and S(1000,10,5) mod 1 000 000 007 = 624839075. Find 
# (∑10 ≤ k ≤ 15 S(10k,k,k)) mod 1 000 000 007.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 528
    timed.caller(dummy, n, i, prob_id)
