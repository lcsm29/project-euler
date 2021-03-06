# Solution of;
# Project Euler Problem 469: Empty chairs
# https://projecteuler.net/problem=469
# 
# In a room N chairs are placed around a round table. Knights enter the room 
# one by one and choose at random an available empty chair. To have enough 
# elbow room the knights always leave at least one empty chair between each 
# other. When there aren't any suitable chairs left, the fraction C of empty 
# chairs is determined. We also define E(N) as the expected value of C. We can 
# verify that E(4) = 1/2 and E(6) = 5/9. Find E(1018). Give your answer 
# rounded to fourteen decimal places in the form 0. abcdefghijklmn.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 469
    timed.caller(dummy, n, i, prob_id)
