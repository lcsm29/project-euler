# Solution of;
# Project Euler Problem 209: Circular Logic
# https://projecteuler.net/problem=209
# 
# A k-input binary truth table is a map from k input bits(binary digits, 0 
# [false] or 1 [true]) to 1 output bit. For example, the 2-input binary truth 
# tables for the logical AND and XOR functions are:xyx AND y000010100111xyx 
# XOR y000011101110How many 6-input binary truth tables, τ, satisfy the 
# formulaτ(a, b, c, d, e, f) AND τ(b, c, d, e, f, a XOR (b AND c)) = 0for all 
# 6-bit inputs (a, b, c, d, e, f)?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
