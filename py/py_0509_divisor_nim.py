# Solution of;
# Project Euler Problem 509: Divisor Nim
# https://projecteuler.net/problem=509
# 
# Anton and Bertrand love to play three pile Nim. However, after a lot of 
# games of Nim they got bored and changed the rules somewhat. They may only 
# take a number of stones from a pile that is a proper divisor of the number 
# of stones present in the pile. E. g. if a pile at a certain moment contains 
# 24 stones they may take only 1,2,3,4,6,8 or 12 stones from that pile. So if 
# a pile contains one stone they can't take the last stone from it as 1 isn't 
# a proper divisor of 1. The first player that can't make a valid move loses 
# the game. Of course both Anton and Bertrand play optimally. The triple 
# (a,b,c) indicates the number of stones in the three piles. Let S(n) be the 
# number of winning positions for the next player for 1 ≤ a, b, c ≤ n. S(10) = 
# 692 and S(100) = 735494. Find S(123456787654321) modulo 1234567890.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 509
    timed.caller(dummy, n, i, prob_id)
