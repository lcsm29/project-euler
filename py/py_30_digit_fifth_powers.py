# Solution of;
# Project Euler Problem 30: Digit fifth powers
# https://projecteuler.net/problem=30
# 
# Surprisingly there are only three numbers that can be written as the sum of 
# fourth powers of their digits:1634 = 14 + 64 + 34 + 448208 = 84 + 24 + 04 + 
# 849474 = 94 + 44 + 74 + 44As 1 = 14 is not a sum it is not included. The sum 
# of these numbers is 1634 + 8208 + 9474 = 19316. Find the sum of all the 
# numbers that can be written as the sum of fifth powers of their digits.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
