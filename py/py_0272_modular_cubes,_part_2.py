# Solution of;
# Project Euler Problem 272: Modular Cubes, part 2
# https://projecteuler.net/problem=272
# 
# For a positive number n, define C(n) as the number of the integers x, for 
# which 1<x<n andx3≡1 mod n. When n=91, there are 8 possible values for x, 
# namely : 9, 16, 22, 29, 53, 74, 79, 81. Thus, C(91)=8. Find the sum of the 
# positive numbers n≤1011 for which C(n)=242.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 272
    timed.caller(dummy, n, i, prob_id)
