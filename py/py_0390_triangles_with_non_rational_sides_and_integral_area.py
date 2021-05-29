# Solution of;
# Project Euler Problem 390: Triangles with non rational sides and integral area
# https://projecteuler.net/problem=390
# 
# Consider the triangle with sides $\sqrt 5$, $\sqrt {65}$ and $\sqrt {68}$. 
# It can be shown that this triangle has area $9$. $S(n)$ is the sum of the 
# areas of all triangles with sides $\sqrt{1+b^2}$, $\sqrt {1+c^2}$ and 
# $\sqrt{b^2+c^2}\,$ (for positive integers $b$ and $c$) that have an integral 
# area not exceeding $n$. The example triangle has $b=2$ and $c=8$. 
# $S(10^6)=18018206$. Find $S(10^{10})$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 390
    timed.caller(dummy, n, i, prob_id)
