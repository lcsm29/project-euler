# Solution of;
# Project Euler Problem 612: Friend numbers
# https://projecteuler.net/problem=612
# 
# Let's call two numbers friend numbers if their representation in base 10 has 
# at least one common digit. E. g. 1123 and 3981 are friend numbers. Let 
# $f(n)$ be the number of pairs $(p,q)$ with $1\le p \lt q \lt n$ such that 
# $p$ and $q$ are friend numbers. $f(100)=1539$. Find $f(10^{18})$ mod 
# $1000267129$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 612
    timed.caller(dummy, n, i, prob_id)
