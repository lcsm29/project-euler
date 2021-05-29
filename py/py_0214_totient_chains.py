# Solution of;
# Project Euler Problem 214: Totient Chains
# https://projecteuler.net/problem=214
# 
# Let φ be Euler's totient function, i. e. for a natural number n,φ(n) is the 
# number of k, 1 ≤ k ≤ n, for which gcd(k,n) = 1. By iterating φ, each 
# positive integer generates a decreasing chain of numbers ending in 1. E. g. 
# if we start with 5 the sequence 5,4,2,1 is generated. Here is a listing of 
# all chains with length 
# 4:5,4,2,17,6,2,18,4,2,19,6,2,110,4,2,112,4,2,114,6,2,118,6,2,1Only two of 
# these chains start with a prime, their sum is 12. What is the sum of all 
# primes less than 40000000 which generate a chain of length 25?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 214
    timed.caller(dummy, n, i, prob_id)
