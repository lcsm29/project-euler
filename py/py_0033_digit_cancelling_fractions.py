# Solution of;
# Project Euler Problem 33: Digit cancelling fractions
# https://projecteuler.net/problem=33
# 
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which 
# is correct, is obtained by cancelling the 9s. We shall consider fractions 
# like, 30/50 = 3/5, to be trivial examples. There are exactly four 
# non-trivial examples of this type of fraction, less than one in value, and 
# containing two digits in the numerator and denominator. If the product of 
# these four fractions is given in its lowest common terms, find the value of 
# the denominator.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 33
    timed.caller(dummy, n, i, prob_id)
