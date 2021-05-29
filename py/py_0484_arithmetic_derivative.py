# Solution of;
# Project Euler Problem 484: Arithmetic Derivative
# https://projecteuler.net/problem=484
# 
# The arithmetic derivative is defined byp' = 1 for any prime p(ab)' = a'b + 
# ab' for all integers a, b (Leibniz rule)For example, 20' = 24. Find ∑ 
# gcd(k,k') for 1 < k ≤ 5×1015. Note: gcd(x,y) denotes the greatest common 
# divisor of x and y.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 484
    timed.caller(dummy, n, i, prob_id)
