# Solution of;
# Project Euler Problem 176: Right-angled triangles that share a cathetus
# https://projecteuler.net/problem=176
# 
# The four right-angled triangles with sides (9,12,15), (12,16,20), (5,12,13) 
# and (12,35,37) all have one of the shorter sides (catheti) equal to 12. It 
# can be shown that no other integer sided right-angled triangle exists with 
# one of the catheti equal to 12. Find the smallest integer that can be the 
# length of a cathetus of exactly 47547 different integer sided right-angled 
# triangles.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 176
    timed.caller(dummy, n, i, prob_id)
