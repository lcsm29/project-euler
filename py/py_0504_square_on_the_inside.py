# Solution of;
# Project Euler Problem 504: Square on the Inside
# https://projecteuler.net/problem=504
# 
# Let ABCD be a quadrilateral whose vertices are lattice points lying on the 
# coordinate axes as follows:A(a, 0), B(0, b), C(−c, 0), D(0, −d), where 1 ≤ 
# a, b, c, d ≤ m and a, b, c, d, m are integers. It can be shown that for m = 
# 4 there are exactly 256 valid ways to construct ABCD. Of these 256 
# quadrilaterals, 42 of them strictly contain a square number of lattice 
# points. How many quadrilaterals ABCD strictly contain a square number of 
# lattice points for m = 100?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 504
    timed.caller(dummy, n, i, prob_id)
