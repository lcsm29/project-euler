# Solution of;
# Project Euler Problem 248: Numbers for which Euler’s totient function equals 13!
# https://projecteuler.net/problem=248
# 
# The first number n for which φ(n)=13! is 6227180929. Find the 150,000th such 
# number.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 248
    timed.caller(dummy, n, i, prob_id)
