# Solution of;
# Project Euler Problem 577: Counting hexagons
# https://projecteuler.net/problem=577
# 
# An equilateral triangle with integer side length $n \ge 3$ is divided into 
# $n^2$ equilateral triangles with side length 1 as shown in the diagram 
# below. The vertices of these triangles constitute a triangular lattice with 
# $\frac{(n+1)(n+2)} 2$ lattice points. Let $H(n)$ be the number of all 
# regular hexagons that can be found by connecting 6 of these points. For 
# example, $H(3)=1$, $H(6)=12$ and $H(20)=966$. Find $\displaystyle 
# \sum_{n=3}^{12345} H(n)$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 577
    timed.caller(dummy, n, i, prob_id)
