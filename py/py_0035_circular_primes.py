# Solution of;
# Project Euler Problem 35: Circular primes
# https://projecteuler.net/problem=35
# 
# The number, 197, is called a circular prime because all rotations of the 
# digits: 197, 971, and 719, are themselves prime. There are thirteen such 
# primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97. How 
# many circular primes are there below one million?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 35
    timed.caller(dummy, n, i, prob_id)
