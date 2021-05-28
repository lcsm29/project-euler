# Solution of;
# Project Euler Problem 693: Finite Sequence Generator
# https://projecteuler.net/problem=693
# 
# Two positive integers $x$ and $y$ ($x > y$) can generate a sequence in the 
# following manner:$a_x = y$ is the first term,$a_{z+1} = a_z^2 \bmod z$ for 
# $z = x, x+1,x+2,\ldots$ andthe generation stops when a term becomes 0 or 1. 
# The number of terms in this sequence is denoted $l(x,y)$. For example, with 
# $x = 5$ and $y = 3$, we get $a_5 = 3$, $a_6 = 3^2 \bmod 5 = 4$, $a_7 = 
# 4^2\bmod 6 = 4$, etc. Giving the sequence of 29 terms:$ 
# 3,4,4,2,4,7,9,4,4,3,9,6,4,16,4,16,16,4,16,3,9,6,10,19,25,16,16,8,0 $Hence 
# $l(5,3) = 29$. $g(x)$ is defined to be the maximum value of $l(x,y)$ for $y 
# < x$. For example, $g(5) = 29$. Further, define $f(n)$ to be the maximum 
# value of $g(x)$ for $x \le n$. For example, $f(100) = 145$ and $f(10\,000) = 
# 8824$. Find $f(3\,000\,000)$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
