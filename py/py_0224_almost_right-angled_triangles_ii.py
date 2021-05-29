# Solution of;
# Project Euler Problem 224: Almost right-angled triangles II
# https://projecteuler.net/problem=224
# 
# Let us call an integer sided triangle with sides a ≤ b ≤ c barely obtuse if 
# the sides satisfy a2 + b2 = c2 - 1. How many barely obtuse triangles are 
# there with perimeter ≤ 75,000,000?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 224
    timed.caller(dummy, n, i, prob_id)
