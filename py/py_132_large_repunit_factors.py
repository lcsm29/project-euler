# Solution of;
# Project Euler Problem 132: Large repunit factors
# https://projecteuler.net/problem=132
# 
# A number consisting entirely of ones is called a repunit. We shall define 
# R(k) to be a repunit of length k. For example, R(10) = 1111111111 = 
# 11×41×271×9091, and the sum of these prime factors is 9414. Find the sum of 
# the first forty prime factors of R(109).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
