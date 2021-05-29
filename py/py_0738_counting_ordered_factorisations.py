# Solution of;
# Project Euler Problem 738: Counting Ordered Factorisations
# https://projecteuler.net/problem=738
# 
# Define $d(n,k)$ to be the number of ways to write $n$ as a product of $k$ 
# ordered integers\[n = x_1\times x_2\times x_3\times \ldots\times x_k\qquad 
# 1\le x_1\le x_2\le\ldots\le x_k\]Further define $D(N,K)$ to be the sum of 
# $d(n,k)$ for $1\le n\le N$ and $1\le k\le K$. You are given that $D(10, 10) 
# = 153$ and $D(100, 100) = 35384$. Find $D(10^{10},10^{10})$ giving your 
# answer modulo $1\,000\,000\,007$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 738
    timed.caller(dummy, n, i, prob_id)
