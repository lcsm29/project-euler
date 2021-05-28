# Solution of;
# Project Euler Problem 127: abc-hits
# https://projecteuler.net/problem=127
# 
# The radical of n, rad(n), is the product of distinct prime factors of n. For 
# example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42. We shall define 
# the triplet of positive integers (a, b, c) to be an abc-hit if:GCD(a, b) = 
# GCD(a, c) = GCD(b, c) = 1a < ba + b = crad(abc) < cFor example, (5, 27, 32) 
# is an abc-hit, because:GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 15 < 275 + 27 
# = 32rad(4320) = 30 < 32It turns out that abc-hits are quite rare and there 
# are only thirty-one abc-hits for c < 1000, with ∑c = 12523. Find ∑c for c < 
# 120000.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
