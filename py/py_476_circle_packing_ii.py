# Solution of;
# Project Euler Problem 476: Circle Packing II
# https://projecteuler.net/problem=476
# 
# Let R(a, b, c) be the maximum area covered by three non-overlapping circles 
# inside a triangle with edge lengths a, b and c. Let S(n) be the average 
# value of R(a, b, c) over all integer triplets (a, b, c) such that 1 ≤ a ≤ b 
# ≤ c < a + b ≤ nYou are given S(2) = R(1, 1, 1) ≈ 0. 31998, S(5) ≈ 1. 25899. 
# Find S(1803) rounded to 5 decimal places behind the decimal point.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
