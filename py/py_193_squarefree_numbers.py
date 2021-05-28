# Solution of;
# Project Euler Problem 193: Squarefree Numbers
# https://projecteuler.net/problem=193
# 
# A positive integer n is called squarefree, if no square of a prime divides 
# n, thus 1, 2, 3, 5, 6, 7, 10, 11 are squarefree, but not 4, 8, 9, 12. How 
# many squarefree numbers are there below 250?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
