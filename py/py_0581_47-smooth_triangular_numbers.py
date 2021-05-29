# Solution of;
# Project Euler Problem 581: 47-smooth triangular numbers
# https://projecteuler.net/problem=581
# 
# A number is p-smooth if it has no prime factors larger than p. Let T be the 
# sequence of triangular numbers, ie T(n)=n(n+1)/2. Find the sum of all 
# indices n such that T(n) is 47-smooth.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 581
    timed.caller(dummy, n, i, prob_id)
