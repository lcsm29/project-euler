# Solution of;
# Project Euler Problem 520: Simbers
# https://projecteuler.net/problem=520
# 
# We define a simber to be a positive integer in which any odd digit, if 
# present, occurs an odd number of times, and any even digit, if present, 
# occurs an even number of times. For example, 141221242 is a 9-digit simber 
# because it has three 1's, four 2's and two 4's. Let Q(n) be the count of all 
# simbers with at most n digits. You are given Q(7) = 287975 and Q(100) mod 1 
# 000 000 123 = 123864868. Find (∑1≤u≤39 Q(2u)) mod 1 000 000 123.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 520
    timed.caller(dummy, n, i, prob_id)
