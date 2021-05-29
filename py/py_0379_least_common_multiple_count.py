# Solution of;
# Project Euler Problem 379: Least common multiple count
# https://projecteuler.net/problem=379
# 
# Let f(n) be the number of couples (x,y) with x and y positive integers, x ≤ 
# y and the least common multiple of x and y equal to n. Let g be the 
# summatory function of f, i. e. : g(n) = ∑ f(i) for 1 ≤ i ≤ n. You are given 
# that g(106) = 37429395. Find g(1012).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 379
    timed.caller(dummy, n, i, prob_id)
