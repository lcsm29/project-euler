# Solution of;
# Project Euler Problem 297: Zeckendorf Representation
# https://projecteuler.net/problem=297
# 
# Each new term in the Fibonacci sequence is generated by adding the previous 
# two terms. Starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 
# 13, 21, 34, 55, 89. Every positive integer can be uniquely written as a sum 
# of nonconsecutive terms of the Fibonacci sequence. For example, 100 = 3 + 8 
# + 89. Such a sum is called the Zeckendorf representation of the number. For 
# any integer n>0, let z(n) be the number of terms in the Zeckendorf 
# representation of n. Thus, z(5) = 1, z(14) = 2, z(100) = 3 etc. Also, for 
# 0<n<106, ∑ z(n) = 7894453. Find ∑ z(n) for 0<n<1017.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 297
    timed.caller(dummy, n, i, prob_id)