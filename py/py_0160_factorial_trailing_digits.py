# Solution of;
# Project Euler Problem 160: Factorial trailing digits
# https://projecteuler.net/problem=160
# 
# For any N, let f(N) be the last five digits before the trailing zeroes in 
# N!. For example,9! = 362880 so f(9)=3628810! = 3628800 so f(10)=3628820! = 
# 2432902008176640000 so f(20)=17664Find f(1,000,000,000,000)
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 160
    timed.caller(dummy, n, i, prob_id)
