# Solution of;
# Project Euler Problem 571: Super Pandigital Numbers
# https://projecteuler.net/problem=571
# 
# A positive number is pandigital in base b if it contains all digits from 0 
# to b - 1 at least once when written in base b. A n-super-pandigital number 
# is a number that is simultaneously pandigital in all bases from 2 to n 
# inclusively. For example 978 = 11110100102 = 11000203 = 331024 = 124035 is 
# the smallest 5-super-pandigital number. Similarly, 1093265784 is the 
# smallest 10-super-pandigital number. The sum of the 10 smallest 
# 10-super-pandigital numbers is 20319792309. What is the sum of the 10 
# smallest 12-super-pandigital numbers?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 571
    timed.caller(dummy, n, i, prob_id)
