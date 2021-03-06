# Solution of;
# Project Euler Problem 116: Red, green or blue tiles
# https://projecteuler.net/problem=116
# 
# A row of five grey square tiles is to have a number of its tiles replaced 
# with coloured oblong tiles chosen from red (length two), green (length 
# three), or blue (length four). If red tiles are chosen there are exactly 
# seven ways this can be done. If green tiles are chosen there are three ways. 
# And if blue tiles are chosen there are two ways. Assuming that colours 
# cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the grey tiles in 
# a row measuring five units in length. How many different ways can the grey 
# tiles in a row measuring fifty units in length be replaced if colours cannot 
# be mixed and at least one coloured tile must be used?NOTE: This is related 
# to Problem 117.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 116
    timed.caller(dummy, n, i, prob_id)
