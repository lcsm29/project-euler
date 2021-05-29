# Solution of;
# Project Euler Problem 492: Exploding sequence
# https://projecteuler.net/problem=492
# 
# Define the sequence a1, a2, a3, . . . as:a1 = 1an+1 = 6an2 + 10an + 3 for n 
# ≥ 1. Examples:a3 = 2359a6 = 269221280981320216750489044576319a6 mod 1 000 
# 000 007 = 203064689a100 mod 1 000 000 007 = 456482974Define B(x,y,n) as ∑ 
# (an mod p) for every prime p such that x ≤ p ≤ x+y. Examples:B(109, 103, 
# 103) = 23674718882B(109, 103, 1015) = 20731563854Find B(109, 107, 1015).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 492
    timed.caller(dummy, n, i, prob_id)
