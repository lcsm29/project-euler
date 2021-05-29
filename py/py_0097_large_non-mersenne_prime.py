# Solution of;
# Project Euler Problem 97: Large non-Mersenne prime
# https://projecteuler.net/problem=97
# 
# The first known prime found to exceed one million digits was discovered in 
# 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 
# 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have 
# been found which contain more digits. However, in 2004 there was found a 
# massive non-Mersenne prime which contains 2,357,207 digits: 
# 28433×27830457+1. Find the last ten digits of this prime number.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 97
    timed.caller(dummy, n, i, prob_id)
