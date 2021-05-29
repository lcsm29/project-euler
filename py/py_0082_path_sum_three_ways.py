# Solution of;
# Project Euler Problem 82: Path sum: three ways
# https://projecteuler.net/problem=82
# 
# NOTE: This problem is a more challenging version of Problem 81.
# The minimal path sum in the 5 by 5 matrix below, by starting in any cell 
# in the left column and finishing in any cell in the right column, 
# and only moving up, down, and right, is indicated in asterisk(*); 
# the sum is equal to 994.
# 
#     131(.) 673(.) 234(*) 103(*) 018(*)
#     201(*) 096(*) 342(*) 965(.) 150(.)
#     630(.) 803(.) 746(.) 422(.) 111(.) 
#     537(.) 699(.) 497(.) 121(.) 956(.) 
#     805(.) 732(.) 524(.) 037(.) 331(.)
#  
# Find the minimal path sum from the left column to the right column in 
# matrix.txt, a 31K text file containing an 80 by 80 matrix.
# https://projecteuler.net/project/resources/p082_matrix.txt
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 82
    timed.caller(dummy, n, i, prob_id)
