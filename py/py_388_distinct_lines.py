# Solution of;
# Project Euler Problem 388: Distinct Lines
# https://projecteuler.net/problem=388
# 
# Consider all lattice points (a,b,c) with 0 ≤ a,b,c ≤ N. From the origin 
# O(0,0,0) all lines are drawn to the other lattice points. Let D(N) be the 
# number of distinct such lines. You are given that D(1 000 000) = 
# 831909254469114121. Find D(1010). Give as your answer the first nine digits 
# followed by the last nine digits.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
