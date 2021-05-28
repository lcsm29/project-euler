# Solution of;
# Project Euler Problem 210: Obtuse Angled Triangles
# https://projecteuler.net/problem=210
# 
# Consider the set S(r) of points (x,y) with integer coordinates satisfying 
# |x| + |y| ≤ r. Let O be the point (0,0) and C the point (r/4,r/4). Let N(r) 
# be the number of points B in S(r), so that the triangle OBC has an obtuse 
# angle, i. e. the largest angle α satisfies 90°<α<180°. So, for example, 
# N(4)=24 and N(8)=100. What is N(1,000,000,000)?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
