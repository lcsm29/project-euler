# Solution of;
# Project Euler Problem 10: Summation of primes
# https://projecteuler.net/problem=10
# 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def fn_sieve_e_sum(n):
    assert n > 0, 'n should be greater than 0'
    assert type(n) == int, 'n should be an integer'
    arr = [True] * (n + 1)
    arr[0] = arr[1] = False
    i = 2
    while i * i <= n:
        if arr[i]:
            for np in range(i * i, n + 1, i):
                arr[np] = False
        i += 1
    sum_primes = 0
    for i, prime in enumerate(arr):
        if prime:
            sum_primes += i
    return sum_primes


if __name__ == '__main__':
    n = 2_000_000
    i = 6
    prob_id = 10
    timed.caller(fn_sieve_e_sum, n, i, prob_id)
