# Solution of;
# Project Euler Problem 259: Reachable Numbers
# https://projecteuler.net/problem=259
# 
# A positive integer will be called reachable if it can result from an 
# arithmetic expression obeying the following rules:Uses the digits 1 through 
# 9, in that order and exactly once each. Any successive digits can be 
# concatenated (for example, using the digits 2, 3 and 4 we obtain the number 
# 234). Only the four usual binary arithmetic operations (addition, 
# subtraction, multiplication and division) are allowed. Each operation can be 
# used any number of times, or not at all. Unary minus is not allowed. Any 
# number of (possibly nested) parentheses may be used to define the order of 
# operations. For example, 42 is reachable, since (1/23) * ((4*5)-6) * (78-9) 
# = 42. What is the sum of all positive reachable integers?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 259
    timed.caller(dummy, n, i, prob_id)
