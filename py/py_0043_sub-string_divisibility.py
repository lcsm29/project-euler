# Solution of;
# Project Euler Problem 43: Sub-string divisibility
# https://projecteuler.net/problem=43
# 
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up 
# of each of the digits 0 to 9 in some order, but it also has a rather 
# interesting sub-string divisibility property. Let d1 be the 1st digit, d2 be 
# the 2nd digit, and so on. In this way, we note the following:d2d3d4=406 is 
# divisible by 2d3d4d5=063 is divisible by 3d4d5d6=635 is divisible by 
# 5d5d6d7=357 is divisible by 7d6d7d8=572 is divisible by 11d7d8d9=728 is 
# divisible by 13d8d9d10=289 is divisible by 17Find the sum of all 0 to 9 
# pandigital numbers with this property.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 43
    timed.caller(dummy, n, i, prob_id)
