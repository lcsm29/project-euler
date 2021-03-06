# Solution of;
# Project Euler Problem 459: Flipping game
# https://projecteuler.net/problem=459
# 
# The flipping game is a two player game played on a N by N square board. Each 
# square contains a disk with one side white and one side black. The game 
# starts with all disks showing their white side. A turn consists of flipping 
# all disks in a rectangle with the following properties:the upper right 
# corner of the rectangle contains a white diskthe rectangle width is a 
# perfect square (1, 4, 9, 16, . . . )the rectangle height is a triangular 
# number (1, 3, 6, 10, . . . )Players alternate turns. A player wins by 
# turning the grid all black. Let W(N) be the number of winning moves for the 
# first player on a N by N board with all disks white, assuming perfect play. 
# W(1) = 1, W(2) = 0, W(5) = 8 and W(102) = 31395. For N=5, the first player's 
# eight winning first moves are:Find W(106).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 459
    timed.caller(dummy, n, i, prob_id)
