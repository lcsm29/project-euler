# Solution of;
# Project Euler Problem 129: Repunit divisibility
# https://projecteuler.net/problem=129
# 
# A number consisting entirely of ones is called a repunit. We shall define 
# R(k) to be a repunit of length k; for example, R(6) = 111111. Given that n 
# is a positive integer and GCD(n, 10) = 1, it can be shown that there always 
# exists a value, k, for which R(k) is divisible by n, and let A(n) be the 
# least such value of k; for example, A(7) = 6 and A(41) = 5. The least value 
# of n for which A(n) first exceeds ten is 17. Find the least value of n for 
# which A(n) first exceeds one-million.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 129
    timed.caller(dummy, n, i, prob_id)
