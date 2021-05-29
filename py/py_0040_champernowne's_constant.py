# Solution of;
# Project Euler Problem 40: Champernowne's constant
# https://projecteuler.net/problem=40
# 
# An irrational decimal fraction is created by concatenating the positive 
# integers:0. 123456789101112131415161718192021. . . It can be seen that the 
# 12th digit of the fractional part is 1. If dn represents the nth digit of 
# the fractional part, find the value of the following expression. d1 × d10 × 
# d100 × d1000 × d10000 × d100000 × d1000000
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 40
    timed.caller(dummy, n, i, prob_id)
