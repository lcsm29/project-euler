# Solution of;
# Project Euler Problem 125: Palindromic sums
# https://projecteuler.net/problem=125
# 
# The palindromic number 595 is interesting because it can be written as the 
# sum of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 122. There are 
# exactly eleven palindromes below one-thousand that can be written as 
# consecutive square sums, and the sum of these palindromes is 4164. Note that 
# 1 = 02 + 12 has not been included as this problem is concerned with the 
# squares of positive integers. Find the sum of all the numbers less than 108 
# that are both palindromic and can be written as the sum of consecutive 
# squares.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 125
    timed.caller(dummy, n, i, prob_id)
