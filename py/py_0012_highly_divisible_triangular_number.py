# Solution of;
# Project Euler Problem 12: Highly divisible triangular number
# https://projecteuler.net/problem=12
# 
# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# Let us list the factors of the first seven triangle numbers: 
#        1: 1
#        3: 1, 3 
#        6: 1, 2, 3, 6
#       10: 1, 2, 5, 10
#       15: 1, 3, 5, 15
#       21: 1, 3, 7, 21
#       28: 1, 2, 4, 7, 14, 28
# 
# We can see that 28 is the first triangle number to have over 5 divisors.
# What is the value of the first triangle number to have over 500 divisors?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed
from math import sqrt
import random


def fn_brute_based_on_pfactor(n): # this one is also too slow but it's the best one atm
    assert n > 1, 'n should be greater than 1'
    assert type(n) == int, 'n should be an integer'

    def get_smallest_prime(num):
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return i
        return num

    def get_prime_factors(num):
        factors = []
        prime, divided = 2, num
        while prime <= divided:
            prime = get_smallest_prime(divided)
            if prime <= divided:
                divided //= prime
                factors.append(prime)
        return factors

    def count_divs(factors):
        count = 1
        for exp in [factors.count(exp) + 1 for exp in set(factors)]:
            count *= exp
        return count
    
    num_divs, triangle = 2, 1
    while num_divs <= n:
        triangle += (1+ int(sqrt(1 + (8 * triangle)))) // 2
        num_divs = count_divs(get_prime_factors(triangle))
    return triangle


if __name__ == '__main__':
    n = 500
    i = 6
    prob_id = 12
    timed.caller(fn_brute_based_on_pfactor, n, i, prob_id)
