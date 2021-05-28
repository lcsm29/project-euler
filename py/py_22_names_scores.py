# Solution of;
# Project Euler Problem 22: Names scores
# https://projecteuler.net/problem=22
# 
# Using names. txt (right click and 'Save Link/Target As. . . '), a 46K text 
# file containing over five-thousand first names, begin by sorting it into 
# alphabetical order. Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to obtain a 
# name score. For example, when the list is sorted into alphabetical order, 
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the 
# list. So, COLIN would obtain a score of 938 × 53 = 49714. What is the total 
# of all the name scores in the file?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
