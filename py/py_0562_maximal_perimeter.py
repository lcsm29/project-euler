# Solution of;
# Project Euler Problem 562: Maximal perimeter
# https://projecteuler.net/problem=562
# 
# Construct triangle ABC such that:Vertices A, B and C are lattice points 
# inside or on the circle of radius r centered at the origin;the triangle 
# contains no other lattice point inside or on its edges;the perimeter is 
# maximum. Let R be the circumradius of triangle ABC and T(r) = R/r. For r = 
# 5, one possible triangle has vertices (-4,-3), (4,2) and (1,0) with 
# perimeter $\sqrt{13}+\sqrt{34}+\sqrt{89}$ and circumradius R = $\sqrt {\frac 
# {19669} 2 }$, so T(5) =$\sqrt {\frac {19669} {50} }$. You are given T(10) ~ 
# 97. 26729 and T(100) ~ 9157. 64707. Find T(107). Give your answer rounded to 
# the nearest integer.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 562
    timed.caller(dummy, n, i, prob_id)
