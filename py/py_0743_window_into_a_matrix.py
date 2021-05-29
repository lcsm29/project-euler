# Solution of;
# Project Euler Problem 743: Window into a Matrix
# https://projecteuler.net/problem=743
# 
# A window into a matrix is a contiguous sub matrix. Consider a $2\times n$ 
# matrix where every entry is either 0 or 1. Let $A(k,n)$ be the total number 
# of these matrices such that the sum of the entries in every $2\times k$ 
# window is $k$. You are given that $A(3,9) = 560$ and $A(4,20) = 1060870$. 
# Find $A(10^8,10^{16})$. Give your answer modulo $1\,000\,000\,007$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 743
    timed.caller(dummy, n, i, prob_id)
