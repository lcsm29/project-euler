# Solution of;
# Project Euler Problem 265: Binary Circles
# https://projecteuler.net/problem=265
# 
# 2N binary digits can be placed in a circle so that all the N-digit clockwise 
# subsequences are distinct. For N=3, two such circular arrangements are 
# possible, ignoring rotations:For the first arrangement, the 3-digit 
# subsequences, in clockwise order, are: 000, 001, 010, 101, 011, 111, 110 and 
# 100. Each circular arrangement can be encoded as a number by concatenating 
# the binary digits starting with the subsequence of all zeros as the most 
# significant bits and proceeding clockwise. The two arrangements for N=3 are 
# thus represented as 23 and 29:00010111 2 = 2300011101 2 = 29Calling S(N) the 
# sum of the unique numeric representations, we can see that S(3) = 23 + 29 = 
# 52. Find S(5).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 265
    timed.caller(dummy, n, i, prob_id)
