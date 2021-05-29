# Solution of;
# Project Euler Problem 166: Criss Cross
# https://projecteuler.net/problem=166
# 
# A 4x4 grid is filled with digits d, 0 ≤ d ≤ 9. It can be seen that in the 
# grid6 3 3 05 0 4 30 7 1 41 2 4 5the sum of each row and each column has the 
# value 12. Moreover the sum of each diagonal is also 12. In how many ways can 
# you fill a 4x4 grid with the digits d, 0 ≤ d ≤ 9 so that each row, each 
# column, and both diagonals have the same sum?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 166
    timed.caller(dummy, n, i, prob_id)
