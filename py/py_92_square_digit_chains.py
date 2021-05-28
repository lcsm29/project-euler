# Solution of;
# Project Euler Problem 92: Square digit chains
# https://projecteuler.net/problem=92
# 
# A number chain is created by continuously adding the square of the digits in 
# a number to form a new number until it has been seen before. For example,44 
# → 32 → 13 → 10 → 1 → 185 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 
# 89Therefore any chain that arrives at 1 or 89 will become stuck in an 
# endless loop. What is most amazing is that EVERY starting number will 
# eventually arrive at 1 or 89. How many starting numbers below ten million 
# will arrive at 89?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
