# Solution of;
# Project Euler Problem 53: Combinatoric selections
# https://projecteuler.net/problem=53
# 
# There are exactly ten ways of selecting three from five, 12345:123, 124, 
# 125, 134, 135, 145, 234, 235, 245, and 345In combinatorics, we use the 
# notation, $\displaystyle \binom 5 3 = 10$. In general, $\displaystyle \binom 
# n r = \dfrac{n!}{r!(n-r)!}$, where $r \le n$, $n! = n \times (n-1) \times . 
# . . \times 3 \times 2 \times 1$, and $0! = 1$. It is not until $n = 23$, 
# that a value exceeds one-million: $\displaystyle \binom {23} {10} = 
# 1144066$. How many, not necessarily distinct, values of $\displaystyle 
# \binom n r$ for $1 \le n \le 100$, are greater than one-million?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
