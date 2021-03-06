# Solution of;
# Project Euler Problem 596: Number of lattice points in a hyperball
# https://projecteuler.net/problem=596
# 
# Let T(r) be the number of integer quadruplets x, y, z, t such that x2 + y2 + 
# z2 + t2 ≤ r2. In other words, T(r) is the number of lattice points in the 
# four-dimensional hyperball of radius r. You are given that T(2) = 89, T(5) = 
# 3121, T(100) = 493490641 and T(104) = 49348022079085897. Find T(108) mod 
# 1000000007.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 596
    timed.caller(dummy, n, i, prob_id)
