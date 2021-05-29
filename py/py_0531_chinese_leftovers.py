# Solution of;
# Project Euler Problem 531: Chinese leftovers
# https://projecteuler.net/problem=531
# 
# Let g(a,n,b,m) be the smallest non-negative solution x to the system:x = a 
# mod nx = b mod mif such a solution exists, otherwise 0. E. g. g(2,4,4,6)=10, 
# but g(3,4,4,6)=0. Let φ(n) be Euler's totient function. Let 
# f(n,m)=g(φ(n),n,φ(m),m)Find ∑ f(n,m) for 1000000 ≤ n < m < 1005000
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 531
    timed.caller(dummy, n, i, prob_id)
