# Solution of;
# Project Euler Problem 9: Special Pythagorean triplet
# https://projecteuler.net/problem=9
# 
# A Pythagorean triplet is a set of three natural numbers, a < b < c,
# for which, a2 + b2 = c2. For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. 
# Find the product abc.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def fn_brute(n):
    for a in range(int(n / 3), 1, -1):
        for b in range(int(n / 2), a, -1):
            c = n - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
    return 0


if __name__ == '__main__':
    n = 1000
    i = 50
    prob_id = 9
    timed.caller(fn_brute, n, i, prob_id)
