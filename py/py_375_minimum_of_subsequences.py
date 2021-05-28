# Solution of;
# Project Euler Problem 375: Minimum of subsequences
# https://projecteuler.net/problem=375
# 
# Let $S_n$ be an integer sequence produced with the following pseudo-random 
# number generator:\[\begin{equation}\begin{split}S_0 & = 290797 \\S_{n+1} & = 
# S_n^2 \bmod 50515093\end{split}\end{equation}\]Let $A(i, j)$ be the minimum 
# of the numbers $S_i, S_{i+1}, \ldots, S_j$ for $i\le j$. Let $M(N) = \sum 
# A(i, j)$ for $1 \le i \le j \le N$. We can verify that $M(10) = 432256955$ 
# and $M(10\,000) = 3264567774119$. Find $M(2\,000\,000\,000)$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
