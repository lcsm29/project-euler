# Solution of;
# Project Euler Problem 5: Smallest multiple
# https://projecteuler.net/problem=5
# 
# 2520 is the smallest number that can be divided by each of the numbers from 
# 1 to 10 without any remainder. What is the smallest positive number that is 
# evenly divisible by all of the numbers from 1 to 20?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed

''' removed beceause it is too slow
def fn_brute(n):
    while n:
        n += 2
        for i in range(3, 21):
            if n % i != 0:
                break
            if i == 20 and n % i == 0:
                return n
'''

def fn_prime_based(n):
    def get_prime_factors(num):
        factors_counts = {i: 0 for i in range(1, n + 1)}
        i, divided = 2, num
        while i ** 2 <= divided:
            if divided % i:
                i += 1
            else:
                factors_counts[i] += 1
                divided //= i
        factors_counts[divided] += 1
        return factors_counts
    factors = {i: 0 for i in range(1, n + 1)}
    for i in range(1, n + 1):
        for k, v in get_prime_factors(i).items():
            if factors[k] < v:
                factors[k] = v
    prod = 1
    for elem in [k ** v for k, v in factors.items() if v != 0]:
        prod *= elem
    return prod

if __name__ == '__main__':
    n = 20
    i = 20_000
    prob_id = 5
    timed.caller(fn_prime_based, n, i, prob_id)
