# Solution of;
# Project Euler Problem 495: Writing n as the product of k distinct positive integers
# https://projecteuler.net/problem=495
# 
# Let W(n,k) be the number of ways in which n can be written as the product of 
# k distinct positive integers. For example, W(144,4) = 7. There are 7 ways in 
# which 144 can be written as a product of 4 distinct positive integers:144 = 
# 1×2×4×18144 = 1×2×8×9144 = 1×2×3×24144 = 1×2×6×12144 = 1×3×4×12144 = 
# 1×3×6×8144 = 2×3×4×6Note that permutations of the integers themselves are 
# not considered distinct. Furthermore, W(100!,10) modulo 1 000 000 007 = 
# 287549200. Find W(10000!,30) modulo 1 000 000 007.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
