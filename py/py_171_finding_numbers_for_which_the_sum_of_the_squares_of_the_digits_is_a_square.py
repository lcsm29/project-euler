# Solution of;
# Project Euler Problem 171: Finding numbers for which the sum of the squares of the digits is a square
# https://projecteuler.net/problem=171
# 
# For a positive integer n, let f(n) be the sum of the squares of the digits 
# (in base 10) of n, e. g. f(3) = 32 = 9,f(25) = 22 + 52 = 4 + 25 = 29,f(442) 
# = 42 + 42 + 22 = 16 + 16 + 4 = 36Find the last nine digits of the sum of all 
# n, 0 < n < 1020, such that f(n) is a perfect square.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
