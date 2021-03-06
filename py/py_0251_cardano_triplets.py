# Solution of;
# Project Euler Problem 251: Cardano Triplets
# https://projecteuler.net/problem=251
# 
# A triplet of positive integers (a,b,c) is called a Cardano Triplet if it 
# satisfies the condition:$$\sqrt[3]{a + b \sqrt{c}} + \sqrt[3]{a - b 
# \sqrt{c}} = 1$$For example, (2,1,5) is a Cardano Triplet. There exist 149 
# Cardano Triplets for which a+b+c ≤ 1000. Find how many Cardano Triplets 
# exist such that a+b+c ≤ 110,000,000.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 251
    timed.caller(dummy, n, i, prob_id)
