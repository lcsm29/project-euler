# Solution of;
# Project Euler Problem 26: Reciprocal cycles
# https://projecteuler.net/problem=26
# 
# A unit fraction contains 1 in the numerator. The decimal representation of 
# the unit fractions with denominators 2 to 10 are given:1/2= 0. 51/3= 0. 
# (3)1/4= 0. 251/5= 0. 21/6= 0. 1(6)1/7= 0. (142857)1/8= 0. 1251/9= 0. 
# (1)1/10= 0. 1Where 0. 1(6) means 0. 166666. . . , and has a 1-digit 
# recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle. Find 
# the value of d < 1000 for which 1/d contains the longest recurring cycle in 
# its decimal fraction part.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)