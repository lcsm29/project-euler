# Solution of;
# Project Euler Problem 463: A weird recurrence relation
# https://projecteuler.net/problem=463
# 
# The function $f$ is defined for all positive integers as 
# follows:$f(1)=1$$f(3)=3$$f(2n)=f(n)$$f(4n + 1)=2f(2n + 1) - f(n)$$f(4n + 
# 3)=3f(2n + 1) - 2f(n)$The function $S(n)$ is defined as 
# $\sum_{i=1}^{n}f(i)$. $S(8)=22$ and $S(100)=3604$. Find $S(3^{37})$. Give 
# the last 9 digits of your answer.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 463
    timed.caller(dummy, n, i, prob_id)
