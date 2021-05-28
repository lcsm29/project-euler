# Solution of;
# Project Euler Problem 625: Gcd sum
# https://projecteuler.net/problem=625
# 
# $G(N)=\sum_{j=1}^N\sum_{i=1}^j \text{gcd}(i,j)$. You are given: $G(10)=122$. 
# Find $G(10^{11})$. Give your answer modulo 998244353
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
