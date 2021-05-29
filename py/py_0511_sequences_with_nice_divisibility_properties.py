# Solution of;
# Project Euler Problem 511: Sequences with nice divisibility properties
# https://projecteuler.net/problem=511
# 
# Let Seq(n,k) be the number of positive-integer sequences {ai}1≤i≤n of length 
# n such that:n is divisible by ai for 1 ≤ i ≤ n, and n + a1 + a2 + . . . + an 
# is divisible by k. Examples:Seq(3,4) = 4, and the 4 sequences are:{1, 1, 
# 3}{1, 3, 1}{3, 1, 1}{3, 3, 3}Seq(4,11) = 8, and the 8 sequences are:{1, 1, 
# 1, 4}{1, 1, 4, 1}{1, 4, 1, 1}{4, 1, 1, 1}{2, 2, 2, 1}{2, 2, 1, 2}{2, 1, 2, 
# 2}{1, 2, 2, 2}The last nine digits of Seq(1111,24) are 840643584. Find the 
# last nine digits of Seq(1234567898765,4321).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 511
    timed.caller(dummy, n, i, prob_id)
