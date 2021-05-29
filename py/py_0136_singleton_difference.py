# Solution of;
# Project Euler Problem 136: Singleton difference
# https://projecteuler.net/problem=136
# 
# The positive integers, x, y, and z, are consecutive terms of an arithmetic 
# progression. Given that n is a positive integer, the equation, x2 − y2 − z2 
# = n, has exactly one solution when n = 20:132 − 102 − 72 = 20In fact there 
# are twenty-five values of n below one hundred for which the equation has a 
# unique solution. How many values of n less than fifty million have exactly 
# one solution?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 136
    timed.caller(dummy, n, i, prob_id)
