# Solution of;
# Project Euler Problem 322: Binomial coefficients divisible by 10
# https://projecteuler.net/problem=322
# 
# Let T(m, n) be the number of the binomial coefficients iCn that are 
# divisible by 10 for n ≤ i < m(i, m and n are positive integers). You are 
# given that T(109, 107-10) = 989697000. Find T(1018, 1012-10).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 322
    timed.caller(dummy, n, i, prob_id)
