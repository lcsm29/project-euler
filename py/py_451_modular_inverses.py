# Solution of;
# Project Euler Problem 451: Modular inverses
# https://projecteuler.net/problem=451
# 
# Consider the number 15. There are eight positive numbers less than 15 which 
# are coprime to 15: 1, 2, 4, 7, 8, 11, 13, 14. The modular inverses of these 
# numbers modulo 15 are: 1, 8, 4, 13, 2, 11, 7, 14 because1 · 1 mod 15=12 · 
# 8=16 mod 15=14 · 4=16 mod 15=17 · 13=91 mod 15=111 · 11=121 mod 15=114 · 
# 14=196 mod 15=1Let I(n) be the largest positive number m smaller than n-1 
# such that the modular inverse of m modulo n equals m itself. So I(15)=11. 
# Also I(100)=51 and I(7)=1. Find ∑ I(n) for 3≤n≤2×107
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
