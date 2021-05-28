# Solution of;
# Project Euler Problem 699: Triffle Numbers
# https://projecteuler.net/problem=699
# 
# Let $\sigma(n)$ be the sum of all the divisors of the positive integer $n$, 
# for example:$\sigma(10) = 1+2+5+10 = 18$. Define $T(N)$ to be the sum of all 
# numbers $n \le N$ such that when the fraction $\frac{\sigma(n)}{n}$ is 
# written in its lowest form $\frac ab$, the denominator is a power of 3 i. e. 
# $b = 3^k, k > 0$. You are given $T(100) = 270$ and $T(10^6) = 26089287$. 
# Find $T(10^{14})$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
