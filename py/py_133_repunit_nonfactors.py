# Solution of;
# Project Euler Problem 133: Repunit nonfactors
# https://projecteuler.net/problem=133
# 
# A number consisting entirely of ones is called a repunit. We shall define 
# R(k) to be a repunit of length k; for example, R(6) = 111111. Let us 
# consider repunits of the form R(10n). Although R(10), R(100), or R(1000) are 
# not divisible by 17, R(10000) is divisible by 17. Yet there is no value of n 
# for which R(10n) will divide by 19. In fact, it is remarkable that 11, 17, 
# 41, and 73 are the only four primes below one-hundred that can be a factor 
# of R(10n). Find the sum of all the primes below one-hundred thousand that 
# will never be a factor of R(10n).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
