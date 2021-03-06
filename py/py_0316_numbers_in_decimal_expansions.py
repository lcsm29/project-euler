# Solution of;
# Project Euler Problem 316: Numbers in decimal expansions
# https://projecteuler.net/problem=316
# 
# Let p = p1 p2 p3 . . . be an infinite sequence of random digits, selected 
# from {0,1,2,3,4,5,6,7,8,9} with equal probability. It can be seen that p 
# corresponds to the real number 0. p1 p2 p3 . . . . It can also be seen that 
# choosing a random real number from the interval [0,1) is equivalent to 
# choosing an infinite sequence of random digits selected from 
# {0,1,2,3,4,5,6,7,8,9} with equal probability. For any positive integer n 
# with d decimal digits, let k be the smallest index such that pk, pk+1, . . . 
# pk+d-1 are the decimal digits of n, in the same order. Also, let g(n) be the 
# expected value of k; it can be proven that g(n) is always finite and, 
# interestingly, always an integer number. For example, if n = 535, thenfor p 
# = 31415926535897. . . . , we get k = 9for p = 
# 355287143650049560000490848764084685354. . . , we get k = 36etc and we find 
# that g(535) = 1008. Given that $\sum \limits_{n = 2}^{999} {g \left ( \left 
# \lfloor \dfrac{10^6}{n} \right \rfloor \right )} = 27280188$, find $\sum 
# \limits_{n = 2}^{999999} {g \left ( \left \lfloor \dfrac{10^{16}}{n} \right 
# \rfloor \right )}$. Note: $\lfloor x \rfloor$ represents the floor function.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 316
    timed.caller(dummy, n, i, prob_id)
