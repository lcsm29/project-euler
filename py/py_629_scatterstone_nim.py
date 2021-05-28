# Solution of;
# Project Euler Problem 629: Scatterstone Nim
# https://projecteuler.net/problem=629
# 
# Alice and Bob are playing a modified game of Nim called Scatterstone Nim, 
# with Alice going first, alternating turns with Bob. The game begins with an 
# arbitrary set of stone piles with a total number of stones equal to $n$. 
# During a player's turn, he/she must pick a pile having at least $2$ stones 
# and perform a split operation, dividing the pile into an arbitrary set of 
# $p$ non-empty, arbitrarily-sized piles where $2 \leq p \leq k$ for some 
# fixed constant $k$. For example, a pile of size $4$ can be split into $\{1, 
# 3\}$ or $\{2, 2\}$, or $\{1, 1, 2\}$ if $k = 3$ and in addition $\{1, 1, 1, 
# 1\}$ if $k = 4$. If no valid move is possible on a given turn, then the 
# other player wins the game. A winning position is defined as a set of stone 
# piles where a player can ultimately ensure victory no matter what the other 
# player does. Let $f(n,k)$ be the number of winning positions for Alice on 
# her first turn, given parameters $n$ and $k$. For example, $f(5, 2) = 3$ 
# with winning positions $\{1, 1, 1, 2\}, \{1, 4\}, \{2, 3\}$. In contrast, 
# $f(5, 3) = 5$ with winning positions $\{1, 1, 1, 2\}, \{1, 1, 3\}, \{1, 4\}, 
# \{2, 3\}, \{5\}$. Let $g(n)$ be the sum of $f(n,k)$ over all $2 \leq k \leq 
# n$. For example, $g(7)=66$ and $g(10)=291$. Find $g(200)$ mod $(10^9 + 7)$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
