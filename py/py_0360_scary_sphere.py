# Solution of;
# Project Euler Problem 360: Scary Sphere
# https://projecteuler.net/problem=360
# 
# Given two points (x1,y1,z1) and (x2,y2,z2) in three dimensional space, the 
# Manhattan distance between those points is defined as 
# |x1-x2|+|y1-y2|+|z1-z2|. Let C(r) be a sphere with radius r and center in 
# the origin O(0,0,0). Let I(r) be the set of all points with integer 
# coordinates on the surface of C(r). Let S(r) be the sum of the Manhattan 
# distances of all elements of I(r) to the origin O. E. g. S(45)=34518. Find 
# S(1010).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 360
    timed.caller(dummy, n, i, prob_id)
