# Solution of;
# Project Euler Problem 615: The millionth number with at least one million prime factors
# https://projecteuler.net/problem=615
# 
# Consider the natural numbers having at least 5 prime factors, which don't 
# have to be distinct. Sorting these numbers by size gives a list which starts 
# with:32=2⋅2⋅2⋅2⋅248=2⋅2⋅2⋅2⋅364=2⋅2⋅2⋅2⋅2⋅272=2⋅2⋅2⋅3⋅380=2⋅2⋅2⋅2⋅596=2⋅2⋅2⋅2⋅2⋅3 
# . . . So, for example, the fifth number with at least 5 prime factors is 80. 
# Find the millionth number with at least one million prime factors. Give your 
# answer modulo 123454321.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 615
    timed.caller(dummy, n, i, prob_id)
