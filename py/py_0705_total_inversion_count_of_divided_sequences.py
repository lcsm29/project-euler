# Solution of;
# Project Euler Problem 705: Total Inversion Count of Divided Sequences
# https://projecteuler.net/problem=705
# 
# The inversion count of a sequence of digits is the smallest number of 
# adjacent pairs that must be swapped to sort the sequence. For example, 34214 
# has inversion count of 5:$34214 \to 32414 \to 23414 \to 23144 \to 21344 
# \to12344$. If each digit of a sequence is replaced by one of its divisors a 
# divided sequence is obtained. For example, the sequence 332 has 8 divided 
# sequences: $\{332,331,312,311,132,131,112,111\}$. Define $G(N)$ to be the 
# concatenation of all primes less than $N$, ignoring any zero digit. For 
# example, $G(20) = 235711131719$. Define $F(N)$ to be the sum of the 
# inversion count for all possible divided sequences from the master sequence 
# $G(N)$. You are given $F(20) = 3312$ and $F(50) = 338079744$. Find 
# $F(10^8)$. Give your answer modulo $1\,000\,000\,007$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 705
    timed.caller(dummy, n, i, prob_id)
