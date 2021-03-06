# Solution of;
# Project Euler Problem 70: Totient permutation
# https://projecteuler.net/problem=70
# 
# Euler's Totient function, φ(n) [sometimes called the phi function], is used 
# to determine the number of positive numbers less than or equal to n which 
# are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all 
# less than nine and relatively prime to nine, φ(9)=6. The number 1 is 
# considered to be relatively prime to every positive number, so φ(1)=1. 
# Interestingly, φ(87109)=79180, and it can be seen that 87109 is a 
# permutation of 79180. Find the value of n, 1 < n < 107, for which φ(n) is a 
# permutation of n and the ratio n/φ(n) produces a minimum.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 70
    timed.caller(dummy, n, i, prob_id)
