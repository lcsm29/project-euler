# Solution of;
# Project Euler Problem 38: Pandigital multiples
# https://projecteuler.net/problem=38
# 
# Take the number 192 and multiply it by each of 1, 2, and 3:192 × 1 = 192192 
# × 2 = 384192 × 3 = 576By concatenating each product we get the 1 to 9 
# pandigital, 192384576. We will call 192384576 the concatenated product of 
# 192 and (1,2,3)The same can be achieved by starting with 9 and multiplying 
# by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the 
# concatenated product of 9 and (1,2,3,4,5). What is the largest 1 to 9 
# pandigital 9-digit number that can be formed as the concatenated product of 
# an integer with (1,2, . . . , n) where n > 1?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
