# Solution of;
# Project Euler Problem 512: Sums of totients of powers
# https://projecteuler.net/problem=512
# 
# Let $\varphi(n)$ be Euler's totient function. Let 
# $f(n)=(\sum_{i=1}^{n}\varphi(n^i)) \text{ mod } (n+1)$. Let 
# $g(n)=\sum_{i=1}^{n} f(i)$. $g(100)=2007$. Find $g(5 \times 10^8)$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 512
    timed.caller(dummy, n, i, prob_id)
