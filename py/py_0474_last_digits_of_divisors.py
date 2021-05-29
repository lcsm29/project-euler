# Solution of;
# Project Euler Problem 474: Last digits of divisors
# https://projecteuler.net/problem=474
# 
# For a positive integer n and digits d, we define F(n, d) as the number of 
# the divisors of n whose last digits equal d. For example, F(84, 4) = 3. 
# Among the divisors of 84 (1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84), three 
# of them (4, 14, 84) have the last digit 4. We can also verify that F(12!, 
# 12) = 11 and F(50!, 123) = 17888. Find F(106!, 65432) modulo (1016 + 61).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 474
    timed.caller(dummy, n, i, prob_id)