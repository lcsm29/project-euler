# Solution of;
# Project Euler Problem 223: Almost right-angled triangles I
# https://projecteuler.net/problem=223
# 
# Let us call an integer sided triangle with sides a ≤ b ≤ c barely acute if 
# the sides satisfy a2 + b2 = c2 + 1. How many barely acute triangles are 
# there with perimeter ≤ 25,000,000?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 223
    timed.caller(dummy, n, i, prob_id)
