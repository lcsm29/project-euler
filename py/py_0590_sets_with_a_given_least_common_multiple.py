# Solution of;
# Project Euler Problem 590: Sets with a given Least Common Multiple
# https://projecteuler.net/problem=590
# 
# Let H(n) denote the number of sets of positive integers such that the least 
# common multiple of the integers in the set equals n. E. g. :The integers in 
# the following ten sets all have a least common multiple of 6:{2,3}, {1,2,3}, 
# {6}, {1,6}, {2,6} ,{1,2,6}, {3,6}, {1,3,6}, {2,3,6} and {1,2,3,6}. Thus 
# H(6)=10. Let L(n) denote the least common multiple of the numbers 1 through 
# n. E. g. L(6) is the least common multiple of the numbers 1,2,3,4,5,6 and 
# L(6) equals 60. Let HL(n) denote H(L(n)). You are given HL(4)=H(12)=44. Find 
# HL(50000). Give your answer modulo 109.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 590
    timed.caller(dummy, n, i, prob_id)
