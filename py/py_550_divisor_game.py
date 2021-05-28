# Solution of;
# Project Euler Problem 550: Divisor game
# https://projecteuler.net/problem=550
# 
# Two players are playing a game, alternating turns. There are k piles of 
# stones. On each turn, a player has to choose a pile and replace it with two 
# piles of stones under the following two conditions: Both new piles must have 
# a number of stones more than one and less than the number of stones of the 
# original pile. The number of stones of each of the new piles must be a 
# divisor of the number of stones of the original pile. The first player 
# unable to make a valid move loses. Let f(n,k) be the number of winning 
# positions for the first player, assuming perfect play, when the game is 
# played with k piles each having between 2 and n stones (inclusively). 
# f(10,5)=40085. Find f(107,1012). Give your answer modulo 987654321.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
