# Solution of;
# Project Euler Problem 441: The inverse summation of coprime couples
# https://projecteuler.net/problem=441
# 
# For an integer M, we define R(M) as the sum of 1/(p·q) for all the integer 
# pairs p and q which satisfy all of these conditions: 1 ≤ p < q ≤ M p + q ≥ M 
# p and q are coprime. We also define S(N) as the sum of R(i) for 2 ≤ i ≤ N. 
# We can verify that S(2) = R(2) = 1/2, S(10) ≈ 6. 9147 and S(100) ≈ 58. 2962. 
# Find S(107). Give your answer rounded to four decimal places.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 441
    timed.caller(dummy, n, i, prob_id)
