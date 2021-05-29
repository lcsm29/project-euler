# Solution of;
# Project Euler Problem 515: Dissonant Numbers
# https://projecteuler.net/problem=515
# 
# Let d(p,n,0) be the multiplicative inverse of n modulo prime p, defined as n 
# × d(p,n,0) = 1 mod p. Let d(p,n,k) = $\sum_{i=1}^n$d(p,i,k−1) for k ≥ 1. Let 
# D(a,b,k) = $\sum$(d(p,p-1,k) mod p) for all primes a ≤ p < a + b. You are 
# given:D(101,1,10) = 45D(103,102,102) = 8334D(106,103,103) = 38162302Find 
# D(109,105,105).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 515
    timed.caller(dummy, n, i, prob_id)
