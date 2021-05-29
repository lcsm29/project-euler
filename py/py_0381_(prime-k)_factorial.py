# Solution of;
# Project Euler Problem 381: (prime-k) factorial
# https://projecteuler.net/problem=381
# 
# For a prime p let S(p) = (∑ (p-k)!) mod(p) for 1 ≤ k ≤ 5. For example, if 
# p=7,(7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! = 
# 720+120+24+6+2 = 872. As 872 mod(7) = 4, S(7) = 4. It can be verified that ∑ 
# S(p) = 480 for 5 ≤ p < 100. Find ∑ S(p) for 5 ≤ p < 108.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 381
    timed.caller(dummy, n, i, prob_id)
