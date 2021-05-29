# Solution of;
# Project Euler Problem 486: Palindrome-containing strings
# https://projecteuler.net/problem=486
# 
# Let F5(n) be the number of strings s such that:s consists only of '0's and 
# '1's,s has length at most n, ands contains a palindromic substring of length 
# at least 5. For example, F5(4) = 0, F5(5) = 8, F5(6) = 42 and F5(11) = 3844. 
# Let D(L) be the number of integers n such that 5 ≤ n ≤ L and F5(n) is 
# divisible by 87654321. For example, D(107) = 0 and D(5·109) = 51. Find 
# D(1018).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 486
    timed.caller(dummy, n, i, prob_id)
