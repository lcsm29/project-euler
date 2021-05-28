# Solution of;
# Project Euler Problem 146: Investigating a Prime Pattern 
# https://projecteuler.net/problem=146
# 
# The smallest positive integer n for which the numbers n2+1, n2+3, n2+7, 
# n2+9, n2+13, and n2+27 are consecutive primes is 10. The sum of all such 
# integers n below one-million is 1242490. What is the sum of all such 
# integers n below 150 million?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
