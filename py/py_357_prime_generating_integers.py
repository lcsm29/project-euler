# Solution of;
# Project Euler Problem 357: Prime generating integers
# https://projecteuler.net/problem=357
# 
# Consider the divisors of 30: 1,2,3,5,6,10,15,30. It can be seen that for 
# every divisor d of 30, d+30/d is prime. Find the sum of all positive 
# integers n not exceeding 100 000 000such thatfor every divisor d of n, d+n/d 
# is prime.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
