# Solution of;
# Project Euler Problem 208: Robot Walks
# https://projecteuler.net/problem=208
# 
# A robot moves in a series of one-fifth circular arcs (72°), with a free 
# choice of a clockwise or an anticlockwise arc for each step, but no turning 
# on the spot. One of 70932 possible closed paths of 25 arcs starting 
# northward isGiven that the robot starts facing North, how many journeys of 
# 70 arcs in length can it take that return it, after the final arc, to its 
# starting position?(Any arc may be traversed multiple times. )
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 208
    timed.caller(dummy, n, i, prob_id)
