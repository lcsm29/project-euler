# Solution of;
# Project Euler Problem 510: Tangent Circles
# https://projecteuler.net/problem=510
# 
# Circles A and B are tangent to each other and to line L at three distinct 
# points. Circle C is inside the space between A, B and L, and tangent to all 
# three. Let rA, rB and rC be the radii of A, B and C respectively. Let S(n) = 
# ∑ rA + rB + rC, for 0 < rA ≤ rB ≤ n where rA, rB and rC are integers. The 
# only solution for 0 < rA ≤ rB ≤ 5 is rA = 4, rB = 4 and rC = 1, so S(5) = 4 
# + 4 + 1 = 9. You are also given S(100) = 3072. Find S(109).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
