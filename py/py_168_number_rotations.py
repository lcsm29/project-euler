# Solution of;
# Project Euler Problem 168: Number Rotations
# https://projecteuler.net/problem=168
# 
# Consider the number 142857. We can right-rotate this number by moving the 
# last digit (7) to the front of it, giving us 714285. It can be verified that 
# 714285=5×142857. This demonstrates an unusual property of 142857: it is a 
# divisor of its right-rotation. Find the last 5 digits of the sum of all 
# integers n, 10 < n < 10100, that have this property.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
