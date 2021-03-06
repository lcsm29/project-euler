# Solution of;
# Project Euler Problem 371: Licence plates
# https://projecteuler.net/problem=371
# 
# Oregon licence plates consist of three letters followed by a three digit 
# number (each digit can be from [0. . 9]). While driving to work Seth plays 
# the following game:Whenever the numbers of two licence plates seen on his 
# trip add to 1000 that's a win. E. g. MIC-012 and HAN-988 is a win and 
# RYU-500 and SET-500 too (as long as he sees them in the same trip). Find the 
# expected number of plates he needs to see for a win. Give your answer 
# rounded to 8 decimal places behind the decimal point. Note: We assume that 
# each licence plate seen is equally likely to have any three digit number on 
# it.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 371
    timed.caller(dummy, n, i, prob_id)
