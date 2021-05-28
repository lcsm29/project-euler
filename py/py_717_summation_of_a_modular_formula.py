# Solution of;
# Project Euler Problem 717: Summation of a Modular Formula
# https://projecteuler.net/problem=717
# 
# For an odd prime $p$, define $f(p) = 
# \left\lfloor\frac{2^{(2^p)}}{p}\right\rfloor\bmod{2^p}$For example, when 
# $p=3$, $\lfloor 2^8/3\rfloor = 85 \equiv 5 \pmod 8$ and so $f(3) = 5$. 
# Further define $g(p) = f(p)\bmod p$. You are given $g(31) = 17$. Now define 
# $G(N)$ to be the summation of $g(p)$ for all odd primes less than $N$. You 
# are given $G(100) = 474$ and $G(10^4) = 2819236$. Find $G(10^7)$
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
