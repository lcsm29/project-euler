# Solution of;
# Project Euler Problem 458: Permutations of Project
# https://projecteuler.net/problem=458
# 
# Consider the alphabet A made out of the letters of the word "project": 
# A={c,e,j,o,p,r,t}. Let T(n) be the number of strings of length n consisting 
# of letters from A that do not have a substring that is one of the 5040 
# permutations of "project". T(7)=77-7!=818503. Find T(1012). Give the last 9 
# digits of your answer.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
