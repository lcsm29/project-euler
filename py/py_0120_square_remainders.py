# Solution of;
# Project Euler Problem 120: Square remainders
# https://projecteuler.net/problem=120
# 
# Let r be the remainder when (a−1)n + (a+1)n is divided by a2. For example, 
# if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49. And as n varies, 
# so too will r, but for a = 7 it turns out that rmax = 42. For 3 ≤ a ≤ 1000, 
# find ∑ rmax.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 120
    timed.caller(dummy, n, i, prob_id)
