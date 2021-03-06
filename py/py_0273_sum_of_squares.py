# Solution of;
# Project Euler Problem 273: Sum of Squares
# https://projecteuler.net/problem=273
# 
# Consider equations of the form: a2 + b2 = N, 0 ≤ a ≤ b, a, b and N integer. 
# For N=65 there are two solutions:a=1, b=8 and a=4, b=7. We call S(N) the sum 
# of the values of a of all solutions of a2 + b2 = N, 0 ≤ a ≤ b, a, b and N 
# integer. Thus S(65) = 1 + 4 = 5. Find ∑ S(N), for all squarefree N only 
# divisible by primes of the form 4k+1 with 4k+1 < 150.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 273
    timed.caller(dummy, n, i, prob_id)
