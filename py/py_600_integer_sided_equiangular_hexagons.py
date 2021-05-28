# Solution of;
# Project Euler Problem 600: Integer sided equiangular hexagons
# https://projecteuler.net/problem=600
# 
# Let H(n) be the number of distinct integer sided equiangular convex hexagons 
# with perimeter not exceeding n. Hexagons are distinct if and only if they 
# are not congruent. You are given H(6) = 1, H(12) = 10, H(100) = 31248. Find 
# H(55106). Equiangular hexagons with perimeter not exceeding 12
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
