# Solution of;
# Project Euler Problem 725: Digit sum numbers
# https://projecteuler.net/problem=725
# 
# A number where one digit is the sum of the other digits is called a digit 
# sum number or DS-number for short. For example, 352, 3003 and 32812 are 
# DS-numbers. We define $S(n)$ to be the sum of all DS-numbers of $n$ digits 
# or less. You are given $S(3) = 63270$ and $S(7) = 85499991450$. Find 
# $S(2020)$. Give your answer modulo $10^{16}$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 725
    timed.caller(dummy, n, i, prob_id)
