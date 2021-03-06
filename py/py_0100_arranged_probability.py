# Solution of;
# Project Euler Problem 100: Arranged probability
# https://projecteuler.net/problem=100
# 
# If a box contains twenty-one coloured discs, composed of fifteen blue discs 
# and six red discs, and two discs were taken at random, it can be seen that 
# the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2. The 
# next such arrangement, for which there is exactly 50% chance of taking two 
# blue discs at random, is a box containing eighty-five blue discs and 
# thirty-five red discs. By finding the first arrangement to contain over 1012 
# = 1,000,000,000,000 discs in total, determine the number of blue discs that 
# the box would contain.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 100
    timed.caller(dummy, n, i, prob_id)
