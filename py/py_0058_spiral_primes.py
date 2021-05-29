# Solution of;
# Project Euler Problem 58: Spiral primes
# https://projecteuler.net/problem=58
# 
# Starting with 1 and spiralling anticlockwise in the following way, a square 
# spiral with side length 7 is formed. 37 36 35 34 33 32 3138 17 16 15 14 13 
# 3039 18 5 4 3 12 2940 19 6 1 2 11 2841 20 7 8 9 10 2742 21 22 23 24 25 2643 
# 44 45 46 47 48 49It is interesting to note that the odd squares lie along 
# the bottom right diagonal, but what is more interesting is that 8 out of the 
# 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 
# 62%. If one complete new layer is wrapped around the spiral above, a square 
# spiral with side length 9 will be formed. If this process is continued, what 
# is the side length of the square spiral for which the ratio of primes along 
# both diagonals first falls below 10%?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 58
    timed.caller(dummy, n, i, prob_id)
