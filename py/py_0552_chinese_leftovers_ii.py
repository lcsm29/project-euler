# Solution of;
# Project Euler Problem 552: Chinese leftovers II
# https://projecteuler.net/problem=552
# 
# Let An be the smallest positive integer satisfying An mod pi = i for all 1 ≤ 
# i ≤ n, where pi is thei-th prime. For example A2 = 5, since this is the 
# smallest positive solution of the system of equations A2 mod 2 = 1 A2 mod 3 
# = 2The system of equations for A3 adds another constraint. That is, A3 is 
# the smallest positive solution of A3 mod 2 = 1 A3 mod 3 = 2 A3 mod 5 = 3and 
# hence A3 = 23. Similarly, one gets A4 = 53 and A5 = 1523. Let S(n) be the 
# sum of all primes up to n that divide at least one element in the sequence 
# A. For example, S(50) = 69 = 5 + 23 + 41, since 5 divides A2, 23 divides A3 
# and 41 divides A10 = 5765999453. No other prime number up to 50 divides an 
# element in A. Find S(300000).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 552
    timed.caller(dummy, n, i, prob_id)
