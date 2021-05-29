# Solution of;
# Project Euler Problem 269: Polynomials with at least one integer root
# https://projecteuler.net/problem=269
# 
# A root or zero of a polynomial P(x) is a solution to the equation P(x) = 0. 
# Define Pn as the polynomial whose coefficients are the digits of n. For 
# example, P5703(x) = 5x3 + 7x2 + 3. We can see that:Pn(0) is the last digit 
# of n,Pn(1) is the sum of the digits of n,Pn(10) is n itself. Define Z(k) as 
# the number of positive integers, n, not exceeding k for which the polynomial 
# Pn has at least one integer root. It can be verified that Z(100 000) is 
# 14696. What is Z(1016)?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 269
    timed.caller(dummy, n, i, prob_id)
