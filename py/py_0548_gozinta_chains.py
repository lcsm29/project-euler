# Solution of;
# Project Euler Problem 548: Gozinta Chains
# https://projecteuler.net/problem=548
# 
# A gozinta chain for n is a sequence {1,a,b,. . . ,n} where each element 
# properly divides the next. There are eight gozinta chains for 12:{1,12} 
# ,{1,2,12}, {1,2,4,12}, {1,2,6,12}, {1,3,12}, {1,3,6,12}, {1,4,12} and 
# {1,6,12}. Let g(n) be the number of gozinta chains for n, so g(12)=8. 
# g(48)=48 and g(120)=132. Find the sum of the numbers n not exceeding 1016 
# for which g(n)=n.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 548
    timed.caller(dummy, n, i, prob_id)
