# Solution of;
# Project Euler Problem 154: Exploring Pascal's pyramid
# https://projecteuler.net/problem=154
# 
# A triangular pyramid is constructed using spherical balls so that each ball 
# rests on exactly three balls of the next lower level. Then, we calculate the 
# number of paths leading from the apex to each position:A path starts at the 
# apex and progresses downwards to any of the three spheres directly below the 
# current position. Consequently, the number of paths to reach a certain 
# position is the sum of the numbers immediately above it (depending on the 
# position, there are up to three numbers above it). The result is Pascal's 
# pyramid and the numbers at each level n are the coefficients of the 
# trinomial expansion (x + y + z)n. How many coefficients in the expansion of 
# (x + y + z)200000 are multiples of 1012?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 154
    timed.caller(dummy, n, i, prob_id)
