# Solution of;
# Project Euler Problem 319: Bounded Sequences
# https://projecteuler.net/problem=319
# 
# Let x1, x2,. . . , xn be a sequence of length n such that:x1 = 2for all 1 < 
# i ≤ n : xi-1 < xifor all i and j with 1 ≤ i, j ≤ n : (xi) j < (xj + 1)iThere 
# are only five such sequences of length 2, namely:{2,4}, {2,5}, {2,6}, {2,7} 
# and {2,8}. There are 293 such sequences of length 5; three examples are 
# given below:{2,5,11,25,55}, {2,6,14,36,88}, {2,8,22,64,181}. Let t(n) denote 
# the number of such sequences of length n. You are given that t(10) = 86195 
# and t(20) = 5227991891. Find t(1010) and give your answer modulo 109.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 319
    timed.caller(dummy, n, i, prob_id)
