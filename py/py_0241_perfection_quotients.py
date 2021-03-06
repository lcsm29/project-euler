# Solution of;
# Project Euler Problem 241: Perfection Quotients
# https://projecteuler.net/problem=241
# 
# For a positive integer $n$, let $\sigma(n)$ be the sum of all divisors of 
# $n$. For example, $\sigma(6) = 1 + 2 + 3 + 6 = 12$. A perfect number, as you 
# probably know, is a number with $\sigma(n) = 2n$. Let us define the 
# perfection quotient of a positive integer as $p(n) = \dfrac{\sigma(n)}{n}$. 
# Find the sum of all positive integers $n \le 10^{18}$ for which $p(n)$ has 
# the form $k + \dfrac{1}{2}$, where $k$ is an integer.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 241
    timed.caller(dummy, n, i, prob_id)
