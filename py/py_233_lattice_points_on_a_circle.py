# Solution of;
# Project Euler Problem 233: Lattice points on a circle
# https://projecteuler.net/problem=233
# 
# Let f(N) be the number of points with integer coordinates that are on a 
# circle passing through (0,0), (N,0),(0,N), and (N,N). It can be shown that 
# f(10000) = 36. What is the sum of all positive integers N ≤ 1011 such that 
# f(N) = 420 ?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
