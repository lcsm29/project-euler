# Solution of;
# Project Euler Problem 93: Arithmetic expressions
# https://projecteuler.net/problem=93
# 
# By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and 
# making use of the four arithmetic operations (+, −, *, /) and 
# brackets/parentheses, it is possible to form different positive integer 
# targets. For example,8 = (4 * (1 + 3)) / 214 = 4 * (3 + 1 / 2)19 = 4 * (2 + 
# 3) − 136 = 3 * 4 * (2 + 1)Note that concatenations of the digits, like 12 + 
# 34, are not allowed. Using the set, {1, 2, 3, 4}, it is possible to obtain 
# thirty-one different target numbers of which 36 is the maximum, and each of 
# the numbers 1 to 28 can be obtained before encountering the first 
# non-expressible number. Find the set of four distinct digits, a < b < c < d, 
# for which the longest set of consecutive positive integers, 1 to n, can be 
# obtained, giving your answer as a string: abcd.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 93
    timed.caller(dummy, n, i, prob_id)
