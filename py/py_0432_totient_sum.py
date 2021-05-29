# Solution of;
# Project Euler Problem 432: Totient sum
# https://projecteuler.net/problem=432
# 
# Let S(n,m) = ∑φ(n × i) for 1 ≤ i ≤ m. (φ is Euler's totient function)You are 
# given that S(510510,106 )= 45480596821125120. Find S(510510,1011). Give the 
# last 9 digits of your answer.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 432
    timed.caller(dummy, n, i, prob_id)
