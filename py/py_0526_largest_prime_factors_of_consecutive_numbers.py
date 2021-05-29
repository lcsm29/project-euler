# Solution of;
# Project Euler Problem 526: Largest prime factors of consecutive numbers
# https://projecteuler.net/problem=526
# 
# Let f(n) be the largest prime factor of n. Let g(n) = f(n) + f(n+1) + f(n+2) 
# + f(n+3) + f(n+4) + f(n+5) + f(n+6) + f(n+7) + f(n+8), the sum of the 
# largest prime factor of each of nine consecutive numbers starting with n. 
# Let h(n) be the maximum value of g(k) for 2 ≤ k ≤ n. You are given:f(100) = 
# 5f(101) = 101g(100) = 409h(100) = 417h(109) = 4896292593Find h(1016).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 526
    timed.caller(dummy, n, i, prob_id)
