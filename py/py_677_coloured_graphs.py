# Solution of;
# Project Euler Problem 677: Coloured Graphs
# https://projecteuler.net/problem=677
# 
# Let $g(n)$ be the number of undirected graphs with $n$ nodes satisfying the 
# following properties:The graph is connected and has no cycles or multiple 
# edges. Each node is either red, blue, or yellow. A red node may have no more 
# than 4 edges connected to it. A blue or yellow node may have no more than 3 
# edges connected to it. An edge may not directly connect a yellow node to a 
# yellow node. For example, $g(2)=5$, $g(3)=15$, and $g(4) = 57$. You are also 
# given that $g(10) = 710249$ and $g(100) \equiv 919747298 
# \pmod{1\,000\,000\,007}$. Find $g(10\,000) \bmod 1\,000\,000\,007$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
