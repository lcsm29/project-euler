# Solution of;
# Project Euler Problem 303: Multiples with small digits
# https://projecteuler.net/problem=303
# 
# For a positive integer n, define f(n) as the least positive multiple of n 
# that, written in base 10, uses only digits ≤ 2. Thus f(2)=2, f(3)=12, 
# f(7)=21, f(42)=210, f(89)=1121222. Also, $\sum \limits_{n = 1}^{100} 
# {\dfrac{f(n)}{n}} = 11363107$. Find $\sum \limits_{n=1}^{10000} 
# {\dfrac{f(n)}{n}}$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 303
    timed.caller(dummy, n, i, prob_id)
