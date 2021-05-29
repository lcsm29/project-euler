# Solution of;
# Project Euler Problem 192: Best Approximations
# https://projecteuler.net/problem=192
# 
# Let $x$ be a real number. A best approximation to $x$ for the denominator 
# bound $d$ is a rational number $\frac r s $ in reduced form, with $s \le d$, 
# such that any rational number which is closer to $x$ than $\frac r s$ has a 
# denominator larger than $d$: $|\frac p q -x | < |\frac r s -x| \Rightarrow q 
# > d$For example, the best approximation to $\sqrt {13}$ for the denominator 
# bound 20 is $\frac {18} 5$ and the best approximation to $\sqrt {13}$ for 
# the denominator bound 30 is $\frac {101}{28}$. Find the sum of all 
# denominators of the best approximations to $\sqrt n$ for the denominator 
# bound $10^{12}$, where $n$ is not a perfect square and $ 1 < n \le 100000$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 192
    timed.caller(dummy, n, i, prob_id)
