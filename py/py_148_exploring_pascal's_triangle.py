# Solution of;
# Project Euler Problem 148: Exploring Pascal's triangle
# https://projecteuler.net/problem=148
# 
# We can easily verify that none of the entries in the first seven rows of 
# Pascal's triangle are divisible by 7: 1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 
# 10 5 11 6 15 20 15 6 1However, if we check the first one hundred rows, we 
# will find that only 2361 of the 5050 entries are not divisible by 7. Find 
# the number of entries which are not divisible by 7 in the first one billion 
# (109) rows of Pascal's triangle.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
