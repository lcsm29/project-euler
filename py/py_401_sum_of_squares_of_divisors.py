# Solution of;
# Project Euler Problem 401: Sum of squares of divisors
# https://projecteuler.net/problem=401
# 
# The divisors of 6 are 1,2,3 and 6. The sum of the squares of these numbers 
# is 1+4+9+36=50. Let sigma2(n) represent the sum of the squares of the 
# divisors of n. Thus sigma2(6)=50. Let SIGMA2 represent the summatory 
# function of sigma2, that is SIGMA2(n)=∑ sigma2(i) for i=1 to n. The first 6 
# values of SIGMA2 are: 1,6,16,37,63 and 113. Find SIGMA2(1015) modulo 109.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
