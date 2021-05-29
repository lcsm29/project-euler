# Solution of;
# Project Euler Problem 323: Bitwise-OR operations on random integers
# https://projecteuler.net/problem=323
# 
# Let y0, y1, y2,. . . be a sequence of random unsigned 32 bit integers(i. e. 
# 0 ≤ yi < 232, every value equally likely). For the sequence xi the following 
# recursion is given:x0 = 0 andxi = xi-1| yi-1, for i > 0. ( | is the 
# bitwise-OR operator)It can be seen that eventually there will be an index N 
# such that xi = 232 -1 (a bit-pattern of all ones) for all i ≥ N. Find the 
# expected value of N. Give your answer rounded to 10 digits after the decimal 
# point.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 323
    timed.caller(dummy, n, i, prob_id)
