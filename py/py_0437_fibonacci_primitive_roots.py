# Solution of;
# Project Euler Problem 437: Fibonacci primitive roots
# https://projecteuler.net/problem=437
# 
# When we calculate 8n modulo 11 for n=0 to 9 we get: 1, 8, 9, 6, 4, 10, 3, 2, 
# 5, 7. As we see all possible values from 1 to 10 occur. So 8 is a primitive 
# root of 11. But there is more:If we take a closer look we see:1+8=98+9=17≡6 
# mod 119+6=15≡4 mod 116+4=104+10=14≡3 mod 1110+3=13≡2 mod 
# 113+2=52+5=75+7=12≡1 mod 11. So the powers of 8 mod 11 are cyclic with 
# period 10, and 8n + 8n+1 ≡ 8n+2 (mod 11). 8 is called a Fibonacci primitive 
# root of 11. Not every prime has a Fibonacci primitive root. There are 323 
# primes less than 10000 with one or more Fibonacci primitive roots and the 
# sum of these primes is 1480491. Find the sum of the primes less than 
# 100,000,000 with at least one Fibonacci primitive root.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 437
    timed.caller(dummy, n, i, prob_id)
