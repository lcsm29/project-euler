# Solution of;
# Project Euler Problem 521: Smallest prime factor
# https://projecteuler.net/problem=521
# 
# Let smpf(n) be the smallest prime factor of n. smpf(91)=7 because 91=7×13 
# and smpf(45)=3 because 45=3×3×5. Let S(n) be the sum of smpf(i) for 2 ≤ i ≤ 
# n. E. g. S(100)=1257. Find S(1012) mod 109.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 521
    timed.caller(dummy, n, i, prob_id)
