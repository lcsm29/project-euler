# Solution of;
# Project Euler Problem 257: Angular Bisectors
# https://projecteuler.net/problem=257
# 
# Given is an integer sided triangle ABC with sides a ≤ b ≤ c. (AB = c, BC = a 
# and AC = b). The angular bisectors of the triangle intersect the sides at 
# points E, F and G (see picture below). The segments EF, EG and FG partition 
# the triangle ABC into four smaller triangles: AEG, BFE, CGF and EFG. It can 
# be proven that for each of these four triangles the ratio 
# area(ABC)/area(subtriangle) is rational. However, there exist triangles for 
# which some or all of these ratios are integral. How many triangles ABC with 
# perimeter≤100,000,000 exist so that the ratio area(ABC)/area(AEG) is 
# integral?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 257
    timed.caller(dummy, n, i, prob_id)
