# Solution of;
# Project Euler Problem 386: Maximum length of an antichain
# https://projecteuler.net/problem=386
# 
# Let n be an integer and S(n) be the set of factors of n. A subset A of S(n) 
# is called an antichain of S(n) if A contains only one element or if none of 
# the elements of A divides any of the other elements of A. For example: S(30) 
# = {1, 2, 3, 5, 6, 10, 15, 30}{2, 5, 6} is not an antichain of S(30). {2, 3, 
# 5} is an antichain of S(30). Let N(n) be the maximum length of an antichain 
# of S(n). Find ∑ N(n) for 1 ≤ n ≤ 108
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 386
    timed.caller(dummy, n, i, prob_id)
