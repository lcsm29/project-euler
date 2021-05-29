# Solution of;
# Project Euler Problem 701: Random connected area
# https://projecteuler.net/problem=701
# 
# Consider a rectangle made up of $W \times H$ square cells each with area 1. 
# Each cell is independently coloured black with probability 0. 5 otherwise 
# white. Black cells sharing an edge are assumed to be connected. Consider the 
# maximum area of connected cells. Define $E(W,H)$ to be the expected value of 
# this maximum area. For example, $E(2,2)=1. 875$, as illustrated below. You 
# are also given $E(4, 4) = 5. 76487732$, rounded to 8 decimal places. Find 
# $E(7, 7)$, rounded to 8 decimal places.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 701
    timed.caller(dummy, n, i, prob_id)
