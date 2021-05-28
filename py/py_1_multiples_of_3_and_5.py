# Solution of;
# Project Euler Problem 1: Multiples of 3 and 5
# https://projecteuler.net/problem=1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def fn_short(n):
    return sum([i for i in range(1, n) if i % 3 == 0 or i % 5 == 0])


def fn_slower_than_short(n):
    lst = []
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            lst.append(i)
    return sum(lst)


def fn_add_directly(n):
    total = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


def fn_triple_sum(n):
    l3 = [i for i in range(3, n, 3)]
    l5 = [i for i in range(5, n, 5)]
    l15 = [i for i in range(15, n, 15)]
    return sum(l3) + sum(l5) - sum(l15)


def fn_triple_gauss_sum(n):
    def gauss_sum(num):
        if n % num != 0:
            mults_count = n // num
        else:
            mults_count = n // num - 1
        g_sum_for_count = (mults_count + 1) * 0.5 * mults_count
        return int(g_sum_for_count * num)
    return gauss_sum(3) + gauss_sum(5) - gauss_sum(15)


if __name__ == '__main__':
    n = 1000
    i = 10000
    timed.caller(fn_short, n, i)
    timed.caller(fn_add_directly, n, i)
    timed.caller(fn_slower_than_short, n, i)
    timed.caller(fn_triple_sum, n, i)
    timed.caller(fn_triple_gauss_sum, n, i)
