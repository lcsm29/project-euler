# Solution of;
# Project Euler Problem 628: Open chess positions
# https://projecteuler.net/problem=628
# 
# A position in chess is an (orientated) arrangement of chess pieces placed on 
# a chessboard of given size. In the following, we consider all positions in 
# which $n$ pawns are placed on a $n \times n$ board in such a way, that there 
# is a single pawn in every row and every column. We call such a position an 
# open position, if a rook, starting at the (empty) lower left corner and 
# using only moves towards the right or upwards, can reach the upper right 
# corner without moving onto any field occupied by a pawn. Let $f(n)$ be the 
# number of open positions for a $n \times n$ chessboard. For example, 
# $f(3)=2$, illustrated by the two open positions for a $3 \times 3$ 
# chessboard below. You are also given $f(5)=70$. Find $f(10^8)$ modulo 
# $1\,008\,691\,207$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 628
    timed.caller(dummy, n, i, prob_id)
