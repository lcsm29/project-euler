# Solution of;
# Project Euler Problem 17: Number letter counts
# https://projecteuler.net/problem=17
# 
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used? 
# 
# NOTE: Do not count spaces or hyphens. For example, 
# 342 (three hundred and forty-two) contains 23 letters and 
# 115 (one hundred and fifteen) contains 20 letters. The use of "and" 
# when writing out numbers is in compliance with British usage.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def fn_brute(n):
    length = 0
    for i in range(n + 1):
        length += len(''.join(big_conv(i)))
    return length


d19 = {i: v for i, v in enumerate('''
    zero one two three four five six seven eight nine
    ten eleven twelve thirteen fourteen fifteen
    sixteen seventeen eighteen nineteen'''.split())}
d99 = {i: v for i, v in zip(
        map(lambda x: x * 10, range(2, 10)), 
        'twenty thirty forty fifty sixty seventy eighty ninety'.split())}
dct = {**d19, **d99, 0: '', 100: 'hundred', 1_000: 'thousand'}
d = {int(1e0) : '',            int(1e1) : 'ten',
     int(1e2) : 'hundred',     int(1e3) : 'thousand',
     int(1e6) : 'million',     int(1e9) : 'billion',
     int(1e12): 'trillion',    int(1e15): 'quadrillion',
     int(1e18): 'quintillion', int(1e21): 'sextillion'}


def k_conv(n):
    if 0 <= n < 20:
        return [dct[n]]
    elif n < 100:
        ten, rest = divmod(n, 10)
        return [dct[ten * 10], dct[rest]]
    elif n < 1_000:
        hnd, rest = divmod(n, 100)
        return ([dct[hnd], dct[1e2], ('and' if n % 100 != 0 else '')] + k_conv(rest))


def big_conv(n):
    assert n < 1e24, 'Number out of range'
    neg = False
    if n < 0:
        n, neg = -n, True
    s = str(n)[::-1]
    l = [int(s[i:i+3][::-1]) for i in range(0, len(s), 3)]
    l.reverse()
    words = [['minus'] if neg else '']
    for i, tri_digit in enumerate(l):
        k = int(10 ** ((len(l) - 1 - i) * 3))
        words.append(k_conv(tri_digit))
        if d[k] != '':
            words.append([d[k]])
    flatten_words = []
    for l in words:
        flatten_words += l
    return flatten_words


if __name__ == '__main__':
    n = 1_000
    i = 570
    prob_id = 17
    timed.caller(fn_brute, n, i, prob_id)
