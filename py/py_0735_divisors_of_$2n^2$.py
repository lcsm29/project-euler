# Solution of;
# Project Euler Problem 735: Divisors of $2n^2$
# https://projecteuler.net/problem=735
# 
# Let $f(n)$ be the number of divisors of $2n^2$ that are no greater than n. 
# For example, $f(15)=8$ because there are 8 such divisors: 1,2,3,5,6,9,10,15. 
# Note that 18 is also a divisor of $2\times 15^2$ but it is not counted 
# because it is greater than 15. Let $\displaystyle F(N) = \sum_{n=1}^N f(n)$. 
# You are given $F(15)=63$, and $F(1000)=15066$. Find $F(10^{12})$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 735
    timed.caller(dummy, n, i, prob_id)
