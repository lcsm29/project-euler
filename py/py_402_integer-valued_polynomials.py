# Solution of;
# Project Euler Problem 402: Integer-valued polynomials
# https://projecteuler.net/problem=402
# 
# It can be shown that the polynomial n4 + 4n3 + 2n2 + 5n is a multiple of 6 
# for every integer n. It can also be shown that 6 is the largest integer 
# satisfying this property. Define M(a, b, c) as the maximum m such that n4 + 
# an3 + bn2 + cn is a multiple of m for all integers n. For example, M(4, 2, 
# 5) = 6. Also, define S(N) as the sum of M(a, b, c) for all 0 < a, b, c ≤ N. 
# We can verify that S(10) = 1972 and S(10000) = 2024258331114. Let Fk be the 
# Fibonacci sequence:F0 = 0, F1 = 1 andFk = Fk-1 + Fk-2 for k ≥ 2. Find the 
# last 9 digits of ∑ S(Fk) for 2 ≤ k ≤ 1234567890123.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
