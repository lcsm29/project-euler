# Solution of;
# Project Euler Problem 15: Lattice paths
# https://projecteuler.net/problem=15
# 
# Starting in the top left corner of a 2×2 grid, and only being able to move 
# to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def fn_combination(n):
    dividend = 1
    for i in range(n[0] + n[1], n[1], -1):
        dividend *= i
    divisor = 1
    for i in range(n[1], 1, -1):
        divisor *= i
    return dividend // divisor


if __name__ == '__main__':
    n = (20, 20)
    i = 450_000
    prob_id = 15
    timed.caller(fn_combination, n, i, prob_id)
