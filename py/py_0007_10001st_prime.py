# Solution of;
# Project Euler Problem 7: 10001st prime
# https://projecteuler.net/problem=7
# 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
# that the 6th prime is 13. What is the 10 001st prime number?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def fn_brute(n):
    assert n > 0, 'n should be greater than 0'
    assert type(n) == int, 'n should be an integer'
    if n in (1, 2): return n + 1
    primes_found = 2
    i = 3
    while primes_found < n:
        i += 2
        sqrt = int(i ** 0.5)
        for div in range(2, sqrt + 1):
            if i % div == 0:
                if div < sqrt: 
                    break
            elif div == sqrt:
                primes_found += 1
    return i


if __name__ == '__main__':
    n = 10001
    i = 10
    prob_id = 7
    timed.caller(fn_brute, n, i, prob_id)
