# Solution of;
# Project Euler Problem 184: Triangles containing the origin
# https://projecteuler.net/problem=184
# 
# Consider the set Ir of points (x,y) with integer co-ordinates in the 
# interior of the circle with radius r, centered at the origin, i. e. x2 + y2 
# < r2. For a radius of 2, I2 contains the nine points (0,0), (1,0), (1,1), 
# (0,1), (-1,1), (-1,0), (-1,-1), (0,-1) and (1,-1). There are eight triangles 
# having all three vertices in I2 which contain the origin in the interior. 
# Two of them are shown below, the others are obtained from these by rotation. 
# For a radius of 3, there are 360 triangles containing the origin in the 
# interior and having all vertices in I3 and for I5 the number is 10600. How 
# many triangles are there containing the origin in the interior and having 
# all three vertices in I105?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 184
    timed.caller(dummy, n, i, prob_id)
