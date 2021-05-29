# Solution of;
# Project Euler Problem 516: 5-smooth totients
# https://projecteuler.net/problem=516
# 
# 5-smooth numbers are numbers whose largest prime factor doesn't exceed 5. 
# 5-smooth numbers are also called Hamming numbers. Let S(L) be the sum of the 
# numbers n not exceeding L such that Euler's totient function φ(n) is a 
# Hamming number. S(100)=3728. Find S(1012). Give your answer modulo 232.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 516
    timed.caller(dummy, n, i, prob_id)
