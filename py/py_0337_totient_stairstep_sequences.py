# Solution of;
# Project Euler Problem 337: Totient Stairstep Sequences
# https://projecteuler.net/problem=337
# 
# Let {a1, a2,. . . , an} be an integer sequence of length n such that:a1 = 
# 6for all 1 ≤ i < n : φ(ai) < φ(ai+1) < ai < ai+11Let S(N) be the number of 
# such sequences with an ≤ N. For example, S(10) = 4: {6}, {6, 8}, {6, 8, 9} 
# and {6, 10}. We can verify that S(100) = 482073668 and S(10 000) mod 108 = 
# 73808307. Find S(20 000 000) mod 108. 1 φ denotes Euler's totient function.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 337
    timed.caller(dummy, n, i, prob_id)
