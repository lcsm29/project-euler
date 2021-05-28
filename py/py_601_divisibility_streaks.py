# Solution of;
# Project Euler Problem 601: Divisibility streaks
# https://projecteuler.net/problem=601
# 
# For every positive number $n$ we define the function $streak(n)=k$ as the 
# smallest positive integer $k$ such that $n+k$ is not divisible by $k+1$. E. 
# g:13 is divisible by 1 14 is divisible by 2 15 is divisible by 3 16 is 
# divisible by 4 17 is NOT divisible by 5 So $streak(13) = 4$. Similarly:120 
# is divisible by 1 121 is NOT divisible by 2 So $streak(120) = 1$. Define 
# $P(s, N)$ to be the number of integers $n$, $1 < n < N$, for which 
# $streak(n) = s$. So $P(3, 14) = 1$ and $P(6, 10^6) = 14286$. Find the sum, 
# as $i$ ranges from 1 to 31, of $P(i, 4^i)$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
