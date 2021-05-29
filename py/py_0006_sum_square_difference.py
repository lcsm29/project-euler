# Solution of;
# Project Euler Problem 6: Sum square difference
# https://projecteuler.net/problem=6
# 
# The sum of the squares of the first ten natural numbers is,$$1^2 + 2^2 + . . 
# . + 10^2 = 385$$The square of the sum of the first ten natural numbers 
# is,$$(1 + 2 + . . . + 10)^2 = 55^2 = 3025$$Hence the difference between the 
# sum of the squares of the first ten natural numbers and the square of the 
# sum is $3025 - 385 = 2640$. Find the difference between the sum of the 
# squares of the first one hundred natural numbers and the square of the sum.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 6
    timed.caller(dummy, n, i, prob_id)
