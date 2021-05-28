# Solution of;
# Project Euler Problem 66: Diophantine equation
# https://projecteuler.net/problem=66
# 
# Consider quadratic Diophantine equations of the form:x2 – Dy2 = 1For 
# example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1. It can 
# be assumed that there are no solutions in positive integers when D is 
# square. By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain 
# the following:32 – 2×22 = 122 – 3×12 = 192 – 5×42 = 152 – 6×22 = 182 – 7×32 
# = 1Hence, by considering minimal solutions in x for D ≤ 7, the largest x is 
# obtained when D=5. Find the value of D ≤ 1000 in minimal solutions of x for 
# which the largest value of x is obtained.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
