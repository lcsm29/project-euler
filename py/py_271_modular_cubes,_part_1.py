# Solution of;
# Project Euler Problem 271: Modular Cubes, part 1
# https://projecteuler.net/problem=271
# 
# For a positive number n, define S(n) as the sum of the integers x, for which 
# 1<x<n andx3≡1 mod n. When n=91, there are 8 possible values for x, namely : 
# 9, 16, 22, 29, 53, 74, 79, 81. Thus, S(91)=9+16+22+29+53+74+79+81=363. Find 
# S(13082761331670030).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
