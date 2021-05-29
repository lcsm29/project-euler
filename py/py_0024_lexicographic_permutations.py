# Solution of;
# Project Euler Problem 24: Lexicographic permutations
# https://projecteuler.net/problem=24
# 
# A permutation is an ordered arrangement of objects. For example, 3124 is one 
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations 
# are listed numerically or alphabetically, we call it lexicographic order. 
# The lexicographic permutations of 0, 1 and 2 are:012 021 102 120 201 210What 
# is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 
# 6, 7, 8 and 9?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 24
    timed.caller(dummy, n, i, prob_id)
