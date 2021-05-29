# Solution of;
# Project Euler Problem 310: Nim Square
# https://projecteuler.net/problem=310
# 
# Alice and Bob play the game Nim Square. Nim Square is just like ordinary 
# three-heap normal play Nim, but the players may only remove a square number 
# of stones from a heap. The number of stones in the three heaps is 
# represented by the ordered triple (a,b,c). If 0≤a≤b≤c≤29 then the number of 
# losing positions for the next player is 1160. Find the number of losing 
# positions for the next player if 0≤a≤b≤c≤100 000.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 310
    timed.caller(dummy, n, i, prob_id)
