# Solution of;
# Project Euler Problem 454: Diophantine reciprocals III
# https://projecteuler.net/problem=454
# 
# In the following equation x, y, and n are positive integers. $$\dfrac{1}{x} 
# + \dfrac{1}{y} = \dfrac{1}{n}$$For a limit L we define F(L) as the number of 
# solutions which satisfy x < y ≤ L. We can verify that F(15) = 4 and F(1000) 
# = 1069. Find F(1012).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 454
    timed.caller(dummy, n, i, prob_id)
