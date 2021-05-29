# Solution of;
# Project Euler Problem 294: Sum of digits - experience #23
# https://projecteuler.net/problem=294
# 
# For a positive integer k, define d(k) as the sum of the digits of k in its 
# usual decimal representation. Thus d(42) = 4+2 = 6. For a positive integer 
# n, define S(n) as the number of positive integers k < 10n with the following 
# properties :k is divisible by 23 andd(k) = 23. You are given that S(9) = 
# 263626 and S(42) = 6377168878570056. Find S(1112) and give your answer mod 
# 109.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 294
    timed.caller(dummy, n, i, prob_id)
