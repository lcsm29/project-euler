# Solution of;
# Project Euler Problem 254: Sums of Digit Factorials
# https://projecteuler.net/problem=254
# 
# Define f(n) as the sum of the factorials of the digits of n. For example, 
# f(342) = 3! + 4! + 2! = 32. Define sf(n) as the sum of the digits of f(n). 
# So sf(342) = 3 + 2 = 5. Define g(i) to be the smallest positive integer n 
# such that sf(n) = i. Though sf(342) is 5, sf(25) is also 5, and it can be 
# verified that g(5) is 25. Define sg(i) as the sum of the digits of g(i). So 
# sg(5) = 2 + 5 = 7. Further, it can be verified that g(20) is 267 and ∑ sg(i) 
# for 1 ≤ i ≤ 20 is 156. What is ∑ sg(i) for 1 ≤ i ≤ 150?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
