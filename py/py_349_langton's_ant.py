# Solution of;
# Project Euler Problem 349: Langton's ant
# https://projecteuler.net/problem=349
# 
# An ant moves on a regular grid of squares that are coloured either black or 
# white. The ant is always oriented in one of the cardinal directions (left, 
# right, up or down) and moves from square to adjacent square according to the 
# following rules:- if it is on a black square, it flips the colour of the 
# square to white, rotates 90 degrees counterclockwise and moves forward one 
# square. - if it is on a white square, it flips the colour of the square to 
# black, rotates 90 degrees clockwise and moves forward one square. Starting 
# with a grid that is entirely white, how many squares are black after 1018 
# moves of the ant?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
