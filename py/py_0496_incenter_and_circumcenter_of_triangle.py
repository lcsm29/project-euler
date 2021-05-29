# Solution of;
# Project Euler Problem 496: Incenter and circumcenter of triangle
# https://projecteuler.net/problem=496
# 
# Given an integer sided triangle ABC:Let I be the incenter of ABC. Let D be 
# the intersection between the line AI and the circumcircle of ABC (A ≠ D). We 
# define F(L) as the sum of BC for the triangles ABC that satisfy AC = DI and 
# BC ≤ L. For example, F(15) = 45 because the triangles ABC with (BC,AC,AB) = 
# (6,4,5), (12,8,10), (12,9,7), (15,9,16) satisfy the conditions. Find F(109).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 496
    timed.caller(dummy, n, i, prob_id)
