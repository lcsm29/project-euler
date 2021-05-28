# Solution of;
# Project Euler Problem 365: A huge binomial coefficient
# https://projecteuler.net/problem=365
# 
# The binomial coefficient $\displaystyle{\binom{10^{18}}{10^9}}$ is a number 
# with more than 9 billion ($9\times 10^9$) digits. Let $M(n,k,m)$ denote the 
# binomial coefficient $\displaystyle{\binom{n}{k}}$ modulo $m$. Calculate 
# $\displaystyle{\sum M(10^{18},10^9,p\cdot q\cdot r)}$ for $1000\lt p\lt q\lt 
# r\lt 5000$ and $p$,$q$,$r$ prime.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
