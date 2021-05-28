# Solution of;
# Project Euler Problem 542: Geometric Progression with Maximum Sum
# https://projecteuler.net/problem=542
# 
# Let S(k) be the sum of three or more distinct positive integers having the 
# following properties:No value exceeds k. The values form a geometric 
# progression. The sum is maximal. S(4) = 4 + 2 + 1 = 7S(10) = 9 + 6 + 4 = 
# 19S(12) = 12 + 6 + 3 = 21S(1000) = 1000 + 900 + 810 + 729 = 3439Let $T(n) = 
# \sum_{k=4}^n (-1)^k S(k)$. T(1000) = 2268Find T(1017).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
