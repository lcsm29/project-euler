# Solution of;
# Project Euler Problem 235: An Arithmetic Geometric sequence
# https://projecteuler.net/problem=235
# 
# Given is the arithmetic-geometric sequence u(k) = (900-3k)rk-1. Let s(n) = 
# Σk=1. . . nu(k). Find the value of r for which s(5000) = -600,000,000,000. 
# Give your answer rounded to 12 places behind the decimal point.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 235
    timed.caller(dummy, n, i, prob_id)
