# Solution of;
# Project Euler Problem 23: Non-abundant sums
# https://projecteuler.net/problem=23
# 
# A perfect number is a number for which the sum of its proper divisors 
# is exactly equal to the number. For example, the sum of the proper divisors 
# of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 
# 28 is a perfect number. 
# 
# A number n is called deficient if the sum of its proper divisors is less 
# than n and it is called abundant if this sum exceeds n. 
# 
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
# number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 
# 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis 
# even though it is known that the greatest number that cannot be expressed 
# as the sum of two abundant numbers is less than this limit. 
# 
# Find the sum of all the positive integers which cannot be written as 
# the sum of two abundant numbers.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed
from math import sqrt


def fn_brute(n):
    def get_pfactors(num):
        def get_smallest_prime(num):
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0: return i
            return num
        factors = []
        prime, divided = 2, num
        while prime <= divided:
            prime = get_smallest_prime(divided)
            if prime <= divided:
                divided //= prime
                factors.append(prime)
        return factors
    
    def get_combs(factors_lst):
        def combs(factors_lst):
            if len(factors_lst) == 0:
                return [[]]
            combinations = []
            for c in combs(factors_lst[1:]):
                combinations += [c, c + [factors_lst[0]]]
            return combinations
        dirty_lst = combs(factors_lst)[1:]
        clean_lst = []
        for lst in dirty_lst:
            if lst not in clean_lst:
                clean_lst.append(lst)
        return clean_lst

    def get_divs(num, combs_lst):
        divisors = [1]
        for l in combs_lst:
            prd = 1
            for elem in l:
                prd *= elem
            if prd != num:
                divisors.append(prd)
        return divisors

    is_abundant = lambda x: x < sum(get_divs(x, get_combs(get_pfactors(x))))
    abundant_nums = [i for i in range(1, n + 1) if is_abundant(i)]
    marker = [False] * (n + 1)
    for i, n1 in enumerate(abundant_nums):
        for j in range(i, len(abundant_nums)):
            tmp = n1 + abundant_nums[j]
            if tmp > n:
                break
            marker[tmp] = True
    return sum([i for i, b in enumerate(marker) if not b])


if __name__ == '__main__':
    n = 28_123
    i = 1
    prob_id = 23
    timed.caller(fn_brute, n, i, prob_id)
