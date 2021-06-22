# Solution of;
# Project Euler Problem 26: Reciprocal cycles
# https://projecteuler.net/problem=26
# 
# A unit fraction contains 1 in the numerator. The decimal representation of 
# the unit fractions with denominators 2 to 10 are given:
#
#   1/2 = 0.5
#   1/3 = 0.(3)
#   1/4 = 0.25
#   1/5 = 0.21
#   1/6 = 0.1(6)
#   1/7= 0.(142857)
#   1/8= 0.125
#   1/9= 0. (1)
#   1/10= 0.1
# 
# Where 0. 1(6) means 0. 166666. . . , and has a 1-digit recurring cycle. 
# It can be seen that 1/7 has a 6-digit recurring cycle. Find the value of
# d < 1000 for which 1/d contains the longest recurring cycle in its decimal
# fraction part.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def fn_prime_based(n):
    def sieve(limit):
        arr = [True] * (limit + 1)
        arr[0] = arr[1] = False
        i = 2
        while i * i <= limit:
            if arr[i]:
                for np in range(i * i, limit + 1, i):
                    arr[np] = False
            i += 1
        return arr
    length = {k: 0 for k, b in enumerate(sieve(n)) if b}
    for prime in length.keys():
        i, remainders = 10, []
        r = i % prime
        while r not in remainders:
            remainders.append(r)
            i = r * 10
            r = i % prime
        length[prime] = len(remainders) if 0 not in remainders else 0
    return max(length, key=length.get)


if __name__ == '__main__':
    n = 1000
    i = 10
    prob_id = 26
    timed.caller(fn_prime_based, n, i, prob_id)
