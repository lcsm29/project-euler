# Solution of;
# Project Euler Problem 306: Paper-strip Game
# https://projecteuler.net/problem=306
# 
# The following game is a classic example of Combinatorial Game Theory:Two 
# players start with a strip of $n$ white squares and they take alternate 
# turns. On each turn, a player picks two contiguous white squares and paints 
# them black. The first player who cannot make a move loses. $n = 1$: No valid 
# moves, so the first player loses automatically. $n = 2$: Only one valid 
# move, after which the second player loses. $n = 3$: Two valid moves, but 
# both leave a situation where the second player loses. $n = 4$: Three valid 
# moves for the first player, who is able to win the game by painting the two 
# middle squares. $n = 5$: Four valid moves for the first player (shown below 
# in red), but no matter what the player does, the second player (blue) wins. 
# So, for $1 \le n \le 5$, there are 3 values of $n$ for which the first 
# player can force a win. Similarly, for $1 \le n \le 50$, there are 40 values 
# of $n$ for which the first player can force a win. For $1 \le n \le 1 000 
# 000$, how many values of $n$ are there for which the first player can force 
# a win?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
