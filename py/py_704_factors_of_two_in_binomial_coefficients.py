# Solution of;
# Project Euler Problem 704: Factors of Two in Binomial Coefficients
# https://projecteuler.net/problem=704
# 
# Define $g(n, m)$ to be the largest integer $k$ such that $2^k$ divides 
# $\binom{n}m$. For example, $\binom{12}5 = 792 = 2^3 \cdot 3^2 \cdot 11$, 
# hence $g(12, 5) = 3$. Then define $F(n) = \max \{ g(n, m) : 0 \le m \le n 
# \}$. $F(10) = 3$ and $F(100) = 6$. Let $S(N)$ = 
# $\displaystyle\sum_{n=1}^N{F(n)}$. You are given that $S(100) = 389$ and 
# $S(10^7) = 203222840$. Find $S(10^{16})$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
