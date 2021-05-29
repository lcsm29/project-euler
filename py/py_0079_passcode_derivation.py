# Solution of;
# Project Euler Problem 79: Passcode derivation
# https://projecteuler.net/problem=79
# 
# A common security method used for online banking is to ask the user for 
# three random characters from a passcode. For example, if the passcode was 
# 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected 
# reply would be: 317. The text file, keylog. txt, contains fifty successful 
# login attempts. Given that the three characters are always asked for in 
# order, analyse the file so as to determine the shortest possible secret 
# passcode of unknown length.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 79
    timed.caller(dummy, n, i, prob_id)
