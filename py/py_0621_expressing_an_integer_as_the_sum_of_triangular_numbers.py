# Solution of;
# Project Euler Problem 621: Expressing an integer as the sum of triangular numbers
# https://projecteuler.net/problem=621
# 
# Gauss famously proved that every positive integer can be expressed as the 
# sum of three triangular numbers (including 0 as the lowest triangular 
# number). In fact most numbers can be expressed as a sum of three triangular 
# numbers in several ways. Let $G(n)$ be the number of ways of expressing $n$ 
# as the sum of three triangular numbers, regarding different arrangements of 
# the terms of the sum as distinct. For example, $G(9) = 7$, as 9 can be 
# expressed as: 3+3+3, 0+3+6, 0+6+3, 3+0+6, 3+6+0, 6+0+3, 6+3+0. You are given 
# $G(1000) = 78$ and $G(10^6) = 2106$. Find $G(17 526 \times 10^9)$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 621
    timed.caller(dummy, n, i, prob_id)
