# Solution of;
# Project Euler Problem 398: Cutting rope
# https://projecteuler.net/problem=398
# 
# Inside a rope of length n, n-1 points are placed with distance 1 from each 
# other and from the endpoints. Among these points, we choose m-1 points at 
# random and cut the rope at these points to create m segments. Let E(n, m) be 
# the expected length of the second-shortest segment. For example, E(3, 2) = 2 
# and E(8, 3) = 16/7. Note that if multiple segments have the same shortest 
# length the length of the second-shortest segment is defined as the same as 
# the shortest length. Find E(107, 100). Give your answer rounded to 5 decimal 
# places behind the decimal point.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 398
    timed.caller(dummy, n, i, prob_id)
