# Solution of;
# Project Euler Problem 427: n-sequences
# https://projecteuler.net/problem=427
# 
# A sequence of integers S = {si} is called an n-sequence if it has n elements 
# and each element si satisfies 1 ≤ si ≤ n. Thus there are nn distinct 
# n-sequences in total. For example, the sequence S = {1, 5, 5, 10, 7, 7, 7, 
# 2, 3, 7} is a 10-sequence. For any sequence S, let L(S) be the length of the 
# longest contiguous subsequence of S with the same value. For example, for 
# the given sequence S above, L(S) = 3, because of the three consecutive 7's. 
# Let f(n) = ∑ L(S) for all n-sequences S. For example, f(3) = 45, f(7) = 
# 1403689 and f(11) = 481496895121. Find f(7 500 000) mod 1 000 000 009.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 427
    timed.caller(dummy, n, i, prob_id)
