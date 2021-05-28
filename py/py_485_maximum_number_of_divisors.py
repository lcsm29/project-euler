# Solution of;
# Project Euler Problem 485: Maximum number of divisors
# https://projecteuler.net/problem=485
# 
# Let d(n) be the number of divisors of n. Let M(n,k) be the maximum value of 
# d(j) for n ≤ j ≤ n+k-1. Let S(u,k) be the sum of M(n,k) for 1 ≤ n ≤ u-k+1. 
# You are given that S(1000,10)=17176. Find S(100 000 000,100 000).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
