# Solution of;
# Project Euler Problem 687: Shuffling Cards
# https://projecteuler.net/problem=687
# 
# A standard deck of 52 playing cards, which consists of thirteen ranks (Ace, 
# Two, . . . , Ten, King, Queen and Jack) each in four suits (Clubs, Diamonds, 
# Hearts and Spades), is randomly shuffled. Let us call a rank perfect if no 
# two cards of that same rank appear next to each other after the shuffle. It 
# can be seen that the expected number of ranks that are perfect after a 
# random shuffle equals $\frac {4324} {425} \approx 10. 1741176471$. Find the 
# probability that the number of perfect ranks is prime. Give your answer 
# rounded to 10 decimal places.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 687
    timed.caller(dummy, n, i, prob_id)
