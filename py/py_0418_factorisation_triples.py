# Solution of;
# Project Euler Problem 418: Factorisation triples
# https://projecteuler.net/problem=418
# 
# Let n be a positive integer. An integer triple (a, b, c) is called a 
# factorisation triple of n if: 1 ≤ a ≤ b ≤ c a·b·c = n. Define f(n) to be a + 
# b + c for the factorisation triple (a, b, c) of n which minimises c / a. One 
# can show that this triple is unique. For example, f(165) = 19, f(100100) = 
# 142 and f(20!) = 4034872. Find f(43!).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 418
    timed.caller(dummy, n, i, prob_id)
