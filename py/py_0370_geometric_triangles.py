# Solution of;
# Project Euler Problem 370: Geometric triangles
# https://projecteuler.net/problem=370
# 
# Let us define a geometric triangle as an integer sided triangle with sides a 
# ≤ b ≤ c so that its sides form a geometric progression, i. e. b2 = a · c . 
# An example of such a geometric triangle is the triangle with sides a = 144, 
# b = 156 and c = 169. There are 861805 geometric triangles with perimeter ≤ 
# 106 . How many geometric triangles exist with perimeter ≤ 2. 5·1013 ?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 370
    timed.caller(dummy, n, i, prob_id)
