# Solution of;
# Project Euler Problem 660: Pandigital Triangles
# https://projecteuler.net/problem=660
# 
# We call an integer sided triangle $n$-pandigital if it contains one angle of 
# 120 degrees and, when the sides of the triangle are written in base $n$, 
# together they use all $n$ digits of that base exactly once. For example, the 
# triangle (217, 248, 403) is 9-pandigital because it contains one angle of 
# 120 degrees and the sides written in base 9 are $261_9, 305_9, 487_9$ using 
# each of the 9 digits of that base once. Find the sum of the largest sides of 
# all n-pandigital triangles with $9 \le n \le 18$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 660
    timed.caller(dummy, n, i, prob_id)
