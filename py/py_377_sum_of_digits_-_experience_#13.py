# Solution of;
# Project Euler Problem 377: Sum of digits - experience #13
# https://projecteuler.net/problem=377
# 
# There are 16 positive integers that do not have a zero in their digits and 
# that have a digital sum equal to 5, namely: 5, 14, 23, 32, 41, 113, 122, 
# 131, 212, 221, 311, 1112, 1121, 1211, 2111 and 11111. Their sum is 17891. 
# Let f(n) be the sum of all positive integers that do not have a zero in 
# their digits and have a digital sum equal to n. Find $\displaystyle 
# \sum_{i=1}^{17} f(13^i)$. Give the last 9 digits as your answer.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
