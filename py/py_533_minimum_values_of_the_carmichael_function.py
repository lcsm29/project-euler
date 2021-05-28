# Solution of;
# Project Euler Problem 533: Minimum values of the Carmichael function
# https://projecteuler.net/problem=533
# 
# The Carmichael function λ(n) is defined as the smallest positive integer m 
# such that am = 1 modulo n for all integers a coprime with n. For example 
# λ(8) = 2 and λ(240) = 4. Define L(n) as the smallest positive integer m such 
# that λ(k) ≥ n for all k ≥ m. For example, L(6) = 241 and L(100) = 20 174 525 
# 281. Find L(20 000 000). Give the last 9 digits of your answer.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
