# Solution of;
# Project Euler Problem 745: Sum of Squares
# https://projecteuler.net/problem=745
# 
# For a positive integer, $n$, define $g(n)$ to be the maximum perfect square 
# that divides $n$. For example, $g(18) = 9$, $g(19) = 1$. Also 
# define$$\displaystyle S(N) = \sum_{n=1}^N g(n)$$For example, $S(10) = 24$ 
# and $S(100) = 767$. Find $S(10^{14})$. Give your answer modulo 
# $1\,000\,000\,007$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 745
    timed.caller(dummy, n, i, prob_id)
