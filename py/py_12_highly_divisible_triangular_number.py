# Solution of;
# Project Euler Problem 12: Highly divisible triangular number
# https://projecteuler.net/problem=12
# 
# The sequence of triangle numbers is generated by adding the natural numbers. 
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The 
# first ten terms would be:1, 3, 6, 10, 15, 21, 28, 36, 45, 55, . . . Let us 
# list the factors of the first seven triangle numbers: 1: 1 3: 1,3 6: 
# 1,2,3,610: 1,2,5,1015: 1,3,5,1521: 1,3,7,2128: 1,2,4,7,14,28We can see that 
# 28 is the first triangle number to have over five divisors. What is the 
# value of the first triangle number to have over five hundred divisors?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)