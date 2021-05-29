# Solution of;
# Project Euler Problem 397: Triangle on parabola
# https://projecteuler.net/problem=397
# 
# On the parabola y = x2/k, three points A(a, a2/k), B(b, b2/k) and C(c, c2/k) 
# are chosen. Let F(K, X) be the number of the integer quadruplets (k, a, b, 
# c) such that at least one angle of the triangle ABC is 45-degree, with 1 ≤ k 
# ≤ K and -X ≤ a < b < c ≤ X. For example, F(1, 10) = 41 and F(10, 100) = 
# 12492. Find F(106, 109).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 397
    timed.caller(dummy, n, i, prob_id)
