# Solution of;
# Project Euler Problem 261: Pivotal Square Sums
# https://projecteuler.net/problem=261
# 
# Let us call a positive integer k a square-pivot, if there is a pair of 
# integers m > 0 and n ≥ k, such that the sum of the (m+1) consecutive squares 
# up to k equals the sum of the m consecutive squares from (n+1) on:(k-m)2 + . 
# . . + k2 = (n+1)2 + . . . + (n+m)2. Some small square-pivots are4: 32 + 42 = 
# 5221: 202 + 212 = 29224: 212 + 222 + 232 + 242 = 252 + 262 + 272110: 1082 + 
# 1092 + 1102 = 1332 + 1342Find the sum of all distinct square-pivots ≤ 1010.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 261
    timed.caller(dummy, n, i, prob_id)
