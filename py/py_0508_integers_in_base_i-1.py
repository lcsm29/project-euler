# Solution of;
# Project Euler Problem 508: Integers in base i-1
# https://projecteuler.net/problem=508
# 
# Consider the Gaussian integer i-1. A base i-1 representation of a Gaussian 
# integer a+bi is a finite sequence of digits dn-1dn-2. . . d1d0 such 
# that:a+bi = dn-1(i-1)n-1 + dn-2(i-1)n-2 + . . . + d1(i-1) + d0Each dk is in 
# {0,1}There are no leading zeroes, i. e. dn-1 ≠ 0, unless a+bi is itself 
# 0Here are base i-1 representations of a few Gaussian integers:11+24i → 
# 11101011000110124-11i → 1100101100118+0i → 111000000-5+0i → 110011010+0i → 
# 0Remarkably, every Gaussian integer has a unique base i-1 
# representation!Define f(a+bi) as the number of 1s in the unique base i-1 
# representation of a+bi. For example, f(11+24i) = 9 and f(24-11i) = 7. Define 
# B(L) as the sum of f(a+bi) for all integers a, b such that |a| ≤ L and |b| ≤ 
# L. For example, B(500) = 10795060. Find B(1015) mod 1 000 000 007.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 508
    timed.caller(dummy, n, i, prob_id)
