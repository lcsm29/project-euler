# Solution of;
# Project Euler Problem 549: Divisibility of factorials
# https://projecteuler.net/problem=549
# 
# The smallest number m such that 10 divides m! is m=5. The smallest number m 
# such that 25 divides m! is m=10. Let s(n) be the smallest number m such that 
# n divides m!. So s(10)=5 and s(25)=10. Let S(n) be ∑s(i) for 2 ≤ i ≤ n. 
# S(100)=2012. Find S(108).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
