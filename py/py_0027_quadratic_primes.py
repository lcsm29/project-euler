# Solution of;
# Project Euler Problem 27: Quadratic primes
# https://projecteuler.net/problem=27
# 
# Euler discovered the remarkable quadratic formula:
# 
#       n^2 + n + 41
# 
# It turns out that the formula will produce 40 primes for the consecutive
# integer values 0 <= n <= 39. However, when n = 40,
# 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, 
# and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
# 
# The incredible formula n^2 - 79n + 1601 was discovered, which produces
# 80 primes for the consecutive values 0 <= n <= 79. The product of the
# coefficients, −79 and 1601, is −126479. Considering quadratics of the form:
# 
#       n^2 + an + b, where |a| < 1000 and |b| <= 1000
#
#       where |n| is modulus/absolute value of n
#       e.g. |11| = 11 and |-4| = 4
#
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n = 0.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def fn_prime_brute(n):
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
    
    primes = tuple(i for i, b in enumerate(sieve(n)) if b)
    prod = nprime = 0
    for b in primes[::-1]:
        for p in [prime for prime in primes if prime < b][::-1]:
            a, length = p - b - 1, 0
            while length**2 + a * length + b in primes: length += 1
            if length > nprime: nprime, prod = length, a * b
    return prod


if __name__ == '__main__':
    n = 1_000
    i = 19
    prob_id = 27
    timed.caller(fn_prime_brute, n, i, prob_id)
