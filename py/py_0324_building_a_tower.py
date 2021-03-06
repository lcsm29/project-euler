# Solution of;
# Project Euler Problem 324: Building a tower
# https://projecteuler.net/problem=324
# 
# Let f(n) represent the number of ways one can fill a 3×3×n tower with blocks 
# of 2×1×1. You're allowed to rotate the blocks in any way you like; however, 
# rotations, reflections etc of the tower itself are counted as distinct. For 
# example (with q = 100000007) :f(2) = 229,f(4) = 117805,f(10) mod q = 
# 96149360,f(103) mod q = 24806056,f(106) mod q = 30808124. Find f(1010000) 
# mod 100000007.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 324
    timed.caller(dummy, n, i, prob_id)
