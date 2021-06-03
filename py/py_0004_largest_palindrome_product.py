# Solution of;
# Project Euler Problem 4: Largest palindrome product
# https://projecteuler.net/problem=4
# 
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest 
# palindrome made from the product of two 3-digit numbers.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def fn_brute_tuned(n):
    max_pal = 0
    for first in range(n, int(n * 0.1), -1):
        if first ** 2 < max_pal:
            break
        for second in range(n, int(n * 0.1), -1):
            if first * second < max_pal:
                break
            if str(first * second) == str(first * second)[::-1]:
                max_pal = first * second
    return max_pal


def fn_fast_pal(n):
    max_pal = 9
    a = n
    while a >= 10 ** (len(str(n)) - 1):
        if a % 11 == 0:
            b, divided = n, 1
        else:
            b, divided = n - n % 11, 11
        while b >= a:
            if a * b <= max_pal:
                break
            if str(a * b) == str(a * b)[::-1]:
                max_pal = a * b
            b = b - divided
        a = a - 1
    return max_pal


if __name__ == '__main__':
    n = 999
    i = 420
    prob_id = 4
    timed.caller(fn_brute_tuned, n, i, prob_id)
    timed.caller(fn_fast_pal, n, i, prob_id)
