# Solution of;
# Project Euler Problem 188: The hyperexponentiation of a number
# https://projecteuler.net/problem=188
# 
# The hyperexponentiation or tetration of a number a by a positive integer b, 
# denoted by a↑↑b or ba, is recursively defined by:a↑↑1 = a,a↑↑(k+1) = 
# a(a↑↑k). Thus we have e. g. 3↑↑2 = 33 = 27, hence 3↑↑3 = 327 = 7625597484987 
# and 3↑↑4 is roughly 103. 6383346400240996*10^12. Find the last 8 digits of 
# 1777↑↑1855.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 188
    timed.caller(dummy, n, i, prob_id)
