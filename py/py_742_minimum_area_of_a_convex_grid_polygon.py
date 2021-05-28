# Solution of;
# Project Euler Problem 742: Minimum area of a convex grid polygon
# https://projecteuler.net/problem=742
# 
# A symmetrical convex grid polygon is a polygon such that:All its vertices 
# have integer coordinates. All its internal angles are strictly smaller than 
# $180°$. It has both horizontal and vertical symmetry. For example, the left 
# polygon is a convex grid polygon which has neither horizontal nor vertical 
# symmetry, while the right one is a valid symmetrical convex grid polygon 
# with six vertices:Define $A(N)$, the minimum area of a symmetrical convex 
# grid polygon with $N$ vertices. You are given $A(4) = 1$, $A(8) = 7$, $A(40) 
# = 1039$ and $A(100) = 17473$. Find $A(1000)$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
