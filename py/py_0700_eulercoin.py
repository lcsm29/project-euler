# Solution of;
# Project Euler Problem 700: Eulercoin
# https://projecteuler.net/problem=700
# 
# Leonhard Euler was born on 15 April 1707. Consider the sequence 
# 1504170715041707n mod 4503599627370517. An element of this sequence is 
# defined to be an Eulercoin if it is strictly smaller than all previously 
# found Eulercoins. For example, the first term is 1504170715041707 which is 
# the first Eulercoin. The second term is 3008341430083414 which is greater 
# than 1504170715041707 so is not an Eulercoin. However, the third term is 
# 8912517754604 which is small enough to be a new Eulercoin. The sum of the 
# first 2 Eulercoins is therefore 1513083232796311. Find the sum of all 
# Eulercoins.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 700
    timed.caller(dummy, n, i, prob_id)
