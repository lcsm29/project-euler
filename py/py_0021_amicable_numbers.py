# Solution of;
# Project Euler Problem 21: Amicable numbers
# https://projecteuler.net/problem=21
# 
# Let d(n) be defined as the sum of proper divisors of n 
# (numbers less than n which divide evenly into n). 
# 
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220. 
# 
# Evaluate the sum of all the amicable numbers under 10000.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed
from math import sqrt


def fn_brute_based_on_pfactor(n):
    assert n > 1, 'n should be greater than 1'
    assert type(n) == int, 'n should be an integer'

    def get_smallest_prime(num):
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0: return i
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
    
    def get_combs(factors_lst):
        if len(factors_lst) == 0:
            return [[]]
        combinations = []
        for c in get_combs(factors_lst[1:]):
            combinations += [c, c + [factors_lst[0]]]
        return combinations

    def get_divisors(num, combs_lst):
        dup_removed = []
        for l in combs_lst[1:]:
            if l not in dup_removed:
                dup_removed.append(l)
        divisors = [1]
        for l in dup_removed:
            prd = 1
            for elem in l:
                prd *= elem
            if prd != num:
                divisors.append(prd)
        return divisors

    a_dct = {i: sum(get_divisors(i, get_combs(get_prime_factors(i))))
                for i in range(2, n)}
    amicables = [k for k, v in a_dct.items() 
                    if 2 < v < n and k != v and k == a_dct[v]]
    return sum(amicables)


if __name__ == '__main__':
    n = 10_000
    i = 10
    prob_id = 21
    timed.caller(fn_brute_based_on_pfactor, n, i, prob_id)
