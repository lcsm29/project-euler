# Solution of;
# Project Euler Problem 268: Counting numbers with at least four distinct prime factors less than 100
# https://projecteuler.net/problem=268
# 
# It can be verified that there are 23 positive integers less than 1000 that 
# are divisible by at least four distinct primes less than 100. Find how many 
# positive integers less than 1016 are divisible by at least four distinct 
# primes less than 100.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 268
    timed.caller(dummy, n, i, prob_id)
