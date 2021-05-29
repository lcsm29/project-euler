# Solution of;
# Project Euler Problem 355: Maximal coprime subset
# https://projecteuler.net/problem=355
# 
# Define Co(n) to be the maximal possible sum of a set of mutually co-prime 
# elements from {1, 2, . . . , n}. For example Co(10) is 30 and hits that 
# maximum on the subset {1, 5, 7, 8, 9}. You are given that Co(30) = 193 and 
# Co(100) = 1356. Find Co(200000).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 355
    timed.caller(dummy, n, i, prob_id)
