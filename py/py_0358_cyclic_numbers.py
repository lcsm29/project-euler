# Solution of;
# Project Euler Problem 358: Cyclic numbers
# https://projecteuler.net/problem=358
# 
# A cyclic number with n digits has a very interesting property:When it is 
# multiplied by 1, 2, 3, 4, . . . n, all the products have exactly the same 
# digits, in the same order, but rotated in a circular fashion!The smallest 
# cyclic number is the 6-digit number 142857 :142857 × 1 = 142857142857 × 2 = 
# 285714142857 × 3 = 428571142857 × 4 = 571428142857 × 5 = 714285142857 × 6 = 
# 857142 The next cyclic number is 0588235294117647 with 16 digits 
# :0588235294117647 × 1 = 05882352941176470588235294117647 × 2 = 
# 11764705882352940588235294117647 × 3 = 1764705882352941. . . 
# 0588235294117647 × 16 = 9411764705882352Note that for cyclic numbers, 
# leading zeros are important. There is only one cyclic number for which, the 
# eleven leftmost digits are 00000000137 and the five rightmost digits are 
# 56789 (i. e. , it has the form 00000000137. . . 56789 with an unknown number 
# of digits in the middle). Find the sum of all its digits.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 358
    timed.caller(dummy, n, i, prob_id)
