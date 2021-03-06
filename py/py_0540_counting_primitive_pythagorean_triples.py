# Solution of;
# Project Euler Problem 540: Counting primitive Pythagorean triples
# https://projecteuler.net/problem=540
# 
# A Pythagorean triple consists of three positive integers $a, b$ and $c$ 
# satisfying $a^2+b^2=c^2$. The triple is called primitive if $a, b$ and $c$ 
# are relatively prime. Let P($n$) be the number of primitive Pythagorean 
# triples with $a < b < c \le n$. For example P(20) = 3, since there are three 
# triples: (3,4,5), (5,12,13) and (8,15,17). You are given that P(106) = 
# 159139. Find P(3141592653589793).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 540
    timed.caller(dummy, n, i, prob_id)
