# Solution of;
# Project Euler Problem 452: Long Products
# https://projecteuler.net/problem=452
# 
# Define F(m,n) as the number of n-tuples of positive integers for which the 
# product of the elements doesn't exceed m. F(10, 10) = 571. F(106, 106) mod 1 
# 234 567 891 = 252903833. Find F(109, 109) mod 1 234 567 891.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
