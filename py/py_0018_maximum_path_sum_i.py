# Solution of;
# Project Euler Problem 18: Maximum path sum I
# https://projecteuler.net/problem=18
# 
# By starting at the top of the triangle below and moving to adjacent numbers 
# on the row below, the maximum total from top to bottom is 23. 37 42 4 68 5 9 
# 3That is, 3 + 7 + 4 + 9 = 23. Find the maximum total from top to bottom of 
# the triangle below:7595 6417 47 8218 35 87 1020 04 82 47 6519 01 23 75 03 
# 3488 02 77 73 07 63 6799 65 04 28 06 16 70 9241 41 26 56 83 40 80 70 3341 48 
# 72 33 47 32 37 16 94 2953 71 44 65 25 43 91 52 97 51 1470 11 33 28 77 73 17 
# 78 39 68 17 5791 71 52 38 17 14 91 43 58 50 27 29 4863 66 04 68 89 53 67 30 
# 73 16 69 87 40 3104 62 98 27 23 09 70 98 73 93 38 53 60 04 23NOTE: As there 
# are only 16384 routes, it is possible to solve this problem by trying every 
# route. However, Problem 67, is the same challenge with a triangle containing 
# one-hundred rows; it cannot be solved by brute force, and requires a clever 
# method! ;o)
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 18
    timed.caller(dummy, n, i, prob_id)
