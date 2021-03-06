# Solution of;
# Project Euler Problem 376: Nontransitive sets of dice
# https://projecteuler.net/problem=376
# 
# Consider the following set of dice with nonstandard pips:Die A: 1 4 4 4 4 
# 4Die B: 2 2 2 5 5 5Die C: 3 3 3 3 3 6A game is played by two players picking 
# a die in turn and rolling it. The player who rolls the highest value wins. 
# If the first player picks die A and the second player picks die B we 
# getP(second player wins) = 7/12 > 1/2If the first player picks die B and the 
# second player picks die C we getP(second player wins) = 7/12 > 1/2If the 
# first player picks die C and the second player picks die A we getP(second 
# player wins) = 25/36 > 1/2So whatever die the first player picks, the second 
# player can pick another die and have a larger than 50% chance of winning. A 
# set of dice having this property is called a nontransitive set of dice. We 
# wish to investigate how many sets of nontransitive dice exist. We will 
# assume the following conditions:There are three six-sided dice with each 
# side having between 1 and N pips, inclusive. Dice with the same set of pips 
# are equal, regardless of which side on the die the pips are located. The 
# same pip value may appear on multiple dice; if both players roll the same 
# value neither player wins. The sets of dice {A,B,C}, {B,C,A} and {C,A,B} are 
# the same set. For N = 7 we find there are 9780 such sets. How many are there 
# for N = 30 ?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 376
    timed.caller(dummy, n, i, prob_id)
