# Solution of;
# Project Euler Problem 466: Distinct terms in a multiplication table
# https://projecteuler.net/problem=466
# 
# Let P(m,n) be the number of distinct terms in an m×n multiplication table. 
# For example, a 3×4 multiplication table looks like this:× 12341 12342 24683 
# 36912There are 8 distinct terms {1,2,3,4,6,8,9,12}, therefore P(3,4) = 8. 
# You are given that:P(64,64) = 1263,P(12,345) = 1998, andP(32,1015) = 
# 13826382602124302. Find P(64,1016).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 466
    timed.caller(dummy, n, i, prob_id)
