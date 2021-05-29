# Solution of;
# Project Euler Problem 81: Path sum: two ways
# https://projecteuler.net/problem=81
# 
# In the 5 by 5 matrix below, the minimal path sum from the top left to the 
# bottom right, by only moving to the right and down, 
# is indicated in asterisk(*) and is equal to 2427.
# 
#     131(*) 673(.) 234(.) 103(.) 018(.)
#     201(*) 096(*) 342(*) 965(.) 150(.)
#     630(.) 803(.) 746(*) 422(*) 111(.) 
#     537(.) 699(.) 497(.) 121(*) 956(.) 
#     805(.) 732(.) 524(.) 037(*) 331(*)
#  
# Find the minimal path sum from the top left to the bottom right by only 
# moving right and down in matrix.txt, 
# https://projecteuler.net/project/resources/p081_matrix.txt
# a 31K text file containing an 80 by 80 matrix.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 81
    timed.caller(dummy, n, i, prob_id)
