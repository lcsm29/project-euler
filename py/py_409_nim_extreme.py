# Solution of;
# Project Euler Problem 409: Nim Extreme
# https://projecteuler.net/problem=409
# 
# Let n be a positive integer. Consider nim positions where:There are n 
# non-empty piles. Each pile has size less than 2n. No two piles have the same 
# size. Let W(n) be the number of winning nim positions satisfying the 
# aboveconditions (a position is winning if the first player has a winning 
# strategy). For example, W(1) = 1, W(2) = 6, W(3) = 168, W(5) = 19764360 and 
# W(100) mod 1 000 000 007 = 384777056. Find W(10 000 000) mod 1 000 000 007.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
