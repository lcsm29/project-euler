# Solution of;
# Project Euler Problem 240: Top Dice
# https://projecteuler.net/problem=240
# 
# There are 1111 ways in which five 6-sided dice (sides numbered 1 to 6) can 
# be rolled so that the top three sum to 15. Some examples are:D1,D2,D3,D4,D5 
# = 4,3,6,3,5D1,D2,D3,D4,D5 = 4,3,3,5,6D1,D2,D3,D4,D5 = 
# 3,3,3,6,6D1,D2,D3,D4,D5 = 6,6,3,3,3In how many ways can twenty 12-sided dice 
# (sides numbered 1 to 12) be rolled so that the top ten sum to 70?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
