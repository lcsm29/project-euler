# Solution of;
# Project Euler Problem 107: Minimal network
# https://projecteuler.net/problem=107
# 
# The following undirected network consists of seven vertices and twelve edges 
# with a total weight of 243. The same network can be represented by the 
# matrix below. 
# ABCDEFGA-161221---B16--1720--C12--28-31-D211728-181923E-20-18--11F--3119--27G---231127-However, 
# it is possible to optimise the network by removing some edges and still 
# ensure that all points on the network remain connected. The network which 
# achieves the maximum saving is shown below. It has a weight of 93, 
# representing a saving of 243 − 93 = 150 from the original network. Using 
# network. txt (right click and 'Save Link/Target As. . . '), a 6K text file 
# containing a network with forty vertices, and given in matrix form, find the 
# maximum saving which can be achieved by removing redundant edges whilst 
# ensuring that the network remains connected.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
