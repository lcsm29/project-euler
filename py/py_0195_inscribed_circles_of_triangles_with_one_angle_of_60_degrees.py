# Solution of;
# Project Euler Problem 195: Inscribed circles of triangles with one angle of 60 degrees
# https://projecteuler.net/problem=195
# 
# Let's call an integer sided triangle with exactly one angle of 60 degrees a 
# 60-degree triangle. Let r be the radius of the inscribed circle of such a 
# 60-degree triangle. There are 1234 60-degree triangles for which r ≤ 100. 
# Let T(n) be the number of 60-degree triangles for which r ≤ n, so T(100) = 
# 1234, T(1000) = 22767, and T(10000) = 359912. Find T(1053779).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 195
    timed.caller(dummy, n, i, prob_id)