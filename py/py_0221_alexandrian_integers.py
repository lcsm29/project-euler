# Solution of;
# Project Euler Problem 221: Alexandrian Integers
# https://projecteuler.net/problem=221
# 
# We shall call a positive integer A an "Alexandrian integer", if there exist 
# integers p, q, r such that:$$A = p \cdot q \cdot r$$and$$\dfrac{1}{A} = 
# \dfrac{1}{p} + \dfrac{1}{q} + \dfrac{1}{r}$$For example, 630 is an 
# Alexandrian integer ($p = 5, q = -7, r = -18$). In fact, 630 is the 6th 
# Alexandrian integer, the first 6 Alexandrian integers being: 6, 42, 120, 
# 156, 420, and 630. Find the 150000th Alexandrian integer.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 221
    timed.caller(dummy, n, i, prob_id)
