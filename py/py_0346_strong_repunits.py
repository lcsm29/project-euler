# Solution of;
# Project Euler Problem 346: Strong Repunits
# https://projecteuler.net/problem=346
# 
# The number 7 is special, because 7 is 111 written in base 2, and 11 written 
# in base 6 (i. e. 710 = 116 = 1112). In other words, 7 is a repunit in at 
# least two bases b > 1. We shall call a positive integer with this property a 
# strong repunit. It can be verified that there are 8 strong repunits below 
# 50: {1,7,13,15,21,31,40,43}. Furthermore, the sum of all strong repunits 
# below 1000 equals 15864. Find the sum of all strong repunits below 1012.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 346
    timed.caller(dummy, n, i, prob_id)
