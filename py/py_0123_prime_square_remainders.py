# Solution of;
# Project Euler Problem 123: Prime square remainders
# https://projecteuler.net/problem=123
# 
# Let pn be the nth prime: 2, 3, 5, 7, 11, . . . , and let r be the remainder 
# when (pn−1)n + (pn+1)n is divided by pn2. For example, when n = 3, p3 = 5, 
# and 43 + 63 = 280 ≡ 5 mod 25. The least value of n for which the remainder 
# first exceeds 109 is 7037. Find the least value of n for which the remainder 
# first exceeds 1010.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 123
    timed.caller(dummy, n, i, prob_id)
