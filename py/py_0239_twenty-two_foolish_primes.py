# Solution of;
# Project Euler Problem 239: Twenty-two Foolish Primes
# https://projecteuler.net/problem=239
# 
# A set of disks numbered 1 through 100 are placed in a line in random order. 
# What is the probability that we have a partial derangement such that exactly 
# 22 prime number discs are found away from their natural positions?(Any 
# number of non-prime disks may also be found in or out of their natural 
# positions. )Give your answer rounded to 12 places behind the decimal point 
# in the form 0. abcdefghijkl.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 239
    timed.caller(dummy, n, i, prob_id)
