# Solution of;
# Project Euler Problem 383: Divisibility comparison between factorials
# https://projecteuler.net/problem=383
# 
# Let f5(n) be the largest integer x for which 5x divides n. For example, 
# f5(625000) = 7. Let T5(n) be the number of integers i which satisfy 
# f5((2·i-1)!) < 2·f5(i!) and 1 ≤ i ≤ n. It can be verified that T5(103) = 68 
# and T5(109) = 2408210. Find T5(1018).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
