# Solution of;
# Project Euler Problem 635: Subset sums
# https://projecteuler.net/problem=635
# 
# Let $A_q(n)$ be the number of subsets, $B$, of the set $\{1, 2, . . . , q 
# \cdot n\}$ that satisfy two conditions:1) $B$ has exactly $n$ elements;2) 
# the sum of the elements of $B$ is divisible by $n$. E. g. $A_2(5)=52$ and 
# $A_3(5)=603$. Let $S_q(L)$ be $\sum A_q(p)$ where the sum is taken over all 
# primes $p \le L$. E. g. $S_2(10)=554$, $S_2(100)$ mod 
# $1\,000\,000\,009=100433628$ and $S_3(100)$ mod 
# $1\,000\,000\,009=855618282$. Find $S_2(10^8)+S_3(10^8)$. Give your answer 
# modulo $1\,000\,000\,009$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 635
    timed.caller(dummy, n, i, prob_id)
