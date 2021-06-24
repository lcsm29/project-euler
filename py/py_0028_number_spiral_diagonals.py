# Solution of;
# Project Euler Problem 28: Number spiral diagonals
# https://projecteuler.net/problem=28
# 
# Starting with the number 1 and moving to the right 
# in a clockwise direction a 5 by 5 spiral is formed as follows:
#
#   21 22 23 24 25
#   20  7  8  9 10
#   19  6  1  2 11
#   18  5  4  3 12
#   17 16 15 14 13
# 
# It can be verified that the sum of the numbers on the diagonals is 101. 
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
# formed in the same way?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def fn_short(n):
    return sum(i**2 + (i**2 - 2*(i-1))*3 for i in range(1, n + 1, 2)) - 3


if __name__ == '__main__':
    n = 1_001
    i = 4_500
    prob_id = 28
    timed.caller(fn_short, n, i, prob_id)
