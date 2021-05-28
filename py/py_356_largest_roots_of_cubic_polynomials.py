# Solution of;
# Project Euler Problem 356: Largest roots of cubic polynomials
# https://projecteuler.net/problem=356
# 
# Let an be the largest real root of a polynomial g(x) = x3 - 2n·x2 + n. For 
# example, a2 = 3. 86619826. . . Find the last eight digits of $\sum 
# \limits_{i = 1}^{30} {\left \lfloor a_i^{987654321} \right \rfloor}$. Note: 
# $\lfloor a \rfloor$ represents the floor function.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
