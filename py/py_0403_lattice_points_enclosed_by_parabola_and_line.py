# Solution of;
# Project Euler Problem 403: Lattice points enclosed by parabola and line
# https://projecteuler.net/problem=403
# 
# For integers a and b, we define D(a, b) as the domain enclosed by the 
# parabola y = x2 and the line y = a·x + b:D(a, b) = { (x, y) | x2 ≤ y ≤ a·x + 
# b }. L(a, b) is defined as the number of lattice points contained in D(a, 
# b). For example, L(1, 2) = 8 and L(2, -1) = 1. We also define S(N) as the 
# sum of L(a, b) for all the pairs (a, b) such that the area of D(a, b) is a 
# rational number and |a|,|b| ≤ N. We can verify that S(5) = 344 and S(100) = 
# 26709528. Find S(1012). Give your answer mod 108.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 403
    timed.caller(dummy, n, i, prob_id)
