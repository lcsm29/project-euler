# Solution of;
# Project Euler Problem 7: 10001st prime
# https://projecteuler.net/problem=7
# 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
# that the 6th prime is 13. What is the 10 001st prime number?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed
from math import log

''' removed due to its slow speed
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
'''

def fn_sieve_eratosthenes(n):
    assert n > 0, 'n should be greater than 0'
    assert type(n) == int, 'n should be an integer'
    def eratosthenes(limit):
        arr = [True] * (limit + 1)
        i = 2
        while i * i <= limit:
            if arr[i]:
                for np in range(i * i, limit + 1, i):
                    arr[np] = False
            i += 1
        return arr
    if n == 1:
        return 2
    elif 1 < n <= 5:
        limit = n * n
    else:
        limit = int(n * (log(n) + log(log(n))))
    tf_table = eratosthenes(limit)
    counter = -2
    for i, prime in enumerate(tf_table):
        if prime:
            counter += 1
        if counter == n:
            return i

''' removed due to its slow speed
def fn_sieve_sundaram(n):
    assert n > 0, 'n should be greater than 0'
    assert type(n) == int, 'n should be an integer'
    def sundaram(limit):
        k = (limit - 2) // 2
        arr = [True] * (k + 1)
        for i in range(1, k + 1):
            j = i
            while i + j + 2 * i * j <= k:
                arr[i + j + 2 * i * j] = False
                j += 1
        return arr
    if n == 1:
        return 2
    elif 1 < n <= 5:
        limit = n * n
    else:
        limit = int(n * (log(n) + log(log(n))))
    tf_table = sundaram(limit)
    counter = 1
    for i in range(1, ((limit - 2) // 2) + 1):
        if tf_table[i]:
            counter += 1
            if counter == n:
                return 2 * i + 1
'''    

if __name__ == '__main__':
    n = 10001
    i = 110
    prob_id = 7
    # timed.caller(fn_brute, n, i, prob_id)
    timed.caller(fn_sieve_eratosthenes, n, i, prob_id)
    # timed.caller(fn_sieve_sundaram, n, i, prob_id)
