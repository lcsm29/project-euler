# Solution of;
# Project Euler Problem 130: Composites with prime repunit property
# https://projecteuler.net/problem=130
# 
# A number consisting entirely of ones is called a repunit. We shall define 
# R(k) to be a repunit of length k; for example, R(6) = 111111. Given that n 
# is a positive integer and GCD(n, 10) = 1, it can be shown that there always 
# exists a value, k, for which R(k) is divisible by n, and let A(n) be the 
# least such value of k; for example, A(7) = 6 and A(41) = 5. You are given 
# that for all primes, p > 5, that p − 1 is divisible by A(p). For example, 
# when p = 41, A(41) = 5, and 40 is divisible by 5. However, there are rare 
# composite values for which this is also true; the first five examples being 
# 91, 259, 451, 481, and 703. Find the sum of the first twenty-five composite 
# values of n for whichGCD(n, 10) = 1 and n − 1 is divisible by A(n).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 130
    timed.caller(dummy, n, i, prob_id)
