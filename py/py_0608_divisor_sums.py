# Solution of;
# Project Euler Problem 608: Divisor Sums
# https://projecteuler.net/problem=608
# 
# Let $D(m,n)=\displaystyle\sum_{d|m}\sum_{k=1}^n\sigma_{\small 0}(kd)$ where 
# $d$ runs through all divisors of $m$ and $\sigma_{\small 0}(n)$ is the 
# number of divisors of $n$. You are given $D(3!,10^2)=3398$ and 
# $D(4!,10^6)=268882292$. Find $D(200!,10^{12}) \text{ mod } (10^9 + 7)$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 608
    timed.caller(dummy, n, i, prob_id)
