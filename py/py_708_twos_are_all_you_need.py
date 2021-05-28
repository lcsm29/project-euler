# Solution of;
# Project Euler Problem 708: Twos are all you need
# https://projecteuler.net/problem=708
# 
# A positive integer, $n$, is factorised into prime factors. We define $f(n)$ 
# to be the product when each prime factor is replaced with $2$. In addition 
# we define $f(1)=1$. For example, $90 = 2\times 3\times 3\times 5$, then 
# replacing the primes, $2\times 2\times 2\times 2 = 16$, hence $f(90) = 16$. 
# Let $\displaystyle S(N)=\sum_{n=1}^{N} f(n)$. You are given 
# $S(10^8)=9613563919$. Find $S(10^{14})$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
