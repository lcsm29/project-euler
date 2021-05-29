# Solution of;
# Project Euler Problem 3: Largest prime factor
# https://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#
# by lcsm29 http://github.com/lcsm29/project-euler
import timed
from math import sqrt


def fn_smallest_prime_division(n):
    def smallest_prime(num):
        smallest = float('inf')
        for i in range(2, int(sqrt(n)) + 2):
            if num % i == 0:
                return min(smallest, i)
        return num
    prime, divided = 2, n
    while prime < divided:
        prime = smallest_prime(divided)
        if prime < divided:
            divided //= prime
    return divided


def fn_sprime_div_wo_def(n):
    i, divided = 2, n
    while i ** 2 <= divided:
        if divided % i:
            i += 1
        else:
            divided //= i
    return divided


if __name__ == '__main__':
    n = 600_851_475_143
    i = 1_500
    prob_id = 3
    timed.caller(fn_smallest_prime_division, n, i, prob_id)
    timed.caller(fn_sprime_div_wo_def, n, i, prob_id)
