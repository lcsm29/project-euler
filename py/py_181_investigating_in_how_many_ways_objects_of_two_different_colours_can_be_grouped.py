# Solution of;
# Project Euler Problem 181: Investigating in how many ways objects of two different colours can be grouped
# https://projecteuler.net/problem=181
# 
# Having three black objects B and one white object W they can be grouped in 7 
# ways like this:(BBBW)(B,BBW)(B,B,BW)(B,B,B,W)(B,BB,W)(BBB,W)(BB,BW)In how 
# many ways can sixty black objects B and forty white objects W be thus 
# grouped?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
