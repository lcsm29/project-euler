# Solution of;
# Project Euler Problem 351: Hexagonal orchards
# https://projecteuler.net/problem=351
# 
# A hexagonal orchard of order n is a triangular lattice made up of points 
# within a regular hexagon with side n. The following is an example of a 
# hexagonal orchard of order 5:Highlighted in green are the points which are 
# hidden from the center by a point closer to it. It can be seen that for a 
# hexagonal orchard of order 5, 30 points are hidden from the center. Let H(n) 
# be the number of points hidden from the center in a hexagonal orchard of 
# order n. H(5) = 30. H(10) = 138. H(1 000) = 1177848. Find H(100 000 000).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 351
    timed.caller(dummy, n, i, prob_id)
