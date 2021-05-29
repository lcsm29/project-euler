# Solution of;
# Project Euler Problem 28: Number spiral diagonals
# https://projecteuler.net/problem=28
# 
# Starting with the number 1 and moving to the right in a clockwise direction 
# a 5 by 5 spiral is formed as follows:21 22 23 24 2520 7 8 9 1019 6 1 2 1118 
# 5 4 3 1217 16 15 14 13It can be verified that the sum of the numbers on the 
# diagonals is 101. What is the sum of the numbers on the diagonals in a 1001 
# by 1001 spiral formed in the same way?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 28
    timed.caller(dummy, n, i, prob_id)
