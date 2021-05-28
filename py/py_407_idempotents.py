# Solution of;
# Project Euler Problem 407: Idempotents
# https://projecteuler.net/problem=407
# 
# If we calculate a2 mod 6 for 0 ≤ a ≤ 5 we get: 0,1,4,3,4,1. The largest 
# value of a such that a2 ≡ a mod 6 is 4. Let's call M(n) the largest value of 
# a < n such that a2 ≡ a (mod n). So M(6) = 4. Find ∑ M(n) for 1 ≤ n ≤ 107.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
