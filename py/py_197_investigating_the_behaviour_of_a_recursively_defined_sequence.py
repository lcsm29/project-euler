# Solution of;
# Project Euler Problem 197: Investigating the behaviour of a recursively defined sequence
# https://projecteuler.net/problem=197
# 
# Given is the function f(x) = ⌊230. 403243784-x2⌋ × 10-9 ( ⌊ ⌋ is the 
# floor-function),the sequence un is defined by u0 = -1 and un+1 = f(un). Find 
# un + un+1 for n = 1012. Give your answer with 9 digits after the decimal 
# point.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
