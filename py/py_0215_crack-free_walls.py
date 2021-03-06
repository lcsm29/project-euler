# Solution of;
# Project Euler Problem 215: Crack-free Walls
# https://projecteuler.net/problem=215
# 
# Consider the problem of building a wall out of 2×1 and 3×1 bricks 
# (horizontal×vertical dimensions) such that, for extra strength, the gaps 
# between horizontally-adjacent bricks never line up in consecutive layers, i. 
# e. never form a "running crack". For example, the following 9×3 wall is not 
# acceptable due to the running crack shown in red:There are eight ways of 
# forming a crack-free 9×3 wall, written W(9,3) = 8. Calculate W(32,10).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 215
    timed.caller(dummy, n, i, prob_id)
