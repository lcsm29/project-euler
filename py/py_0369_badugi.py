# Solution of;
# Project Euler Problem 369: Badugi
# https://projecteuler.net/problem=369
# 
# In a standard 52 card deck of playing cards, a set of 4 cards is a Badugi if 
# it contains 4 cards with no pairs and no two cards of the same suit. Let 
# f(n) be the number of ways to choose n cards with a 4 card subset that is a 
# Badugi. For example, there are 2598960 ways to choose five cards from a 
# standard 52 card deck, of which 514800 contain a 4 card subset that is a 
# Badugi, so f(5) = 514800. Find ∑ f(n) for 4 ≤ n ≤ 13.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 369
    timed.caller(dummy, n, i, prob_id)
