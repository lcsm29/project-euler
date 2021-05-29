# Solution of;
# Project Euler Problem 250: 250250
# https://projecteuler.net/problem=250
# 
# Find the number of non-empty subsets of {11, 22, 33,. . . , 250250250250}, 
# the sum of whose elements is divisible by 250. Enter the rightmost 16 digits 
# as your answer.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 250
    timed.caller(dummy, n, i, prob_id)
