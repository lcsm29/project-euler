# Solution of;
# Project Euler Problem 47: Distinct primes factors
# https://projecteuler.net/problem=47
# 
# The first two consecutive numbers to have two distinct prime factors are:14 
# = 2 × 715 = 3 × 5The first three consecutive numbers to have three distinct 
# prime factors are:644 = 2² × 7 × 23645 = 3 × 5 × 43646 = 2 × 17 × 19. Find 
# the first four consecutive integers to have four distinct prime factors 
# each. What is the first of these numbers?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 47
    timed.caller(dummy, n, i, prob_id)
