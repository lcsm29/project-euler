# Solution of;
# Project Euler Problem 110: Diophantine reciprocals II
# https://projecteuler.net/problem=110
# 
# In the following equation x, y, and n are positive integers. $$\dfrac{1}{x} 
# + \dfrac{1}{y} = \dfrac{1}{n}$$It can be verified that when $n = 1260$ there 
# are 113 distinct solutions and this is the least value of $n$ for which the 
# total number of distinct solutions exceeds one hundred. What is the least 
# value of $n$ for which the number of distinct solutions exceeds four 
# million?NOTE: This problem is a much more difficult version of Problem 108 
# and as it is well beyond the limitations of a brute force approach it 
# requires a clever implementation.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 110
    timed.caller(dummy, n, i, prob_id)
