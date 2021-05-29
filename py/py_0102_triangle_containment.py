# Solution of;
# Project Euler Problem 102: Triangle containment
# https://projecteuler.net/problem=102
# 
# Three distinct points are plotted at random on a Cartesian plane, for which 
# -1000 ≤ x, y ≤ 1000, such that a triangle is formed. Consider the following 
# two triangles:A(-340,495), B(-153,-910), C(835,-947)X(-175,41), 
# Y(-421,-714), Z(574,-645)It can be verified that triangle ABC contains the 
# origin, whereas triangle XYZ does not. Using triangles. txt (right click and 
# 'Save Link/Target As. . . '), a 27K text file containing the co-ordinates of 
# one thousand "random" triangles, find the number of triangles for which the 
# interior contains the origin. NOTE: The first two examples in the file 
# represent the triangles in the example given above.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 102
    timed.caller(dummy, n, i, prob_id)
