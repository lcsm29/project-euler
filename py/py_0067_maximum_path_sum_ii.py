# Solution of;
# Project Euler Problem 67: Maximum path sum II
# https://projecteuler.net/problem=67
# 
# By starting at the top of the triangle below and moving to adjacent numbers 
# on the row below, the maximum total from top to bottom is 23. 37 42 4 68 5 9 
# 3That is, 3 + 7 + 4 + 9 = 23. Find the maximum total from top to bottom in 
# triangle. txt (right click and 'Save Link/Target As. . . '), a 15K text file 
# containing a triangle with one-hundred rows. NOTE: This is a much more 
# difficult version of Problem 18. It is not possible to try every route to 
# solve this problem, as there are 299 altogether! If you could check one 
# trillion (1012) routes every second it would take over twenty billion years 
# to check them all. There is an efficient algorithm to solve it. ;o)
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 67
    timed.caller(dummy, n, i, prob_id)
