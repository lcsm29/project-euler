# Solution of;
# Project Euler Problem 124: Ordered radicals
# https://projecteuler.net/problem=124
# 
# The radical of n, rad(n), is the product of the distinct prime factors of n. 
# For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42. If we 
# calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on n 
# if the radical values are equal, we get:Unsorted Sortednrad(n)nrad(n)k11 
# 11122 22233 42342 82455 33566 93677 55782 66893 7791010 101010Let E(k) be 
# the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9. 
# If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 124
    timed.caller(dummy, n, i, prob_id)
