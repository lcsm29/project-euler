# Solution of;
# Project Euler Problem 169: Exploring the number of different ways a number can be expressed as a sum of powers of 2
# https://projecteuler.net/problem=169
# 
# Define f(0)=1 and f(n) to be the number of different ways n can be expressed 
# as a sum of integer powers of 2 using each power no more than twice. For 
# example, f(10)=5 since there are five different ways to express 10:1 + 1 + 
# 81 + 1 + 4 + 41 + 1 + 2 + 2 + 42 + 4 + 42 + 8What is f(1025)?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
