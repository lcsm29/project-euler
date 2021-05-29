# Solution of;
# Project Euler Problem 342: The totient of a square is a cube
# https://projecteuler.net/problem=342
# 
# Consider the number 50. 502 = 2500 = 22 × 54, so φ(2500) = 2 × 4 × 53 = 8 × 
# 53 = 23 × 53. 1So 2500 is a square and φ(2500) is a cube. Find the sum of 
# all numbers n, 1 < n < 1010 such that φ(n2) is a cube. 1 φ denotes Euler's 
# totient function.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 342
    timed.caller(dummy, n, i, prob_id)
