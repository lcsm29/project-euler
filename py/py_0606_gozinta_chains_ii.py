# Solution of;
# Project Euler Problem 606: Gozinta Chains II
# https://projecteuler.net/problem=606
# 
# A gozinta chain for n is a sequence {1,a,b,. . . ,n} where each element 
# properly divides the next. For example, there are eight distinct gozinta 
# chains for 12: {1,12}, {1,2,12}, {1,2,4,12}, {1,2,6,12}, {1,3,12}, 
# {1,3,6,12}, {1,4,12} and {1,6,12}. Let S(n) be the sum of all numbers, k, 
# not exceeding n, which have 252 distinct gozinta chains. You are given 
# S(106)=8462952 and S(1012)=623291998881978. Find S(1036), giving the last 
# nine digits of your answer.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 606
    timed.caller(dummy, n, i, prob_id)
