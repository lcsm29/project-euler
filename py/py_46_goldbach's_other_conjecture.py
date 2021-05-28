# Solution of;
# Project Euler Problem 46: Goldbach's other conjecture
# https://projecteuler.net/problem=46
# 
# It was proposed by Christian Goldbach that every odd composite number can be 
# written as the sum of a prime and twice a square. 9 = 7 + 2×1215 = 7 + 
# 2×2221 = 3 + 2×3225 = 7 + 2×3227 = 19 + 2×2233 = 31 + 2×12It turns out that 
# the conjecture was false. What is the smallest odd composite that cannot be 
# written as the sum of a prime and twice a square?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
