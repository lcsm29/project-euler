# Solution of;
# Project Euler Problem 204: Generalised Hamming Numbers
# https://projecteuler.net/problem=204
# 
# A Hamming number is a positive number which has no prime factor larger than 
# 5. So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15. 
# There are 1105 Hamming numbers not exceeding 108. We will call a positive 
# number a generalised Hamming number of type n, if it has no prime factor 
# larger than n. Hence the Hamming numbers are the generalised Hamming numbers 
# of type 5. How many generalised Hamming numbers of type 100 are there which 
# don't exceed 109?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 204
    timed.caller(dummy, n, i, prob_id)
