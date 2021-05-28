# Solution of;
# Project Euler Problem 565: Divisibility of sum of divisors
# https://projecteuler.net/problem=565
# 
# Let $\sigma(n)$ be the sum of the divisors of $n$. E. g. the divisors of 4 
# are 1, 2 and 4, so $\sigma(4)=7$. The numbers $n$ not exceeding 20 such that 
# 7 divides $\sigma(n)$ are: 4,12,13 and 20, the sum of these numbers being 
# 49. Let $S(n , d)$ be the sum of the numbers $i$ not exceeding $n$ such that 
# $d$ divides $\sigma(i)$. So $S(20 , 7)=49$. You are given: 
# $S(10^6,2017)=150850429$ and $S(10^9 , 2017)=249652238344557$. Find 
# $S(10^{11} , 2017)$
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
