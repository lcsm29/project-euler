# Solution of;
# Project Euler Problem 518: Prime triples and geometric sequences
# https://projecteuler.net/problem=518
# 
# Let S(n) = Σ a+b+c over all triples (a,b,c) such that:a, b, and c are prime 
# numbers. a < b < c < n. a+1, b+1, and c+1 form a geometric sequence. For 
# example, S(100) = 1035 with the following triples: (2, 5, 11), (2, 11, 47), 
# (5, 11, 23), (5, 17, 53), (7, 11, 17), (7, 23, 71), (11, 23, 47), (17, 23, 
# 31), (17, 41, 97), (31, 47, 71), (71, 83, 97)Find S(108).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 518
    timed.caller(dummy, n, i, prob_id)
