# Solution of;
# Project Euler Problem 62: Cubic permutations
# https://projecteuler.net/problem=62
# 
# The cube, 41063625 (3453), can be permuted to produce two other cubes: 
# 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube 
# which has exactly three permutations of its digits which are also cube. Find 
# the smallest cube for which exactly five permutations of its digits are 
# cube.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 62
    timed.caller(dummy, n, i, prob_id)
