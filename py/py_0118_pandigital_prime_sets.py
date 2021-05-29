# Solution of;
# Project Euler Problem 118: Pandigital prime sets
# https://projecteuler.net/problem=118
# 
# Using all of the digits 1 through 9 and concatenating them freely to form 
# decimal integers, different sets can be formed. Interestingly with the set 
# {2,5,47,89,631}, all of the elements belonging to it are prime. How many 
# distinct sets containing each of the digits one through nine exactly once 
# contain only prime elements?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 118
    timed.caller(dummy, n, i, prob_id)
