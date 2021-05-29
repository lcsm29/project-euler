# Solution of;
# Project Euler Problem 712: Exponent Difference
# https://projecteuler.net/problem=712
# 
# For any integer $n>0$ and prime number $p,$ define $\nu_p(n)$ as the 
# greatest integer $r$ such that $p^r$ divides $n$. Define $$D(n, m) = \sum_{p 
# \text{ prime}} \left| \nu_p(n) - \nu_p(m)\right|. $$ For example, $D(14,24) 
# = 4$. Furthermore, define $$S(N) = \sum_{1 \le n, m \le N} D(n, m). $$ You 
# are given $S(10) = 210$ and $S(10^2) = 37018$. Find $S(10^{12})$. Give your 
# answer modulo $1\,000\,000\,007$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 712
    timed.caller(dummy, n, i, prob_id)
