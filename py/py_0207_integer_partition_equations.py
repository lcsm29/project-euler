# Solution of;
# Project Euler Problem 207: Integer partition equations
# https://projecteuler.net/problem=207
# 
# For some positive integers k, there exists an integer partition of the form 
# 4t = 2t + k,where 4t, 2t, and k are all positive integers and t is a real 
# number. The first two such partitions are 41 = 21 + 2 and 41. 5849625. . . = 
# 21. 5849625. . . + 6. Partitions where t is also an integer are called 
# perfect. For any m ≥ 1 let P(m) be the proportion of such partitions that 
# are perfect with k ≤ m. Thus P(6) = 1/2. In the following table are listed 
# some values of P(m) P(5) = 1/1 P(10) = 1/2 P(15) = 2/3 P(20) = 1/2 P(25) = 
# 1/2 P(30) = 2/5 . . . P(180) = 1/4 P(185) = 3/13Find the smallest m for 
# which P(m) < 1/12345
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 207
    timed.caller(dummy, n, i, prob_id)
