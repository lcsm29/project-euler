# Solution of;
# Project Euler Problem 423: Consecutive die throws
# https://projecteuler.net/problem=423
# 
# Let n be a positive integer. A 6-sided die is thrown n times. Let c be the 
# number of pairs of consecutive throws that give the same value. For example, 
# if n = 7 and the values of the die throws are (1,1,5,6,6,6,3), then the 
# following pairs of consecutive throws give the same 
# value:(1,1,5,6,6,6,3)(1,1,5,6,6,6,3)(1,1,5,6,6,6,3)Therefore, c = 3 for 
# (1,1,5,6,6,6,3). Define C(n) as the number of outcomes of throwing a 6-sided 
# die n times such that c does not exceed π(n). 1For example, C(3) = 216, C(4) 
# = 1290, C(11) = 361912500 and C(24) = 4727547363281250000. Define S(L) as ∑ 
# C(n) for 1 ≤ n ≤ L. For example, S(50) mod 1 000 000 007 = 832833871. Find 
# S(50 000 000) mod 1 000 000 007. 1 π denotes the prime-counting function, i. 
# e. π(n) is the number of primes ≤ n.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 423
    timed.caller(dummy, n, i, prob_id)
