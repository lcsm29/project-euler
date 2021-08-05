# Solution of;
# Project Euler Problem 31: Coin sums
# https://projecteuler.net/problem=31
# 
# In the United Kingdom the currency is made up of pound (£) and pence (p). 
# There are eight coins in general circulation:
#   1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# 
# It is possible to make £2 in the following way:
#   1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# 
# How many different ways can £2 be made using any number of coins?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def fn_brute(target, coins=(1, 2, 5, 10, 20, 50, 100, 200)):
    arr = [1] + [0] * target
    for coin in coins:
        for i in range(len(arr) - coin):
            arr[i + coin] += arr[i]
    return arr[-1]


if __name__ == '__main__':
    n = 200
    i = 15_000
    prob_id = 31
    timed.caller(fn_brute, n, i, prob_id)
