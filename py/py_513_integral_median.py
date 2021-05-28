# Solution of;
# Project Euler Problem 513: Integral median
# https://projecteuler.net/problem=513
# 
# ABC is an integral sided triangle with sides a≤b≤c. mc is the median 
# connecting C and the midpoint of AB. F(n) is the number of such triangles 
# with c≤n for which mc has integral length as well. F(10)=3 and F(50)=165. 
# Find F(100000).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
