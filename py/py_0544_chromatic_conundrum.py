# Solution of;
# Project Euler Problem 544: Chromatic Conundrum
# https://projecteuler.net/problem=544
# 
# Let F(r,c,n) be the number of ways to colour a rectangular grid with r rows 
# and c columns using at most n colours such that no two adjacent cells share 
# the same colour. Cells that are diagonal to each other are not considered 
# adjacent. For example, F(2,2,3) = 18, F(2,2,20) = 130340, and F(3,4,6) = 
# 102923670. Let S(r,c,n) = $\sum_{k=1}^{n}$ F(r,c,k). For example, S(4,4,15) 
# mod 109+7 = 325951319. Find S(9,10,1112131415) mod 109+7.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 544
    timed.caller(dummy, n, i, prob_id)
