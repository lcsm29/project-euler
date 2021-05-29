# Solution of;
# Project Euler Problem 229: Four Representations using Squares
# https://projecteuler.net/problem=229
# 
# Consider the number 3600. It is very special, because3600 = 482 + 3623600 = 
# 202 + 2×4023600 = 302 + 3×3023600 = 452 + 7×152Similarly, we find that 88201 
# = 992 + 2802 = 2872 + 2×542 = 2832 + 3×522 = 1972 + 7×842. In 1747, Euler 
# proved which numbers are representable as a sum of two squares. We are 
# interested in the numbers n which admit representations of all of the 
# following four types:n = a12 + b12n = a22 + 2 b22n = a32 + 3 b32n = a72 + 7 
# b72,where the ak and bk are positive integers. There are 75373 such numbers 
# that do not exceed 107. How many such numbers are there that do not exceed 
# 2×109?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 229
    timed.caller(dummy, n, i, prob_id)
