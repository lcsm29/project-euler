# Solution of;
# Project Euler Problem 147: Rectangles in cross-hatched grids
# https://projecteuler.net/problem=147
# 
# In a 3x2 cross-hatched grid, a total of 37 different rectangles could be 
# situated within that grid as indicated in the sketch. There are 5 grids 
# smaller than 3x2, vertical and horizontal dimensions being important, i. e. 
# 1x1, 2x1, 3x1, 1x2 and 2x2. If each of them is cross-hatched, the following 
# number of different rectangles could be situated within those smaller 
# grids:1x112x143x181x242x218Adding those to the 37 of the 3x2 grid, a total 
# of 72 different rectangles could be situated within 3x2 and smaller grids. 
# How many different rectangles could be situated within 47x43 and smaller 
# grids?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 147
    timed.caller(dummy, n, i, prob_id)
