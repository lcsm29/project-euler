# Solution of;
# Project Euler Problem 455: Powers With Trailing Digits
# https://projecteuler.net/problem=455
# 
# Let f(n) be the largest positive integer x less than 109 such that the last 
# 9 digits of nx form the number x (including leading zeros), or zero if no 
# such integer exists. For example:f(4) = 411728896 (4411728896 = . . . 
# 490411728896) f(10) = 0f(157) = 743757 (157743757 = . . . 567000743757)∑ 
# f(n), 2 ≤ n ≤ 103 = 442530011399Find ∑ f(n), 2 ≤ n ≤ 106.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 455
    timed.caller(dummy, n, i, prob_id)
