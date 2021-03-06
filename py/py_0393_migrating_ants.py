# Solution of;
# Project Euler Problem 393: Migrating ants
# https://projecteuler.net/problem=393
# 
# An n×n grid of squares contains n2 ants, one ant per square. All ants decide 
# to move simultaneously to an adjacent square (usually 4 possibilities, 
# except for ants on the edge of the grid or at the corners). We define f(n) 
# to be the number of ways this can happen without any ants ending on the same 
# square and without any two ants crossing the same edge between two squares. 
# You are given that f(4) = 88. Find f(10).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 393
    timed.caller(dummy, n, i, prob_id)
