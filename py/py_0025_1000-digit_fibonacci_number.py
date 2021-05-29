# Solution of;
# Project Euler Problem 25: 1000-digit Fibonacci number
# https://projecteuler.net/problem=25
# 
# The Fibonacci sequence is defined by the recurrence relation:Fn = Fn−1 + 
# Fn−2, where F1 = 1 and F2 = 1. Hence the first 12 terms will be:F1 = 1F2 = 
# 1F3 = 2F4 = 3F5 = 5F6 = 8F7 = 13F8 = 21F9 = 34F10 = 55F11 = 89F12 = 144The 
# 12th term, F12, is the first term to contain three digits. What is the index 
# of the first term in the Fibonacci sequence to contain 1000 digits?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 25
    timed.caller(dummy, n, i, prob_id)
