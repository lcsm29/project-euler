# Solution of;
# Project Euler Problem 642: Sum of largest prime factors
# https://projecteuler.net/problem=642
# 
# Let $f(n)$ be the largest prime factor of $n$ and $\displaystyle F(n) = 
# \sum_{i=2}^{n}f(i)$. For example $F(10)=32$, $F(100)=1915$ and 
# $F(10000)=10118280$. Find $F(201820182018)$. Give your answer modulus 
# $10^9$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 642
    timed.caller(dummy, n, i, prob_id)
