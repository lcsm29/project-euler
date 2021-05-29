# Solution of;
# Project Euler Problem 237: Tours on a 4 x n playing board
# https://projecteuler.net/problem=237
# 
# Let T(n) be the number of tours over a 4 × n playing board such that:The 
# tour starts in the top left corner. The tour consists of moves that are up, 
# down, left, or right one square. The tour visits each square exactly once. 
# The tour ends in the bottom left corner. The diagram shows one tour over a 4 
# × 10 board:T(10) is 2329. What is T(1012) modulo 108?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 237
    timed.caller(dummy, n, i, prob_id)
