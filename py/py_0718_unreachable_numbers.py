# Solution of;
# Project Euler Problem 718: Unreachable Numbers
# https://projecteuler.net/problem=718
# 
# Consider the equation$17^pa+19^pb+23^pc = n$ where $a$, $b$, $c$ and $p$ are 
# positive integers, i. e. $a,b,c,p>0$. For a given $p$ there are some values 
# of $n > 0$ for which the equation cannot be solved. We call these 
# unreachable values. Define $G(p)$ to be the sum of all unreachable values of 
# $n$ for the given value of $p$. For example $G(1) = 8253$ and $G(2)= 
# 60258000$. Find $G(6)$. Give your answer modulo $1\,000\,000\,007$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 718
    timed.caller(dummy, n, i, prob_id)
