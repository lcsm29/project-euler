# Solution of;
# Project Euler Problem 231: The prime factorisation of binomial coefficients
# https://projecteuler.net/problem=231
# 
# The binomial coefficient $\displaystyle \binom {10} 3 = 120$. $120 = 2^3 
# \times 3 \times 5 = 2 \times 2 \times 2 \times 3 \times 5$, and $2 + 2 + 2 + 
# 3 + 5 = 14$. So the sum of the terms in the prime factorisation of 
# $\displaystyle \binom {10} 3$ is $14$. Find the sum of the terms in the 
# prime factorisation of $\displaystyle \binom {20\,000\,000} {15\,000\,000}$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
