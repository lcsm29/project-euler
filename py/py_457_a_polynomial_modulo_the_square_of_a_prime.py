# Solution of;
# Project Euler Problem 457: A polynomial modulo the square of a prime
# https://projecteuler.net/problem=457
# 
# Let f(n) = n2 - 3n - 1. Let p be a prime. Let R(p) be the smallest positive 
# integer n such that f(n) mod p2 = 0 if such an integer n exists, otherwise 
# R(p) = 0. Let SR(L) be ∑ R(p) for all primes not exceeding L. Find SR(107).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
