# Solution of;
# Project Euler Problem 558: Irrational base
# https://projecteuler.net/problem=558
# 
# Let r be the real root of the equation x3 = x2 + 1. Every positive integer 
# can be written as the sum of distinct increasing powers of r. If we require 
# the number of terms to be finite and the difference between any two 
# exponents to be three or more, then the representation is unique. For 
# example, 3 = r -10 + r -5 + r -1 + r 2 and 10 = r -10 + r -7 + r 6. 
# Interestingly, the relation holds for the complex roots of the equation. Let 
# w(n) be the number of terms in this unique representation of n. Thus w(3) = 
# 4 and w(10) = 3. More formally, for all positive integers n, we have:n = 
# $\displaystyle \sum_{k=-\infty}^{\infty}$ bk rkunder the conditions that:bk 
# is 0 or 1 for all k;bk + bk+1 + bk+2 ≤ 1 for all k;w(n) = $\displaystyle 
# \sum_{k=-\infty}^{\infty}$ bk is finite. Let S(m) = $\displaystyle 
# \sum_{j=1}^{m}$ w(j2). You are given S(10) = 61 and S(1000) = 19403. Find 
# S(5 000 000).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 558
    timed.caller(dummy, n, i, prob_id)
