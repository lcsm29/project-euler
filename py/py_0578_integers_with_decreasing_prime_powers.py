# Solution of;
# Project Euler Problem 578: Integers with decreasing prime powers
# https://projecteuler.net/problem=578
# 
# Any positive integer can be written as a product of prime powers: p1a1 × 
# p2a2 × . . . × pkak,where pi are distinct prime integers, ai > 0 and pi < pj 
# if i < j. A decreasing prime power positive integer is one for which ai ≥ aj 
# if i < j. For example, 1, 2, 15=3×5, 360=23×32×5 and 1000=23×53 are 
# decreasing prime power integers. Let C(n) be the count of decreasing prime 
# power positive integers not exceeding n. C(100) = 94 since all positive 
# integers not exceeding 100 have decreasing prime powers except 18, 50, 54, 
# 75, 90 and 98. You are given C(106) = 922052. Find C(1013).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 578
    timed.caller(dummy, n, i, prob_id)
