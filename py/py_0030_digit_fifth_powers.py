# Solution of;
# Project Euler Problem 30: Digit fifth powers
# https://projecteuler.net/problem=30
# 
# Surprisingly there are only three numbers that can be written as 
# the sum of fourth powers of their digits:
# 
#   1634 = 1^4 + 6^4 + 3^4 + 4^4
#   8208 = 8^4 + 2^4 + 0^4 + 8^4
#   9474 = 9^4 + 4^4 + 7^4 + 4^4
# 
# As 1 = 1^4 is not a sum it is not included. The sum of these numbers is 
# 1634 + 8208 + 9474 = 19316. Find the sum of all the numbers that can be
# written as the sum of fifth powers of their digits.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def fn_brute(n):
    limit = 1
    while len(str(9**n * limit)) >= limit:
        limit += 1
    limit *= 9**n + 1
    return sum([i for i in range(2, limit)
        if sum([int(digit) ** n for digit in str(i)]) == i])


if __name__ == '__main__':
    n = 5
    i = 1
    prob_id = 30
    timed.caller(fn_brute, n, i, prob_id)
