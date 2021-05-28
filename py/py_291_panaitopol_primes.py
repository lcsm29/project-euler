# Solution of;
# Project Euler Problem 291: Panaitopol Primes
# https://projecteuler.net/problem=291
# 
# A prime number $p$ is called a Panaitopol prime if $p = \dfrac{x^4 - 
# y^4}{x^3 + y^3}$ for some positive integers $x$ and $y$. Find how many 
# Panaitopol primes are less than 5×1015.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
