# Solution of;
# Project Euler Problem 582: Nearly isosceles 120 degree triangles
# https://projecteuler.net/problem=582
# 
# Let a, b and c be the sides of an integer sided triangle with one angle of 
# 120 degrees, a≤b≤c and b-a≤100. Let T(n) be the number of such triangles 
# with c≤n. T(1000)=235 and T(108)=1245. Find T(10100).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 582
    timed.caller(dummy, n, i, prob_id)
