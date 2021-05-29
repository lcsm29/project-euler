# Solution of;
# Project Euler Problem 529: 10-substrings
# https://projecteuler.net/problem=529
# 
# A 10-substring of a number is a substring of its digits that sum to 10. For 
# example, the 10-substrings of the number 3523014 
# are:3523014352301435230143523014A number is called 10-substring-friendly if 
# every one of its digits belongs to a 10-substring. For example, 3523014 is 
# 10-substring-friendly, but 28546 is not. Let T(n) be the number of 
# 10-substring-friendly numbers from 1 to 10n (inclusive). For example T(2) = 
# 9 and T(5) = 3492. Find T(1018) mod 1 000 000 007.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 529
    timed.caller(dummy, n, i, prob_id)
