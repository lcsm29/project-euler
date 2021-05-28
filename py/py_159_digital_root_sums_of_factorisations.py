# Solution of;
# Project Euler Problem 159: Digital root sums of factorisations
# https://projecteuler.net/problem=159
# 
# A composite number can be factored many different ways. For instance, not 
# including multiplication by one, 24 can be factored in 7 distinct ways:24 = 
# 2x2x2x324 = 2x3x424 = 2x2x624 = 4x624 = 3x824 = 2x1224 = 24Recall that the 
# digital root of a number, in base 10, is found by adding together the digits 
# of that number, and repeating that process until a number is arrived at that 
# is less than 10. Thus the digital root of 467 is 8. We shall call a Digital 
# Root Sum (DRS) the sum of the digital roots of the individual factors of our 
# number. The chart below demonstrates all of the DRS values for 24. 
# FactorisationDigital Root Sum2x2x2x392x3x492x2x6104x6103x8112x125246The 
# maximum Digital Root Sum of 24 is 11. The function mdrs(n) gives the maximum 
# Digital Root Sum of n. So mdrs(24)=11. Find ∑ mdrs(n) for 1 < n < 1,000,000.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
