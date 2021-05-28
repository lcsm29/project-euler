# Solution of;
# Project Euler Problem 475: Music festival
# https://projecteuler.net/problem=475
# 
# 12n musicians participate at a music festival. On the first day, they form 
# 3n quartets and practice all day. It is a disaster. At the end of the day, 
# all musicians decide they will never again agree to play with any member of 
# their quartet. On the second day, they form 4n trios, with every musician 
# avoiding any previous quartet partners. Let f(12n) be the number of ways to 
# organize the trios amongst the 12n musicians. You are given f(12) = 576 and 
# f(24) mod 1 000 000 007 = 509089824. Find f(600) mod 1 000 000 007.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
