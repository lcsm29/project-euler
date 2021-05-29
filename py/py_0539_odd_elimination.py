# Solution of;
# Project Euler Problem 539: Odd elimination
# https://projecteuler.net/problem=539
# 
# Start from an ordered list of all integers from 1 to n. Going from left to 
# right, remove the first number and every other number afterward until the 
# end of the list. Repeat the procedure from right to left, removing the right 
# most number and every other number from the numbers left. Continue removing 
# every other numbers, alternating left to right and right to left, until a 
# single number remains. Starting with n = 9, we have:1 2 3 4 5 6 7 8 92 4 6 
# 82 66Let P(n) be the last number left starting with a list of length n. Let 
# $\displaystyle S(n) = \sum_{k=1}^n P(k)$. You are given P(1)=1, P(9) = 6, 
# P(1000)=510, S(1000)=268271. Find S(1018) mod 987654321.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 539
    timed.caller(dummy, n, i, prob_id)
