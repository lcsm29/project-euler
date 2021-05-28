# Solution of;
# Project Euler Problem 312: Cyclic paths on Sierpiński graphs
# https://projecteuler.net/problem=312
# 
# - A Sierpiński graph of order-1 (S1) is an equilateral triangle. - Sn+1 is 
# obtained from Sn by positioning three copies of Sn so that every pair of 
# copies has one common corner. Let C(n) be the number of cycles that pass 
# exactly once through all the vertices of Sn. For example, C(3) = 8 because 
# eight such cycles can be drawn on S3, as shown below:It can also be verified 
# that :C(1) = C(2) = 1C(5) = 71328803586048C(10 000) mod 108 = 37652224C(10 
# 000) mod 138 = 617720485Find C(C(C(10 000))) mod 138.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
