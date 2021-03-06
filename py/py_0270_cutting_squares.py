# Solution of;
# Project Euler Problem 270: Cutting Squares
# https://projecteuler.net/problem=270
# 
# A square piece of paper with integer dimensions N×N is placed with a corner 
# at the origin and two of its sides along the x- and y-axes. Then, we cut it 
# up respecting the following rules:We only make straight cuts between two 
# points lying on different sides of the square, and having integer 
# coordinates. Two cuts cannot cross, but several cuts can meet at the same 
# border point. Proceed until no more legal cuts can be made. Counting any 
# reflections or rotations as distinct, we call C(N) the number of ways to cut 
# an N×N square. For example, C(1) = 2 and C(2) = 30 (shown below). What is 
# C(30) mod 108 ?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 270
    timed.caller(dummy, n, i, prob_id)
