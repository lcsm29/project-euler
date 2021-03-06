# Solution of;
# Project Euler Problem 113: Non-bouncy numbers
# https://projecteuler.net/problem=113
# 
# Working from left-to-right if no digit is exceeded by the digit to its left 
# it is called an increasing number; for example, 134468. Similarly if no 
# digit is exceeded by the digit to its right it is called a decreasing 
# number; for example, 66420. We shall call a positive integer that is neither 
# increasing nor decreasing a "bouncy" number; for example, 155349. As n 
# increases, the proportion of bouncy numbers below n increases such that 
# there are only 12951 numbers below one-million that are not bouncy and only 
# 277032 non-bouncy numbers below 1010. How many numbers below a googol 
# (10100) are not bouncy?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 113
    timed.caller(dummy, n, i, prob_id)
