# Solution of;
# Project Euler Problem 108: Diophantine reciprocals I
# https://projecteuler.net/problem=108
# 
# In the following equation x, y, and n are positive integers. $$\dfrac{1}{x} 
# + \dfrac{1}{y} = \dfrac{1}{n}$$For n = 4 there are exactly three distinct 
# solutions:$$\begin{align}\dfrac{1}{5} + \dfrac{1}{20} &= 
# \dfrac{1}{4}\\\dfrac{1}{6} + \dfrac{1}{12} &= \dfrac{1}{4}\\\dfrac{1}{8} + 
# \dfrac{1}{8} &= \dfrac{1}{4}\end{align}$$What is the least value of n for 
# which the number of distinct solutions exceeds one-thousand?NOTE: This 
# problem is an easier version of Problem 110; it is strongly advised that you 
# solve this one first.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 108
    timed.caller(dummy, n, i, prob_id)
