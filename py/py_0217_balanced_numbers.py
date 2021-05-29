# Solution of;
# Project Euler Problem 217: Balanced Numbers
# https://projecteuler.net/problem=217
# 
# A positive integer with k (decimal) digits is called balanced if its first 
# ⌈k/2⌉ digits sum to the same value as its last ⌈k/2⌉ digits, where ⌈x⌉, 
# pronounced ceiling of x, is the smallest integer ≥ x, thus ⌈π⌉ = 4 and ⌈5⌉ = 
# 5. So, for example, all palindromes are balanced, as is 13722. Let T(n) be 
# the sum of all balanced numbers less than 10n. Thus: T(1) = 45, T(2) = 540 
# and T(5) = 334795890. Find T(47) mod 315
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 217
    timed.caller(dummy, n, i, prob_id)
