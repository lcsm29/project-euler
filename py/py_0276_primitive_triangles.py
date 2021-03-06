# Solution of;
# Project Euler Problem 276: Primitive Triangles
# https://projecteuler.net/problem=276
# 
# Consider the triangles with integer sides a, b and c with a ≤ b ≤ c. An 
# integer sided triangle (a,b,c) is called primitive if gcd(a,b,c)=1. How many 
# primitive integer sided triangles exist with a perimeter not exceeding 10 
# 000 000?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 276
    timed.caller(dummy, n, i, prob_id)
