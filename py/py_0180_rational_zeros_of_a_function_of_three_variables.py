# Solution of;
# Project Euler Problem 180: Rational zeros of a function of three variables
# https://projecteuler.net/problem=180
# 
# For any integer n, consider the three functionsf1,n(x,y,z) = xn+1 + yn+1 − 
# zn+1f2,n(x,y,z) = (xy + yz + zx)*(xn-1 + yn-1 − zn-1)f3,n(x,y,z) = xyz*(xn-2 
# + yn-2 − zn-2)and their combinationfn(x,y,z) = f1,n(x,y,z) + f2,n(x,y,z) − 
# f3,n(x,y,z)We call (x,y,z) a golden triple of order k if x, y, and z are all 
# rational numbers of the form a / b with0 < a < b ≤ k and there is (at least) 
# one integer n, so that fn(x,y,z) = 0. Let s(x,y,z) = x + y + z. Let t = u / 
# v be the sum of all distinct s(x,y,z) for all golden triples (x,y,z) of 
# order 35. All the s(x,y,z) and t must be in reduced form. Find u + v.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 180
    timed.caller(dummy, n, i, prob_id)
