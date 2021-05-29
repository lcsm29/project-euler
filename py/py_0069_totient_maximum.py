# Solution of;
# Project Euler Problem 69: Totient maximum
# https://projecteuler.net/problem=69
# 
# Euler's Totient function, φ(n) [sometimes called the phi function], is used 
# to determine the number of numbers less than n which are relatively prime to 
# n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and 
# relatively prime to nine, φ(9)=6. nRelatively Primeφ(n)n/φ(n)211231,221. 
# 541,32251,2,3,441. 2561,52371,2,3,4,5,661. 1666. . . 
# 81,3,5,74291,2,4,5,7,861. 5101,3,7,942. 5It can be seen that n=6 produces a 
# maximum n/φ(n) for n ≤ 10. Find the value of n ≤ 1,000,000 for which n/φ(n) 
# is a maximum.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 69
    timed.caller(dummy, n, i, prob_id)
