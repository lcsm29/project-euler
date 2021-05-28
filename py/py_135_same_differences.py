# Solution of;
# Project Euler Problem 135: Same differences
# https://projecteuler.net/problem=135
# 
# Given the positive integers, x, y, and z, are consecutive terms of an 
# arithmetic progression, the least value of the positive integer, n, for 
# which the equation, x2 − y2 − z2 = n, has exactly two solutions is n = 
# 27:342 − 272 − 202 = 122 − 92 − 62 = 27It turns out that n = 1155 is the 
# least value which has exactly ten solutions. How many values of n less than 
# one million have exactly ten distinct solutions?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
