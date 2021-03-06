# Solution of;
# Project Euler Problem 286: Scoring probabilities
# https://projecteuler.net/problem=286
# 
# Barbara is a mathematician and a basketball player. She has found that the 
# probability of scoring a point when shooting from a distance x is exactly (1 
# - x/q), where q is a real constant greater than 50. During each practice 
# run, she takes shots from distances x = 1, x = 2, . . . , x = 50 and, 
# according to her records, she has precisely a 2 % chance to score a total of 
# exactly 20 points. Find q and give your answer rounded to 10 decimal places.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 286
    timed.caller(dummy, n, i, prob_id)
