# Solution of;
# Project Euler Problem 266: Pseudo Square Root
# https://projecteuler.net/problem=266
# 
# The divisors of 12 are: 1,2,3,4,6 and 12. The largest divisor of 12 that 
# does not exceed the square root of 12 is 3. We shall call the largest 
# divisor of an integer n that does not exceed the square root of n the pseudo 
# square root (PSR) of n. It can be seen that PSR(3102)=47. Let p be the 
# product of the primes below 190. Find PSR(p) mod 1016.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 266
    timed.caller(dummy, n, i, prob_id)
