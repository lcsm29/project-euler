# Solution of;
# Project Euler Problem 694: Cube-full Divisors
# https://projecteuler.net/problem=694
# 
# A positive integer $n$ is considered cube-full, if for every prime $p$ that 
# divides $n$, so does $p^3$. Note that $1$ is considered cube-full. Let 
# $s(n)$ be the function that counts the number of cube-full divisors of $n$. 
# For example, $1$, $8$ and $16$ are the three cube-full divisors of $16$. 
# Therefore, $s(16)=3$. Let $S(n)$ represent the summatory function of $s(n)$, 
# that is $S(n)=\displaystyle\sum_{i=1}^n s(i)$. You are given $S(16) = 19$, 
# $S(100) = 126$ and $S(10000) = 13344$. Find $S(10^{18})$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 694
    timed.caller(dummy, n, i, prob_id)
