# Solution of;
# Project Euler Problem 131: Prime cube partnership
# https://projecteuler.net/problem=131
# 
# There are some prime values, p, for which there exists a positive integer, 
# n, such that the expression n3 + n2p is a perfect cube. For example, when p 
# = 19, 83 + 82×19 = 123. What is perhaps most surprising is that for each 
# prime with this property the value of n is unique, and there are only four 
# such primes below one-hundred. How many primes below one million have this 
# remarkable property?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 131
    timed.caller(dummy, n, i, prob_id)
