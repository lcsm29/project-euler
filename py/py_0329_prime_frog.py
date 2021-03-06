# Solution of;
# Project Euler Problem 329: Prime Frog
# https://projecteuler.net/problem=329
# 
# Susan has a prime frog. Her frog is jumping around over 500 squares numbered 
# 1 to 500. He can only jump one square to the left or to the right, with 
# equal probability, and he cannot jump outside the range [1;500]. (if it 
# lands at either end, it automatically jumps to the only available square on 
# the next move. )When he is on a square with a prime number on it, he croaks 
# 'P' (PRIME) with probability 2/3 or 'N' (NOT PRIME) with probability 1/3 
# just before jumping to the next square. When he is on a square with a number 
# on it that is not a prime he croaks 'P' with probability 1/3 or 'N' with 
# probability 2/3 just before jumping to the next square. Given that the 
# frog's starting position is random with the same probability for every 
# square, and given that she listens to his first 15 croaks, what is the 
# probability that she hears the sequence PPPPNNPPPNPPNPN?Give your answer as 
# a fraction p/q in reduced form.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 329
    timed.caller(dummy, n, i, prob_id)
