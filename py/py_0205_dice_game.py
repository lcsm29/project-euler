# Solution of;
# Project Euler Problem 205: Dice Game
# https://projecteuler.net/problem=205
# 
# Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 
# 3, 4. Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 
# 3, 4, 5, 6. Peter and Colin roll their dice and compare totals: the highest 
# total wins. The result is a draw if the totals are equal. What is the 
# probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded 
# to seven decimal places in the form 0. abcdefg
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 205
    timed.caller(dummy, n, i, prob_id)
