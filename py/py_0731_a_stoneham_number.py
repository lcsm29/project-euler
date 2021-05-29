# Solution of;
# Project Euler Problem 731: A Stoneham Number
# https://projecteuler.net/problem=731
# 
# $$A=\sum_{i=1}^{\infty} \frac{1}{3^i 10^{3^i}}$$Define $A(n)$ to be the 10 
# decimal digits from the $n$th digit onward. For example, $A(100) = 
# 4938271604$ and $A(10^8)=2584642393$. Find $A(10^{16})$
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 731
    timed.caller(dummy, n, i, prob_id)
