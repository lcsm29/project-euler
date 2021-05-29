# Solution of;
# Project Euler Problem 163: Cross-hatched triangles
# https://projecteuler.net/problem=163
# 
# Consider an equilateral triangle in which straight lines are drawn from each 
# vertex to the middle of the opposite side, such as in the size 1 triangle in 
# the sketch below. Sixteen triangles of either different shape or size or 
# orientation or location can now be observed in that triangle. Using size 1 
# triangles as building blocks, larger triangles can be formed, such as the 
# size 2 triangle in the above sketch. One-hundred and four triangles of 
# either different shape or size or orientation or location can now be 
# observed in that size 2 triangle. It can be observed that the size 2 
# triangle contains 4 size 1 triangle building blocks. A size 3 triangle would 
# contain 9 size 1 triangle building blocks and a size n triangle would thus 
# contain n2 size 1 triangle building blocks. If we denote T(n) as the number 
# of triangles present in a triangle of size n, thenT(1) = 16T(2) = 104Find 
# T(36).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 163
    timed.caller(dummy, n, i, prob_id)
