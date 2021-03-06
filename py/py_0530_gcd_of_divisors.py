# Solution of;
# Project Euler Problem 530: GCD of Divisors
# https://projecteuler.net/problem=530
# 
# Every divisor d of a number n has a complementary divisor n/d. Let f(n) be 
# the sum of the greatest common divisor of d and n/d over all positive 
# divisors d of n, that is$f(n)=\displaystyle\sum\limits_{d|n}\, 
# \text{gcd}(d,\frac n d)$. Let F be the summatory function of f, that 
# is$F(k)=\displaystyle\sum\limits_{n=1}^k \, f(n)$. You are given that 
# F(10)=32 and F(1000)=12776. Find F(1015).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 530
    timed.caller(dummy, n, i, prob_id)
