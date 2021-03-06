# Solution of;
# Project Euler Problem 134: Prime pair connection
# https://projecteuler.net/problem=134
# 
# Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that 
# 1219 is the smallest number such that the last digits are formed by p1 
# whilst also being divisible by p2. In fact, with the exception of p1 = 3 and 
# p2 = 5, for every pair of consecutive primes, p2 > p1, there exist values of 
# n for which the last digits are formed by p1 and n is divisible by p2. Let S 
# be the smallest of these values of n. Find ∑ S for every pair of consecutive 
# primes with 5 ≤ p1 ≤ 1000000.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 134
    timed.caller(dummy, n, i, prob_id)
