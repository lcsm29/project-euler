# Solution of;
# Project Euler Problem 536: Modulo power identity 
# https://projecteuler.net/problem=536
# 
# Let S(n) be the sum of all positive integers m not exceeding n having the 
# following property:a m+4 ≡ a (mod m) for all integers a. The values of m ≤ 
# 100 that satisfy this property are 1, 2, 3, 5 and 21, thus S(100) = 
# 1+2+3+5+21 = 32. You are given S(106) = 22868117. Find S(1012).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 536
    timed.caller(dummy, n, i, prob_id)
