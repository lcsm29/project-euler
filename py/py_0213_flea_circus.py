# Solution of;
# Project Euler Problem 213: Flea Circus
# https://projecteuler.net/problem=213
# 
# A 30×30 grid of squares contains 900 fleas, initially one flea per square. 
# When a bell is rung, each flea jumps to an adjacent square at random 
# (usually 4 possibilities, except for fleas on the edge of the grid or at the 
# corners). What is the expected number of unoccupied squares after 50 rings 
# of the bell? Give your answer rounded to six decimal places.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 213
    timed.caller(dummy, n, i, prob_id)
