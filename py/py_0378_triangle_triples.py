# Solution of;
# Project Euler Problem 378: Triangle Triples
# https://projecteuler.net/problem=378
# 
# Let $T(n)$ be the nth triangle number, so $T(n) = \dfrac{n(n + 1)}{2}$. Let 
# $dT(n)$ be the number of divisors of $T(n)$. E. g. : $T(7) = 28$ and $dT(7) 
# = 6$. Let $Tr(n)$ be the number of triples $(i, j, k)$ such that $1 \le i 
# \lt j \lt k \le n$ and $dT(i) \gt dT(j) \gt dT(k)$. $Tr(20) = 14$, $Tr(100) 
# = 5772$, and $Tr(1000) = 11174776$. Find $Tr(60 000 000)$. Give the last 18 
# digits of your answer.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 378
    timed.caller(dummy, n, i, prob_id)
