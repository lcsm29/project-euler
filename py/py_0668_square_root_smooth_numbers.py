# Solution of;
# Project Euler Problem 668: Square root smooth Numbers
# https://projecteuler.net/problem=668
# 
# A positive integer is called square root smooth if all of its prime factors 
# are strictly less than its square root. Including the number $1$, there are 
# $29$ square root smooth numbers not exceeding $100$. How many square root 
# smooth numbers are there not exceeding $10\,000\,000\,000$?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 668
    timed.caller(dummy, n, i, prob_id)
